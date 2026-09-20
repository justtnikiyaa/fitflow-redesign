from pydantic import BaseModel
from typing import List, Optional

class FoodItem(BaseModel):
    name: str = ""
    confidence: float
    estimated_calories: int
    protein_g: float
    carbs_g: float
    fat_g: float

class NutritionAnalysisResponse(BaseModel):
    meal_name: str
    total_calories: int
    items: List[FoodItem]

class WorkoutPlanRequest(BaseModel):
    user_id: str
    fitness_level: str
    target_muscle_groups: List[str]
    time_available_mins: int
    fatigue_level: int  # 1 (fresh) to 5 (exhausted)

class WorkoutPlanResponse(BaseModel):
    plan_name: str
    duration_mins: int
    difficulty: str
    exercises: List[str]
    adaptive_notes: str
