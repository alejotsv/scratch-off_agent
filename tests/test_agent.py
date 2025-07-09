from backend.odds_agent import ScratchoffQAAgent

# Path to your JSON data file
DATA_PATH = "../data/scratchoff_data.json"

def display_games(games):
    for game in games:
        print(f"\n🎟️ Game: {game['name']}")
        if "overall_odds" in game:
            print(f"📊 Overall Odds: {game['overall_odds']}")
        if "ticket_price" in game:
            print(f"💵 Ticket Price: ${game['ticket_price']}")
        if "top_prize" in game:
            print(f"🏆 Top Prize: ${game['top_prize']}")
        if "odds_breakdown" in game:
            print("🔍 Odds Breakdown:")
            for prize in game["odds_breakdown"]:
                print(f"  - ${prize['prize']}: {prize['odds']} ({prize['remaining']} left)")

def display_prize_odds(prizes):
    for entry in prizes:
        print(f"\n🎟️ Game: {entry['game']} (ID: {entry['game_id']})")
        print(f"💵 Ticket Price: ${entry['ticket_price']}")
        print(f"🏆 Prize: ${entry['prize']}")
        print(f"📊 Odds: {entry['odds']}")
        print(f"🔢 Remaining: {entry['remaining']}")

def main():
    agent = ScratchoffQAAgent(DATA_PATH)

    print("\n📈 Top 5 games with best general odds:")
    best_general = agent.get_best_overall_game_odds(limit=5)
    display_games(best_general)

    print("\n💰 Top 5 best odds for prizes between $500 and $1000:")
    best_prizes = agent.get_best_prize_odds(min_prize=500, max_prize=1000, limit=5)
    display_prize_odds(best_prizes)

if __name__ == "__main__":
    main()
