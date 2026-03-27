# Fitness Tracker MVP - Documentación Técnica 🦖

## 1. Visión General
Plataforma para gestionar progresiones de entrenamiento basadas en un modelo de **Niveles de Carga**. En lugar de gestionar kilos directamente, el usuario progresa a través de niveles predefinidos (Base + Step * Nivel).

## 2. Arquitectura (Single-Port Mono-App)
Para optimizar recursos y evitar limitaciones de túneles (ngrok free), el proyecto corre consolidado:
- **Backend:** FastAPI (Python 3.12) en puerto 8000.
- **Frontend:** React + Vite + TypeScript (Compilado en `dist/`).
- **Base de Datos:** PostgreSQL local.

## 3. Estado Actual (MVP v0.1)
### ✅ Implementado:
- **Infraestructura:** Repositorio GitHub, Túnel ngrok, DB Postgres configurada.
- **Esquema DB:**
    - `progression_profile`: Define estrategias de evaluación (ej: "last_working_set").
    - `inactivity_profile`: Define de-entrenamiento por días.
    - `user_exercise`: Configuración de cada ejercicio (Peso base, incremento por nivel, nivel actual).
    - `exercise_set`: Registro histórico de series (reps, peso, nivel).
- **API Endpoints:**
    - `GET /api/exercises`: Lista ejercicios con cálculo dinámico de peso sugerido.
    - `POST /api/sets`: Guarda registros de entrenamiento.
- **UI:** Interfaz oscura, lista de ejercicios y formulario de "Registro Rápido".

### 🛠️ En curso / Pendiente:
- **Lógica de Progresión:** El backend debe analizar la serie guardada y actualizar `current_level` automáticamente (Ej: >12 reps = +1 nivel).
- **Historial Visual:** Ver las últimas series registradas en el frontend.
- **Autenticación:** Actualmente es multi-usuario pero usa IDs de prueba (0000...).

## 4. Próximos Pasos (Action List)
1. **[Back]** Implementar `update_exercise_level()`: Lógica para subir/bajar niveles tras cada `POST /api/sets`.
2. **[Front]** Mostrar el historial de las últimas 5 series debajo de cada ejercicio.
3. **[Back]** Añadir logs de auditoría para ver cuándo y por qué cambió un nivel.

---
*Documentación generada por Intigirto (Codex Mode) - 2026-03-27*
