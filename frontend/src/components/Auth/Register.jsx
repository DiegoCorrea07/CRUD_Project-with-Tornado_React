import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './Login.css'; // Importa el archivo de estilos (asumimos que usaremos el mismo)

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        try {
            const response = await fetch('http://localhost:8888/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok && data.status === 'success') {
                alert(data.data.message);
                navigate('/login'); // Redirigir al login después del registro exitoso
            } else {
                setError(data.data?.message || 'Error al registrar usuario.');
            }
        } catch (error) {
            setError('No se pudo conectar al servidor.');
            console.error('Error de registro:', error);
        }
    };

    return (
        <div className="login-container"> {/* Usamos el mismo contenedor para el fondo */}
            <div className="login-box"> {/* Usamos la misma caja para la disposición */}
                <h2 className="login-heading">Registro</h2>
                {error && <p className="login-error">{error}</p>}
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label htmlFor="username" className="input-label">Usuario:</label>
                        <input
                            type="text"
                            id="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                            className="input-field"
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="password" className="input-label">Contraseña:</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                            className="input-field"
                        />
                    </div>
                    <button type="submit" className="login-button">Registrar</button>
                </form>
                <p className="register-text">¿Ya tienes una cuenta? <Link to="/login" className="register-link">Inicia Sesión</Link></p>
            </div>
        </div>
    );
};

export default Register;