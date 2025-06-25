GENERAL_LEVEL_SELECTORS = {
    "table_row": "//tbody/tr[contains(@class, 'row-rounded')]",
    "game_name": "th a span",
    "game_link": "th a",
    "top_prize": "td:nth-of-type(1)",
    "top_prizes_remaining": "td:nth-of-type(2) a",
    "ticket_price": "td:nth-of-type(3)"
}

PAGE_LEVEL_SELECTORS = {
    "overall_odds": "//div[contains(@class, 'cmp-infolist__item-title') and text()='Overall Odds']/following-sibling::div/p",
    "odds_table_rows": "//table[contains(@class, 'font-sans-tds')]//tbody/tr"
}
