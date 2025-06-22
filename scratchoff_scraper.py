import asyncio
from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("SCRATCHOFF_BASE_URL")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(BASE_URL)
        await page.wait_for_selector('tr.row-rounded')

        rows = await page.query_selector_all('tr.row-rounded')

        print(f"\n🎯 Found {len(rows)} ticket rows:\n")

        with open("data/scratchoff_links.txt", "w") as f:
            pass

        for row in rows:
            a_tag = await row.query_selector('th a')
            if a_tag:
                href = await a_tag.get_attribute('href')
                if href and href.startswith("/"):
                    href = "https://floridalottery.com" + href
                with open("data/scratchoff_links.txt", "a") as f:
                    f.write(href + "\n")
                print(href + " added to file.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
