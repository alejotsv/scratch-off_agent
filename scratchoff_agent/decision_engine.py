import json

from scratchoff_agent.nlg_agent import bedrock, CLAUDE_MODEL_ID


def parse_user_goal_with_claude(question: str) -> dict:
    prompt = f"""
You are an intent classifier for a lottery scratch-off assistant.

Extract the user goal from this question: "{question}".

Return a JSON with the following fields:
- intent: either "best_overall", "best_prize_odds"
- min_prize: (optional) float
- max_prize: (optional) float
- top_prize_only: (optional) true/false
- ticket_price_ceiling: (optional) float

Respond with only the JSON object, no explanation.
"""

    response = bedrock.invoke_model(
        modelId=CLAUDE_MODEL_ID,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 300,
            "temperature": 0,
        }),
        contentType="application/json",
        accept="application/json"
    )

    body = json.loads(response["body"].read())
    json_text = body["content"][0]["text"]

    try:
        parsed = json.loads(json_text)
        return parsed
    except:
        return {"intent": "unsupported"}