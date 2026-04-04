import certifi
import httpx
from openai import OpenAI
import json

# Force proper SSL verification using certifi
http_client = httpx.Client(verify=certifi.where())


client = OpenAI(
    http_client=httpx.Client(
        verify=certifi.where(),
        trust_env=True   # ← IMPORTANT
    )
)


def analyze_text(text: str):
    prompt = f"""
    Analyze the following user query and respond ONLY in JSON format:

    {{
        "sentiment": "positive | negative | neutral",
        "summary": "short one-line summary"
    }}

    Query: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # safer model
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    output = response.choices[0].message.content

    try:
        return json.loads(output)
    except:
        return {
            "sentiment": "unknown",
            "summary": output
        }
