from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from scratchoff_agent.agent import ScratchoffQAAgent
import os

app = FastAPI()

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
    limit: int = Query(5, ge=1, le=250),
):
    results = agent.get_best_prize_odds_filtered(
        min_prize=min_prize,
        max_prize=max_prize,
        top_prize_only=top_prize_only,
        limit=limit,
    )
    return results
