import asyncio
import json
import os
from backend.scratchoff_scraper import fetch_scratchoff_data

OUTPUT_FILE = "data/scratchoff_data.json"
MAX_GAMES = None  # Change this to None to scrape all games

async def main():
    data = await fetch_scratchoff_data(refresh=True, max_games=MAX_GAMES)

    if not data:
        print("⚠️ No data was collected. Exiting without writing file.")
        return

    os.makedirs("data", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Finished scraping. Total records: {len(data)}")
    print(f"📁 Data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
