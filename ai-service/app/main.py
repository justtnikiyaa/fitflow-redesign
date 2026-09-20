from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import nutrition, workouts

app = FastAPI(
    title="FitFlow AI & Vision Microservice",
    description="Computer Vision food recognition and AI-powered adaptive workout engine for FitFlow",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nutrition.router)
app.include_router(workouts.router)

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "FitFlow AI Microservice"}
