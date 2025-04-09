import React, { useEffect, useState } from "react";
import FlightForm from "./components/FlightForm";
import FlightList from "./components/FlightList";
import { FaPlus} from 'react-icons/fa';
import "./App.css";

const API_URL = "http://localhost:8888/flights";

function App() {
  const [flights, setFlights] = useState([]);
  const [editingFlight, setEditingFlight] = useState(null);
  const [showForm, setShowForm] = useState(false);

  const fetchFlights = async () => {
    const res = await fetch(API_URL);
    const data = await res.json();
    if (data.status === "success") setFlights(data.data);
  };

  const createFlight = async (flight) => {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(flight),
    });
    if (res.ok) {
      fetchFlights();
      setShowForm(false); // Cierra el formulario después de la creación
    }
  };

  const updateFlight = async (flight) => {
    const res = await fetch(`${API_URL}/${editingFlight.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(flight),
    });
    if (res.ok) {
      setEditingFlight(null);
      fetchFlights();
      setShowForm(false); // Cierra el formulario después de la edición
    }
  };

  const deleteFlight = async (id) => {
    if (window.confirm("¿Estás seguro de que deseas eliminar este vuelo?")) {
      const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      if (res.ok) fetchFlights();
    }
  };

  const handleEdit = (flight) => {
    setEditingFlight(flight);
    setShowForm(true); // Abre el formulario en modo edición
  };

  const handleAddFlightClick = () => {
    setEditingFlight(null); // Resetea el vuelo en edición
    setShowForm(true); // Abre el formulario en modo creación
  };

  const handleFormClose = () => {
    setShowForm(false);
    setEditingFlight(null);
  };

  useEffect(() => {
    fetchFlights();
  }, []);

  return (
      <div className="app-container">
        <h1>Gestión de Vuelos</h1>
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
              onDelete={deleteFlight}
              onEdit={handleEdit}
          />
        </div>
        );
        }

        export default App;