# 🎰 Scratchy – AI-Powered Lottery Odds Advisor

Scratchy is an AI-powered web app that helps users make smarter lottery ticket decisions based on real-time scratch-off game data.

## 🌟 Features

- Ask natural language questions like:
  - “What are the best $10 scratch-offs with prizes left?”
  - “Show me games under $20 with good odds”
- Real-time odds analysis with Claude via Amazon Bedrock
- FastAPI backend with custom agents and filters
- React + Tailwind frontend hosted on Vercel
- Deployed backend on Render with environment-secured Claude access

---

## 🧠 How It Works

1. The frontend sends the user’s natural language question to the backend `/ask` endpoint.
2. A Claude-powered intent parser (via Amazon Bedrock) analyzes the question and classifies it (e.g. "best overall odds" or "best top prizes").
3. Based on the identified intent, the orchestrator agent decides which internal API method to invoke:
   - `get_best_overall_game_odds()` for overall odds
   - `get_best_prize_odds_filtered()` for top prize and range-based filtering
4. The selected method returns filtered scratch-off game data using a cached JSON dataset (refreshed by a scraper pipeline).
5. Claude is then called again to summarize the filtered data into a natural-language response tailored to the original question.
6. The response is returned to the frontend and displayed inside the chatbox interface.

This design allows a single AI agent to interpret the user's goal and dynamically route control through multiple backend operations — an orchestrator pattern that bridges LLM reasoning with structured logic and real-world data.

---

## 🛠️ Technologies Used

| Layer       | Tech                     |
|-------------|--------------------------|
| Frontend    | React, Vite, Tailwind    |
| Backend     | FastAPI, Python 3        |
| AI Agent    | Claude (via Bedrock SDK) |
| Hosting     | Vercel (frontend), Render (API) |
| Infra       | AWS Bedrock, Boto3, dotenv

---

## 🧪 Developer Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/alejotsv/scratch-off_agent.git
   cd scratch-off_agent
   ```

2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Create a `.env` file:
   ```
   AWS_ACCESS_KEY_ID=...
   AWS_SECRET_ACCESS_KEY=...
   AWS_DEFAULT_REGION=us-east-1
   UI_URL=http://localhost:5173
   ```

4. Run FastAPI locally:
   ```bash
   uvicorn backend.api.app:app --reload
   ```

5. Setup frontend:
   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

---

## 🤖 AI & Bedrock Focus

Scratchy follows an **orchestrated AI agent pattern**, using Claude via Amazon Bedrock to interpret user intent and dynamically direct internal logic.

Rather than functioning as a single prompt-based response generator, the AI acts as an **interpreter and controller**:
- It first analyzes the user's question and extracts structured intent
- Then chooses the relevant logic path or API method
- Finally, it summarizes structured results into conversational responses

This enables the backend to behave like an intelligent router — blending LLM flexibility with deterministic filtering and decision rules.

---

## 📄 License

MIT — for educational and personal use.
