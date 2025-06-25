import asyncio
import json
import os
from scratchoff_agent.scratchoff_scraper import fetch_scratchoff_data

OUTPUT_FILE = "data/scratchoff_data.json"

async def main():
    # Ask user whether to refresh the data
    refresh = False
    if os.path.exists(OUTPUT_FILE):
        user_input = input(f"\n📄 A previous dataset exists at {OUTPUT_FILE}. Do you want to refresh it? (Y/N): ").strip().lower()
        refresh = user_input == "y"

    # Fetch data
    data = await fetch_scratchoff_data(refresh=refresh)

    # Ensure 'data' directory exists
    os.makedirs("data", exist_ok=True)

    # Write to JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Finished scraping. Total records: {len(data)}")
    print(f"📁 Data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
