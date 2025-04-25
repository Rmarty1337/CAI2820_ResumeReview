import openai
import os

# Use environment variable for API key
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

def get_resume_feedback(resume_text):
    prompt = f"Review the following resume and suggest 5 improvements focused on grammar, clarity, and formatting:\n\n{resume_text}"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    feedback = response.choices[0].message.content.strip()
    return feedback
