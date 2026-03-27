from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional

class Exercise(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    custom_name: str
    current_level: int
    base_weight: float
    step_value: float
    
    def calculate_suggested_weight(self) -> float:
        return self.base_weight + (self.current_level - 1) * self.step_value

class ExerciseSet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[UUID] = None
    user_exercise_id: UUID
    reps: int
    weight: float
    level: int
    created_at: Optional[datetime] = None
