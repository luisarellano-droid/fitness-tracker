from typing import List
from uuid import UUID
from app.domain.models.exercise import Exercise, ExerciseSet

class IExerciseRepository:
    def get_all_by_user(self, user_id: UUID) -> List[Exercise]:
        raise NotImplementedError
        
    def get_by_id(self, exercise_id: UUID) -> Exercise:
        raise NotImplementedError
        
    def update_level(self, exercise_id: UUID, new_level: int) -> None:
        raise NotImplementedError

class ISetRepository:
    def add(self, exercise_set: ExerciseSet) -> ExerciseSet:
        raise NotImplementedError
        
    def get_latest_by_exercise(self, exercise_id: UUID, limit: int = 5) -> List[ExerciseSet]:
        raise NotImplementedError
