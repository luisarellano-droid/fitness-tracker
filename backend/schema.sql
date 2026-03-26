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

-- Configuración del ejercicio
CREATE TABLE IF NOT EXISTS user_exercise (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid NOT NULL,
    custom_name text NOT NULL,
    progression_profile_id uuid REFERENCES progression_profile(id),
    inactivity_profile_id uuid REFERENCES inactivity_profile(id),
    load_mode text NOT NULL DEFAULT 'fixed_step',
    base_weight_value numeric(8,2),
    step_value numeric(8,2),
    initial_level int NOT NULL DEFAULT 1
);
