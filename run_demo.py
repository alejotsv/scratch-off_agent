import json

from scratchoff_agent.odds_agent import ScratchoffQAAgent
from scratchoff_agent.nlg_agent import summarize_recommendation

DATA_FILE = "data/scratchoff_data.json"

def load_data(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("🤖 Loading scratch-off game data...")
    games = load_data(DATA_FILE)

    # Initialize odds agent using the JSON file
    qa_agent = ScratchoffQAAgent(DATA_FILE)

    # Get top 5 games with best overall odds
    top_games = qa_agent.get_best_overall_game_odds(limit=5)

    # Define user intent / goal
    user_goal = "I want the best odds under $30"

    # Generate explanation using Claude
    print("\n💬 Generating summary using Claude Sonnet 4...\n")
    summary = summarize_recommendation(top_games, user_goal)

    print("📝 Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
