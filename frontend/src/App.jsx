import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import FlightForm from "./components/FlightForm";
import FlightList from "./components/FlightList";
import Login from "./components/Auth/Login";
import Register from "./components/Auth/Register";
import { FaPlus } from 'react-icons/fa';
import { jwtDecode } from 'jwt-decode';
import "./App.css";

const API_URL = "http://localhost:8888/api/flights";

// Componente para proteger rutas
const PrivateRoute = ({ children }) => {
    const token = localStorage.getItem('token');
    return token ? children : <Navigate to="/login" />;
};

const AuthCheck = ({ children }) => {
    const token = localStorage.getItem('token');
    return token ? <Navigate to="/flights" /> : children;
};

function AppContent() {
    const [flights, setFlights] = useState([]);
    const [editingFlight, setEditingFlight] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const navigate = useNavigate();
    const [isAdmin, setIsAdmin] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
            try {
                const decodedToken = jwtDecode(token);
                setIsAdmin(decodedToken?.role === 'admin');
            } catch (error) {
                console.error("Error decoding token:", error);
                setIsAdmin(false);
            }
        } else {
            setIsAdmin(false);
        }
    }, []);

    const fetchFlights = async () => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }
        try {
            const res = await fetch(API_URL, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });
            if (!res.ok) {
                if (res.status === 401) {
                    localStorage.removeItem('token');
                    navigate('/login');
                    return;
                }
                console.error("Error fetching flights:", await res.json());
                return;
            }
            const data = await res.json();
            if (data.status === "success") setFlights(data.data);
        } catch (error) {
            console.error("Error fetching flights:", error);
        }
    };

    const createFlight = async (flight) => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }
        const res = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Bearer ${token}`,
            },
            body: JSON.stringify(flight),
        });
        if (res.ok) {
            fetchFlights();
            setShowForm(false);
        }
    };

   const updateFlight = async (flight) => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }
        try {
            const res = await fetch(`${API_URL}/${editingFlight.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    'Authorization': `Bearer ${token}`,
                },
                body: JSON.stringify(flight),
            });

            if (!res.ok) {
                if (res.status === 403) {
                    alert("No tiene permisos de administrador para actualizar este vuelo.");
                    return;
                } else {
                    console.error("Error al actualizar el vuelo:", await res.json());

                    return;
                }
            }

            if (res.ok) {
                setEditingFlight(null);
                fetchFlights();
                setShowForm(false);
            }
        } catch (error) {
            console.error("Error al comunicarse con el servidor:", error);
            // Manejar errores de conexión
        }
   };

    const deleteFlight = async (id) => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login');
            return;
        }
        if (window.confirm("¿Estás seguro de que deseas eliminar este vuelo?")) {
            try {
                const res = await fetch(`${API_URL}/${id}`, {
                    method: "DELETE",
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                });

                if (!res.ok) {
                    if (res.status === 403) {

                        alert("No tiene permisos de administrador para eliminar este vuelo.");
                        return;
                    } else {
                        console.error("Error al eliminar el vuelo:", await res.json());
                        return;
                    }
                }

                if (res.ok) fetchFlights();

            } catch (error) {
                console.error("Error al comunicarse con el servidor:", error);
            }
        }
    };

    const handleEdit = (flight) => {
        setEditingFlight(flight);
        setShowForm(true);
    };

    const handleAddFlightClick = () => {
        setEditingFlight(null);
        setShowForm(true);
    };

    const handleFormClose = () => {
        setShowForm(false);
        setEditingFlight(null);
    };

    const handleLogout = () => {
        localStorage.removeItem('token');
        navigate('/login');
    };

    useEffect(() => {
        fetchFlights();
    }, []); // Dependencia vacía para que se ejecute solo al montar

    return (
        <div className="app-container">
            <div className="header"> {/* Añadimos un contenedor para el título y el botón */}
                <h1>Gestión de Vuelos</h1>
                <button onClick={handleLogout} className="logout-button">Cerrar Sesión</button>
            </div>
            <div className="add-container">
                <button onClick={handleAddFlightClick} className="add-flight-button">
                    <FaPlus/> Nuevo
                </button>
            </div>
            {showForm && (
                <div className="modal">
                    <div className="modal-content">
                        <FlightForm
                            onSubmit={editingFlight ? updateFlight : createFlight}
                            flightToEdit={editingFlight}
                            clearEdit={handleFormClose}
                        />
                    </div>
                </div>
            )}

            <FlightList
                flights={flights}
                onDelete={isAdmin ? deleteFlight : null} // Solo permitir eliminar si es admin
                onEdit={handleEdit}
                isAdmin={isAdmin}
            />
        </div>
    );
}

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<AuthCheck><Login /></AuthCheck>} />
                <Route path="/register" element={<AuthCheck><Register /></AuthCheck>} />
                <Route path="/flights/*" element={<PrivateRoute><AppContent /></PrivateRoute>} />
                <Route path="/" element={<Navigate to="/flights" />} /> {/* Redirigir la raíz a /flights si está logueado */}
            </Routes>
        </Router>
    );
}

export default App;