import certifi
import httpx
from openai import OpenAI
import json

client = OpenAI(
    http_client=httpx.Client(verify=certifi.where(), trust_env=True)
)

def analyze_text(text: str):
    prompt = f"""
    Analyze the user query and return JSON:

    {{
        "sentiment": "positive | negative | neutral",
        "summary": "short summary",
        "category": "billing | technical | general",
        "priority": "low | medium | high"
    }}

    Rules:
    - Frustration → high priority
    - Crashes/errors → technical
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text + "\n" + prompt}],
    )

    output = response.choices[0].message.content

    try:
        return json.loads(output)
    except:
        return {
            "sentiment": "unknown",
            "summary": output,
            "category": "general",
            "priority": "low"
        }


def generate_response(text: str, sentiment: str):
    prompt = f"""
    You are a professional support assistant.

    Generate a helpful reply.

    Sentiment: {sentiment}
    Query: {text}

    Keep it short and polite.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
