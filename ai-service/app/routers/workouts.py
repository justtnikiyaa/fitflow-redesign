from fastapi import APIRouter
from app.models.schemas import WorkoutPlanRequest, WorkoutPlanResponse

router = APIRouter(prefix="/v1/workouts", tags=["AI Workout Generator"])

@router.post("/generate", response_model=WorkoutPlanResponse)
async def generate_workout_plan(req: WorkoutPlanRequest):
    """
    Generate an AI-driven personalized and adaptive workout plan based on user fatigue and goals.
    """
    if req.fatigue_level >= 4:
        return WorkoutPlanResponse(
            plan_name="Active Recovery & Mobility Flow",
            duration_mins=min(req.time_available_mins, 25),
            difficulty="Light",
            exercises=[
                "Thoracic Spine Openers (3 mins)",
                "Cat-Cow & Child's Pose Flow (4 mins)",
                "Pigeon Stretch (5 mins)",
                "Diaphragmatic Breathing & Core Stabilizers (8 mins)"
            ],
            adaptive_notes="High fatigue detected. Adjusted routine to active recovery to prevent overtraining."
        )

    return WorkoutPlanResponse(
        plan_name=f"Adaptive Hypertrophy & Cardio ({', '.join(req.target_muscle_groups)})",
        duration_mins=req.time_available_mins,
        difficulty=req.fitness_level.capitalize(),
        exercises=[
            "Dynamic Joint Mobilization (5 mins)",
            "Goblet Squats: 3 sets x 12 reps",
            "Dumbbell Romanian Deadlifts: 3 sets x 10 reps",
            "Push-Ups / Incline Press: 3 sets x 12 reps",
            "HIIT Finisher: 30s Mountain Climbers / 30s rest x 5 rounds"
        ],
        adaptive_notes="Optimized volume and rest intervals for balanced progressive overload."
    )
