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
You are a friendly and helpful scratch-off lottery assistant.

Your job is to recommend the best scratch-off tickets for the user based on their goal: "{user_goal}"

Here’s how you should respond:
- Start naturally with something like "I can help with that!" or "Here's what I found for you."
- Sound friendly and human, not like you're summarizing a report.
- Use bullet points or short sections to present details clearly.
- If multiple good options exist, mention your top pick, then briefly list others.
- Avoid repeating the phrase “based on the data.”

ONLY use the ticket data provided below. Don’t make up information. If the user asks something that the data can’t answer, say so politely.

DO NOT invite the user to ask more questions or continue the conversation. Just end with a confident recommendation.

Here is the ticket data (in JSON format):
{json.dumps(ticket_data, indent=2)}
"""
