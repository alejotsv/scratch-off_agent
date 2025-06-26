import json
from pathlib import Path


class ScratchoffQAAgent:
    def __init__(self, data_path: str = "data/scratchoff_data.json"):
        self.data_path = Path(data_path)
        self.games = self._load_data()

    def _load_data(self):
        if not self.data_path.exists():
            raise FileNotFoundError(f"Scratch-off data not found at {self.data_path}")
        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_best_overall_odds(self):
        def parse_odds(odds_str):
            try:
                if odds_str and "1-in-" in odds_str.lower():
                    return float(odds_str.lower().split("1-in-")[-1].strip())
            except Exception:
                return None
            return None

        best_games = []
        best_odds = float("inf")

        for game in self.games:
            odds_value = parse_odds(game.get("overall_odds"))
            if odds_value and odds_value < best_odds:
                best_odds = odds_value
                best_games = [game]
            elif odds_value and odds_value == best_odds:
                best_games.append(game)

        return best_games
