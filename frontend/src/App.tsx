import { useState, useEffect } from 'react'
import './App.css'

interface Exercise {
  id: string;
  name: string;
  level: number;
  weight: number;
}

function App() {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [selectedEx, setSelectedEx] = useState<Exercise | null>(null);
  const [reps, setReps] = useState(10);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/exercises')
      .then(res => res.json())
      .then(data => {
        setExercises(data);
        setLoading(false);
      });
  }, []);

  const handleRegister = async () => {
    if (!selectedEx) return;
    const res = await fetch('/api/sets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_exercise_id: selectedEx.id,
        reps,
        weight: selectedEx.weight,
        level: selectedEx.level
      })
    });
    if (res.ok) {
      alert(`Serie guardada: ${selectedEx.weight}kg x ${reps}`);
      setSelectedEx(null);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>🦖 Fitness Tracker</h1>
        <p>Tu progreso real, nivel a nivel.</p>
      </header>

      <main>
        {selectedEx ? (
          <section className="form-card">
            <h2>Registrar: {selectedEx.name}</h2>
            <div className="stat">Nivel: {selectedEx.level} | Peso: <strong>{selectedEx.weight}kg</strong></div>
            <div className="input-group">
              <label>Repeticiones:</label>
              <input 
                type="number" 
                value={reps} 
                onChange={e => setReps(parseInt(e.target.value))} 
                min="1"
              />
            </div>
            <div className="actions">
              <button className="btn-save" onClick={handleRegister}>Guardar Serie</button>
              <button className="btn-cancel" onClick={() => setSelectedEx(null)}>Cancelar</button>
            </div>
          </section>
        ) : (
          <section className="exercise-list">
            <h2>Tus Ejercicios</h2>
            {loading ? <p>Cargando...</p> : (
              <ul className="list">
                {exercises.map(ex => (
                  <li key={ex.id} className="exercise-item">
                    <div className="info">
                      <span className="name">{ex.name}</span>
                      <span className="sub">Lvl {ex.level} • {ex.weight}kg</span>
                    </div>
                    <button onClick={() => setSelectedEx(ex)}>Registrar</button>
                  </li>
                ))}
              </ul>
            )}
          </section>
        )}
      </main>
    </div>
  )
}

export default App
