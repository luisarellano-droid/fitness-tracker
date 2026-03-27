from uuid import UUID
from app.domain.repositories import IExerciseRepository, ISetRepository
from app.domain.models.exercise import ExerciseSet

class RegisterSetUseCase:
    def __init__(self, exercise_repo: IExerciseRepository, set_repo: ISetRepository):
        self.exercise_repo = exercise_repo
        self.set_repo = set_repo

    async def execute(self, user_exercise_id: UUID, reps: int, weight: float, level: int):
        # 1. Crear y registrar la serie (Infrastructure -> DB)
        new_set = ExerciseSet(
            user_exercise_id=user_exercise_id,
            reps=reps,
            weight=weight,
            level=level
        )
        self.set_repo.add(new_set)
        
        # 2. Lógica de Progresión (Domain logic inside Use Case for now)
        # TODO: Refactor into a Domain Service if logic grows
        if reps >= 12: # Umbral de éxito para subir nivel
            self.exercise_repo.update_level(user_exercise_id, level + 1)
        elif reps <= 6: # Umbral de de-entrenamiento o ajuste
            self.exercise_repo.update_level(user_exercise_id, max(1, level - 1))
            
        return {"status": "success", "new_level": level + 1 if reps >= 12 else level}
