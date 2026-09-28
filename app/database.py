from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./fitbuddy.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Float)
    goal = Column(String)
    intensity = Column(String)
    schedule = Column(Integer, default=7)

class WorkoutPlan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    original_plan = Column(Text)
    updated_plan = Column(Text, nullable=True)

Base.metadata.create_all(bind=engine)

def save_user(user_id: int, name: str, age: int, weight: float, goal: str, intensity: str):
    db = SessionLocal()
    existing = db.query(User).filter_by(id=user_id).first()
    if existing:
        existing.name = name
        existing.age = age
        existing.weight = weight
        existing.goal = goal
        existing.intensity = intensity
    else:
        user = User(id=user_id, name=name, age=age, weight=weight, goal=goal, intensity=intensity, schedule=7)
        db.add(user)
    db.commit()
    db.close()

def save_plan(user_id: int, plan: str):
    db = SessionLocal()
    workout = WorkoutPlan(user_id=user_id, original_plan=plan)
    db.add(workout)
    db.commit()
    db.close()

def update_plan(user_id: int, updated_plan_text: str):
    db = SessionLocal()
    plan = db.query(WorkoutPlan).filter_by(user_id=user_id).order_by(WorkoutPlan.id.desc()).first()
    if plan:
        plan.updated_plan = updated_plan_text
        db.commit()
    db.close()

def get_original_plan(user_id: int):
    db = SessionLocal()
    plan = db.query(WorkoutPlan).filter_by(user_id=user_id).order_by(WorkoutPlan.id.desc()).first()
    db.close()
    return plan.original_plan if plan else None

def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter_by(id=user_id).first()
    db.close()
    return user

def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def get_all_plans():
    db = SessionLocal()
    plans = db.query(WorkoutPlan).all()
    db.close()
    return plans