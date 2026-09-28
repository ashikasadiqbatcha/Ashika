from pydantic import BaseModel

class UserInput(BaseModel):
    user_id: int
    name: str
    age: int
    weight: float
    goal: str
    intensity: str

class FeedbackRequest(BaseModel):
    user_id: int
    feedback: str