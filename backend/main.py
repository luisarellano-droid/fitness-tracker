from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import os

app = FastAPI(title="Fitness Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "postgresql://luis:fitness_pass@localhost:5432/fitness_tracker_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- MODELOS PYDANTIC ---
class SetCreate(BaseModel):
    user_exercise_id: str
    reps: int
    weight: float
    level: int

# --- API ENDPOINTS ---
@app.get("/api/exercises")
def get_exercises(db: Session = Depends(get_db)):
    query = text("""
        SELECT id, custom_name, current_level, base_weight_value, step_value 
        FROM user_exercise
    """)
    result = db.execute(query).fetchall()
    return [{
        "id": str(r[0]), 
        "name": r[1], 
        "level": r[2],
        "weight": float(r[3] + (r[2]-1)*r[4]) # Cálculo simple de carga actual
    } for r in result]

@app.post("/api/sets")
def create_set(data: SetCreate, db: Session = Depends(get_db)):
    query = text("""
        INSERT INTO exercise_set (user_exercise_id, reps, weight, level)
        VALUES (:ue_id, :reps, :weight, :level)
        RETURNING id
    """)
    result = db.execute(query, {
        "ue_id": data.user_exercise_id,
        "reps": data.reps,
        "weight": data.weight,
        "level": data.level
    })
    db.commit()
    return {"status": "success", "id": str(result.fetchone()[0])}

# --- STATIC FILES ---
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/dist")
if os.path.exists(frontend_path):
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_path, "assets")), name="assets")
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        if full_path.startswith("api/"): raise HTTPException(status_code=404)
        return FileResponse(os.path.join(frontend_path, "index.html"))
