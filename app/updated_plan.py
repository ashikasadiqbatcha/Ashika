import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def update_workout_plan(original_plan, feedback):
    prompt = f"Original Plan: {original_plan}\n\nUser Feedback: {feedback}\n\nUpdate the 7-day workout plan based on feedback. Keep structured."
    try:
        response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"