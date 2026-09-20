# classifier.py

from groq import Groq
import json

client = Groq(api_key="...")

def classify_business(data):

    prompt = f"""
    Classify this website.

    Title: {data['title']}

    Description:
    {data['description']}

    Content:
    {data['content'][:2000]}

    Return JSON only.

    {{
      "classification": "",
      "industry": "",
      "confidence": 0.0
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(
        response.choices[0].message.content
    )
