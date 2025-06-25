from playwright.async_api import async_playwright
import os
from scratchoff_selectors.ticket_page import GENERAL_LEVEL_SELECTORS, PAGE_LEVEL_SELECTORS
from dotenv import load_dotenv

load_dotenv()

async def extract_overall_odds(page) -> str:
    selector = PAGE_LEVEL_SELECTORS["overall_odds"]
    element = await page.query_selector(selector)
    if element:
        return (await element.inner_text()).strip()
    return None

async def fetch_scratchoff_data(refresh: bool = False) -> list:
    all_data = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(os.getenv("SCRATCHOFF_BASE_URL"))
        await page.wait_for_selector(GENERAL_LEVEL_SELECTORS["table_row"])

        rows = await page.query_selector_all(GENERAL_LEVEL_SELECTORS["table_row"])
        print(f"\n🎯 Found {len(rows)} ticket rows:\n")

        for row in rows:
            game_data = {}

            # Game name and link
            link_el = await row.query_selector(GENERAL_LEVEL_SELECTORS["game_link"])
            if link_el:
                game_data["name"] = (await link_el.inner_text()).strip()
                href = await link_el.get_attribute("href")
                if href:
                    full_url = href if href.startswith("http") else f"https://floridalottery.com{href}"
                    game_data["url"] = full_url

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
                detail_page = await browser.new_page()
                await detail_page.goto(game_data["url"])
                overall_odds = await extract_overall_odds(detail_page)
                await detail_page.close()
                game_data["overall_odds"] = overall_odds

            all_data.append(game_data)

        await browser.close()

    return all_data
