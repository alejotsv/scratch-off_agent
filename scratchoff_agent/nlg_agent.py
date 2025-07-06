import boto3
import json

BEDROCK_REGION = "us-east-1"
CLAUDE_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

bedrock = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)

def summarize_recommendation(ticket_data: list, user_goal: str) -> str:
    prompt = build_claude_prompt(ticket_data, user_goal)

    response = bedrock.invoke_model(
        modelId=CLAUDE_MODEL_ID,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 500,
            "temperature": 0.7,
            "top_k": 250,
            "top_p": 1.0,
            "stop_sequences": []
        }),
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response["body"].read())
    return response_body["content"][0]["text"]

def build_claude_prompt(ticket_data: list, user_goal: str) -> str:
    return f"""
You are a scratch-off lottery assistant. Based only on the following ticket data (in JSON), analyze and recommend the best option based on this user goal: "{user_goal}".

Consider:
- Odds (lower is better)
- Prize amount
- Remaining prizes
- Percent of total prizes still available
- Ticket price (value for money)

Explain your recommendation clearly and only use the data provided. If there are close contenders, mention them.

TICKET DATA:
{json.dumps(ticket_data, indent=2)}
"""
