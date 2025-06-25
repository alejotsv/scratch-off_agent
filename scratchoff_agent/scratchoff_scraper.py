import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from scratchoff_selectors.ticket_page import GENERAL_LEVEL_SELECTORS, PAGE_LEVEL_SELECTORS

load_dotenv()

async def extract_overall_odds(page) -> str:
    selector = PAGE_LEVEL_SELECTORS["overall_odds"]
    element = await page.wait_for_selector(selector, timeout=10000)

    if element:
        return (await element.inner_text()).strip()
    return None

async def fetch_scratchoff_data(refresh: bool = True, max_games: int = None) -> list:
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

        for index, row in enumerate(rows):
            if max_games is not None and index >= max_games:
                break

            game_data = {}

            try:
                # Game name and link
                link_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["game_link"])
                if link_el:
                    game_data["name"] = (await link_el.inner_text()).strip()
                    href = await link_el.get_attribute("href")
                    if href:
                        full_url = href if href.startswith("http") else f"https://floridalottery.com{href}"
                        game_data["url"] = full_url

                        # Extract ID from URL
                        parsed_url = urlparse(full_url)
                        game_id = parse_qs(parsed_url.query).get("id", [None])[0]
                        game_data["id"] = game_id

                    else:
                        print(f"⚠️ Skipping game {game_data.get('name', '[Unknown]')} due to missing href")

                # Ticket price
                price_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["ticket_price"])
                if price_el:
                    game_data["ticket_price"] = (await price_el.inner_text()).strip()

                # Top prize
                top_prize_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["top_prize"])
                if top_prize_el:
                    game_data["top_prize"] = (await top_prize_el.inner_text()).strip()

                # Top prizes remaining
                remaining_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["top_prizes_remaining"])
                if remaining_el:
                    game_data["top_prizes_remaining"] = (await remaining_el.inner_text()).strip()

                # Visit individual page for overall odds
                if "url" in game_data:
                    print(f"🔍 Visiting: {game_data['url']}")
                    try:
                        detail_page = await browser.new_page()
                        await detail_page.goto(game_data["url"], timeout=60000, wait_until="domcontentloaded")
                        overall_odds = await extract_overall_odds(detail_page)
                        game_data["overall_odds"] = overall_odds
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
