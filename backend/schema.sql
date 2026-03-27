-- Perfil de progresión por repeticiones
CREATE TABLE IF NOT EXISTS progression_profile (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid NOT NULL, -- references app_user(id)
    name text NOT NULL,
    evaluation_strategy text NOT NULL DEFAULT 'last_working_set',
    description text,
    is_default boolean NOT NULL DEFAULT false,
    created_at timestamptz NOT NULL DEFAULT now()
);

-- Perfil de inactividad por días
CREATE TABLE IF NOT EXISTS inactivity_profile (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid NOT NULL, -- references app_user(id)
    name text NOT NULL,
    description text,
    is_default boolean NOT NULL DEFAULT false,
    created_at timestamptz NOT NULL DEFAULT now()
);

-- Tabla de series (logs)
CREATE TABLE IF NOT EXISTS exercise_set (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_exercise_id uuid NOT NULL REFERENCES user_exercise(id),
    reps int NOT NULL,
    weight numeric(8,2) NOT NULL,
    level int NOT NULL, -- El nivel en el que se realizó la serie
    is_working_set boolean NOT NULL DEFAULT true,
    created_at timestamptz NOT NULL DEFAULT now()
);

-- Actualizar user_exercise para guardar el nivel actual
ALTER TABLE user_exercise ADD COLUMN IF NOT EXISTS current_level int NOT NULL DEFAULT 1;
