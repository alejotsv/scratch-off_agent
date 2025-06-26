import json
import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from scratchoff_selectors.ticket_page import GENERAL_LEVEL_SELECTORS, PAGE_LEVEL_SELECTORS

load_dotenv()

def normalize_odds_format(odds_str):
    if odds_str and "1-in-" in odds_str:
        return odds_str.replace("1-in-", "1:")
    return odds_str

def normalize_currency(value):
    if not value:
        return None
    try:
        return float(value.replace("$", "").replace(",", "").strip())
    except Exception:
        return value

async def extract_overall_odds(page) -> str:
    selector = PAGE_LEVEL_SELECTORS["overall_odds"]
    await page.wait_for_selector(selector)
    element = await page.query_selector(selector)
    if element:
        return normalize_odds_format((await element.inner_text()).strip())
    return None

async def extract_prize_breakdown(page) -> list:
    selector = PAGE_LEVEL_SELECTORS["prize_breakdown"]
    await page.wait_for_selector(selector)
    rows = await page.query_selector_all(selector)
    breakdown = []

    for row in rows:
        try:
            cells = await row.query_selector_all("td, th")
            if len(cells) == 3:
                prize = await cells[0].inner_text()
                odds = await cells[1].inner_text()
                remaining = await cells[2].inner_text()
                breakdown.append({
                    "prize": normalize_currency(prize),
                    "odds": normalize_odds_format(odds.strip()),
                    "remaining": remaining.strip()
                })
        except Exception:
            continue

    return breakdown

async def fetch_scratchoff_data(refresh: bool = True, limit: int = None) -> list:
    all_data = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        base_url = os.getenv("SCRATCHOFF_BASE_URL")
        if not base_url:
            raise EnvironmentError("SCRATCHOFF_BASE_URL not set in environment variables.")

        await page.goto(base_url)
        await page.wait_for_selector(GENERAL_LEVEL_SELECTORS["table_row"])

        rows = await page.query_selector_all(GENERAL_LEVEL_SELECTORS["table_row"])
        print(f"\n🎯 Found {len(rows)} ticket rows:\n")

        rows = rows[:limit] if limit else rows

        for row in rows:
            game_data = {}

            try:
                link_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["game_link"])
                if link_el:
                    game_data["name"] = (await link_el.inner_text()).strip()
                    href = await link_el.get_attribute("href")
                    if href:
                        full_url = href if href.startswith("http") else f"https://floridalottery.com{href}"
                        game_data["url"] = full_url

                        parsed_url = urlparse(full_url)
                        game_id = parse_qs(parsed_url.query).get("id", [None])[0]
                        game_data["id"] = game_id

                price_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["ticket_price"])
                if price_el:
                    raw_price = (await price_el.inner_text()).strip()
                    game_data["ticket_price"] = normalize_currency(raw_price)

                top_prize_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["top_prize"])
                if top_prize_el:
                    raw_prize = (await top_prize_el.inner_text()).strip()
                    game_data["top_prize"] = normalize_currency(raw_prize)

                remaining_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["top_prizes_remaining"])
                if remaining_el:
                    game_data["top_prizes_remaining"] = (await remaining_el.inner_text()).strip()

                if "url" in game_data:
                    print(f"🔍 Visiting: {game_data['url']}")
                    try:
                        detail_page = await browser.new_page()
                        await detail_page.goto(game_data["url"], timeout=60000, wait_until="domcontentloaded")
                        overall_odds = await extract_overall_odds(detail_page)
                        game_data["overall_odds"] = overall_odds
                        prize_breakdown = await extract_prize_breakdown(detail_page)
                        game_data["odds_breakdown"] = prize_breakdown
                        await detail_page.close()
                    except Exception as e:
                        print(f"⚠️ Failed to retrieve odds for {game_data['url']}: {e}")
                        game_data["overall_odds"] = None
                else:
                    print("⚠️ Skipping row due to missing URL.")
                    continue

                all_data.append(game_data)

            except Exception as e:
                print(f"❌ Skipping row due to error: {e}")
                continue

        await browser.close()

    return all_data

class ScratchoffQAAgent:
    def __init__(self, data_path: str):
        self.data_path = data_path
        with open(data_path, "r", encoding="utf-8") as f:
            self.games = json.load(f)

    def get_best_overall_game_odds(self, limit=5):
        def parse(odds):
            try:
                return float(odds.split(":")[-1])
            except:
                return float("inf")

        sorted_games = sorted(
            [g for g in self.games if g.get("overall_odds")],
            key=lambda g: parse(g["overall_odds"])
        )
        return sorted_games[:limit]

    def get_best_prize_odds(self, min_prize=0, max_prize=float("inf"), limit=5):
        all_prizes = []
        for game in self.games:
            if not game.get("odds_breakdown"):
                continue
            for prize_entry in game["odds_breakdown"]:
                prize = prize_entry.get("prize")
                odds = prize_entry.get("odds")
                if prize is not None and odds:
                    try:
                        odds_value = float(odds.split(":")[-1])
                        if min_prize <= prize <= max_prize:
                            all_prizes.append({
                                "game": game["name"],
                                "ticket_price": game.get("ticket_price"),
                                "prize": prize,
                                "odds": odds,
                                "remaining": prize_entry.get("remaining"),
                                "game_id": game.get("id")
                            })
                    except:
                        continue

        all_prizes.sort(key=lambda x: float(x["odds"].split(":")[-1]))
        return all_prizes[:limit]
