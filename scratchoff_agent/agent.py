import json

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

    def get_best_prize_odds_filtered(
            self,
            min_prize=0,
            max_prize=float("inf"),
            top_prize_only=False,
            limit=5
    ):
        all_prizes = []

        def approx_equal(a, b, tol=0.01):
            return abs(a - b) <= tol

        for game in self.games:
            if not game.get("odds_breakdown"):
                continue

            top_prize = game.get("top_prize")
            try:
                top_prize = float(top_prize) if top_prize is not None else None
            except:
                top_prize = None

            for prize_entry in game["odds_breakdown"]:
                prize_raw = prize_entry.get("prize")
                odds = prize_entry.get("odds")

                try:
                    prize = float(prize_raw)
                    odds_value = float(odds.split(":")[-1])
                except:
                    continue  # skip bad values

                if not (min_prize <= prize <= max_prize):
                    continue

                if top_prize_only:
                    if top_prize is None or not approx_equal(prize, top_prize):
                        continue

                all_prizes.append({
                    "game": game["name"],
                    "ticket_price": game.get("ticket_price"),
                    "prize": prize,
                    "odds": odds,
                    "remaining": prize_entry.get("remaining"),
                    "game_id": game.get("id")
                })

        all_prizes.sort(key=lambda x: float(x["odds"].split(":")[-1]))
        return all_prizes[:limit]

