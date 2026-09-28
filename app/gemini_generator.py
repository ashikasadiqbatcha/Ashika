import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_workout_gemini(user_input):
    prompt = f"""Create a 7-day workout plan for:
    Age: {user_input.age}, Weight: {user_input.weight}kg, Goal: {user_input.goal}, Intensity: {user_input.intensity}
    Include warmup, exercises with sets/reps, cooldown. Engaging with emojis."""
    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"