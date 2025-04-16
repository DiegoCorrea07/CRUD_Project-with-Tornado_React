import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './Login.css'; // Importa el archivo de estilos

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        try {
            const response = await fetch('http://localhost:8888/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok && data.status === 'success' && data.data.token) {
                localStorage.setItem('token', data.data.token);
                navigate('/flights');
            } else {
                setError(data.data?.message || 'Error al iniciar sesión. Credenciales inválidas.');
            }
        } catch (error) {
            setError('No se pudo conectar al servidor.');
            console.error('Error de login:', error);
        }
    };

    return (
        <div className="login-container">
            <div className="login-box">
                <h2 className="login-heading">Iniciar Sesión</h2>
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
                    <button type="submit" className="login-button">Iniciar Sesión</button>
                </form>
                <p className="register-text">¿No tienes una cuenta? <Link to="/register" className="register-link">Regístrate</Link></p>
            </div>
        </div>
    );
};

export default Login;