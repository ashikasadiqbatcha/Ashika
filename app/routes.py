from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.schemas import UserInput
from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash
from app.updated_plan import update_workout_plan
from app.database import save_user, save_plan, update_plan, get_original_plan, get_user, get_all_users, get_all_plans

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.post("/generate-workout")
def generate_workout(request: Request, username: str = Form(...), user_id: int = Form(...), age: int = Form(...), weight: float = Form(...), goal: str = Form(...), intensity: str = Form(...)):
    user_input = UserInput(user_id=user_id, name=username, age=age, weight=weight, goal=goal, intensity=intensity)
    workout_plan = generate_workout_gemini(user_input)
    nutrition_tip = generate_nutrition_tip_with_flash(goal)
    save_user(user_id, username, age, weight, goal, intensity)
    save_plan(user_id, workout_plan)
    return templates.TemplateResponse(request, "result.html", {
        "username": username, "user_id": user_id, "age": age, "weight": weight, "goal": goal, "intensity": intensity,
        "workout_plan": workout_plan, "nutrition_tip": nutrition_tip
    })

@router.post("/submit-feedback")
def submit_feedback(request: Request, user_id: int = Form(...), feedback: str = Form(...)):
    original_plan = get_original_plan(user_id)
    user = get_user(user_id)
    updated = update_workout_plan(original_plan, feedback)
    update_plan(user_id, updated)
    nutrition_tip = generate_nutrition_tip_with_flash(user.goal if user else "general fitness")
    return templates.TemplateResponse(request, "result.html", {
        "username": user.name if user else "User", "user_id": user_id, "goal": user.goal if user else "", "intensity": user.intensity if user else "",
        "workout_plan": updated, "nutrition_tip": nutrition_tip, "message": "Plan updated successfully!"
    })

@router.get("/view-all-users")
def view_all_users(request: Request):
    users = get_all_users()
    plans = get_all_plans()
    return templates.TemplateResponse(request, "all_users.html", {"users": users, "plans": plans})