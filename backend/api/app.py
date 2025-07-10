from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Query, Header
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.decision_engine import parse_user_goal_with_claude
from backend.nlg_agent import summarize_recommendation
from backend.odds_agent import ScratchoffQAAgent
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("UI_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join("data", "scratchoff_data.json")
agent = ScratchoffQAAgent(DATA_PATH)


@app.get("/")
def root():
    return {"message": "Scratch-off API is running!"}


@app.get("/best-overall-odds")
def get_best_overall(limit: int = Query(5, ge=1, le=250)):
    results = agent.get_best_overall_game_odds(limit=limit)
    return results


@app.get("/best-prize-odds")
def get_best_prize_odds(
    min_prize: float = Query(0),
    max_prize: float = Query(1e6),
    top_prize_only: bool = Query(False),
    limit: int = Query(5, ge=1, le=1000),
):
    results = agent.get_best_prize_odds_filtered(
        min_prize=min_prize,
        max_prize=max_prize,
        top_prize_only=top_prize_only,
        limit=limit,
    )
    return results


class QuestionPayload(BaseModel):
    question: str

RELEVANT_KEYWORDS = [
    "ticket", "scratch", "scratch-off", "lottery", "odds", "prize", "jackpot", "winning",
    "remaining", "top prize", "cashword", "gold rush", "multiplier", "best game", "claim",
    "overall odds", "instant win", "number of prizes"
]

def is_relevant_question(question: str) -> bool:
    q = question.lower()
    return any(keyword in q for keyword in RELEVANT_KEYWORDS)

@app.post("/ask")
def ask_question(
    payload: QuestionPayload,
    odds_debug: Optional[str] = Header(default="false", alias="odds-debug")
):
    question = payload.question.strip()
    if not question:
        return JSONResponse(content={"error": "Question cannot be empty"}, status_code=400)

    # Check if it's within the expected topic
    if not is_relevant_question(question):
        return {
            "response": "This assistant only answers questions about Florida Lottery scratch-off tickets. Please ask about ticket odds, prizes, or top games."
        }

    try:
        # Use Claude to decide intent and filtering
        debug_info = parse_user_goal_with_claude(question)

        intent = debug_info.get("intent", "unsupported")
        if intent not in {"best_overall", "best_prize_odds"}:
            return {
                "response": "I'm only trained to help with scratch-off odds and prizes. Try asking about the best tickets or remaining prizes."
            }

        # Decide which games to use
        games = []

        if intent == "best_overall":
            ceiling = debug_info.get("ticket_price_ceiling", float("inf"))
            games = [
                g for g in agent.get_best_overall_game_odds(limit=1000)
                if g.get("ticket_price") is not None and g["ticket_price"] <= ceiling
            ]

        elif intent == "best_prize_odds":
            min_prize = debug_info.get("min_prize", 0)
            max_prize = debug_info.get("max_prize", float("inf"))
            top_prize_only = debug_info.get("top_prize_only", False)
            price_ceiling = debug_info.get("ticket_price_ceiling", float("inf"))

            games = [
                g for g in agent.get_best_prize_odds_filtered(
                    min_prize=min_prize,
                    max_prize=max_prize,
                    top_prize_only=top_prize_only,
                    limit=1000,
                )
                if g.get("ticket_price") is not None and g["ticket_price"] <= price_ceiling
            ]

        # Fallback if filtering yielded nothing
        if not games:
            games = agent.games

        # Final Claude response
        response = summarize_recommendation(games, question)

        # Build result
        show_debug = odds_debug.lower() == "true"
        result = {"response": response}
        if show_debug:
            result["debug"] = debug_info
            result["games"] = games
        return result

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
