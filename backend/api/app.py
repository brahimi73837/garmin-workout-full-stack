from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv
from .create_workout_service import create_workout_from_text

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Garmin AI Workout Creator")

# Allow cross-origin for local frontend dev (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WorkoutRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/create-workout")
def create_workout(req: WorkoutRequest):
    """
    Accepts plain text workout description and returns upload result.
    """
    try:
        result = create_workout_from_text(req.text)
        return {"status": "success", "result": result}
    except Exception as e:
        logger.exception("Failed to create workout")
        raise HTTPException(status_code=500, detail=str(e))
