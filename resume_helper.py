import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_resume_feedback(resume_text):
    prompt = f"Review the following resume and suggest 5 improvements focused on grammar, clarity, and formatting:\n\n{resume_text}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    feedback = response.choices[0].message.content.strip()
    return feedback
