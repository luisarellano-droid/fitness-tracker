# Documentación de Arquitectura Híbrida 🦖

## Backend (DDD + Hexagonal)
- **app/domain**: Entidades (`Exercise`, `Set`) y Contratos (`IExerciseRepository`). Independiente de frameworks.
- **app/application**: Casos de Uso (`RegisterSetUseCase`). Orquesta el flujo de negocio sin conocer detalles de DB.
- **app/infrastructure**: Implementación técnica (SQLAlchemy, PostgreSQL, repositorios concretos).
- **app/api**: Puertos de entrada (FastAPI Routes).

## Frontend (Scream Architecture)
- **src/features/**: Carpetas que "gritan" de qué trata el negocio.
  - `exercises/`: Componentes y lógica para ver y gestionar ejercicios.
  - `sets/`: Todo lo referente al registro de series (formulario, lógica de envío).
- **src/shared/**: Componentes genéricos (Botones, inputs, hooks globales).
- **src/main.tsx**: Entrada principal del sistema.

---
*Diseño: Codex Flash Mode (Architecting MVP v0.2)*
