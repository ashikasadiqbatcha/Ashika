import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_nutrition_tip_with_flash(goal):
    prompt = f"Give a short, practical nutrition tip (2-3 lines) for someone whose fitness goal is {goal}. Include foods to eat."
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating tip: {e}"