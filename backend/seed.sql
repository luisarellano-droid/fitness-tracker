-- Insertar Perfil de Progresión (Default)
INSERT INTO progression_profile (user_id, name, evaluation_strategy, description, is_default)
VALUES ('00000000-0000-0000-0000-000000000000', 'Standard Hypertrophy', 'last_working_set', 'Progresión basada en la última serie efectiva.', true);

-- Insertar Perfil de Inactividad (Default)
INSERT INTO inactivity_profile (user_id, name, description, is_default)
VALUES ('00000000-0000-0000-0000-000000000000', 'Standard Deconditioning', 'Pérdida de nivel progresiva tras 7 días de inactividad.', true);

-- Insertar algunos ejercicios de prueba
INSERT INTO user_exercise (user_id, custom_name, progression_profile_id, inactivity_profile_id, load_mode, base_weight_value, step_value, initial_level)
SELECT 
    '00000000-0000-0000-0000-000000000000', 
    'Press de Banca', 
    p.id, 
    i.id, 
    'fixed_step', 
    20.0, 
    2.5, 
    1
FROM progression_profile p, inactivity_profile i
WHERE p.is_default = true AND i.is_default = true
LIMIT 1;

INSERT INTO user_exercise (user_id, custom_name, progression_profile_id, inactivity_profile_id, load_mode, base_weight_value, step_value, initial_level)
SELECT 
    '00000000-0000-0000-0000-000000000000', 
    'Sentadilla libre', 
    p.id, 
    i.id, 
    'fixed_step', 
    40.0, 
    5.0, 
    1
FROM progression_profile p, inactivity_profile i
WHERE p.is_default = true AND i.is_default = true
LIMIT 1;
