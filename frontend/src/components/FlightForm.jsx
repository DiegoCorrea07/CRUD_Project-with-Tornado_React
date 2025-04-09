import React, { useState, useEffect } from "react";
import "./FlightForm.css";

const FlightForm = ({ onSubmit, flightToEdit, clearEdit }) => {
  const [formData, setFormData] = useState({
    airline: "",
    flight_number: "",
    origin: "",
    destination: "",
    departure_time: "",
    arrival_time: "",
  });

  const [error, setError] = useState(""); // Estado para manejar errores

  useEffect(() => {
    if (flightToEdit) {
      setFormData({
        airline: flightToEdit.airline || "",
        flight_number: flightToEdit.flight_number || "",
        origin: flightToEdit.origin || "",
        destination: flightToEdit.destination || "",
        departure_time: flightToEdit.departure_time ? flightToEdit.departure_time.slice(0, 16) : "",
        arrival_time: flightToEdit.arrival_time ? flightToEdit.arrival_time.slice(0, 16) : "",
      });
    } else {
      setFormData({
        airline: "",
        flight_number: "",
        origin: "",
        destination: "",
        departure_time: "",
        arrival_time: "",
      });
    }
  }, [flightToEdit]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(""); // Limpiar errores previos
    const result = await onSubmit(formData); // Llamar a la función onSubmit
    if (result && result.error) {
      setError(result.error); // Mostrar el error si existe
    } else {
      setFormData({
        airline: "",
        flight_number: "",
        origin: "",
        destination: "",
        departure_time: "",
        arrival_time: "",
      });
      if (clearEdit) clearEdit();
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flight-form">
      <h2>{flightToEdit ? "Editar Vuelo" : "Crear Vuelo"}</h2>
      {error && <p className="error">{error}</p>} {/* Mostrar mensaje de error */}
      <div className="form-group">
        <label htmlFor="airline">Aerolínea:</label>
        <input
          type="text"
          id="airline"
          name="airline"
          placeholder="Aerolínea"
          value={formData.airline}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="flight_number">Número de Vuelo:</label>
        <input
          type="text"
          id="flight_number"
          name="flight_number"
          placeholder="Número de Vuelo"
          value={formData.flight_number}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="origin">Origen:</label>
        <input
          type="text"
          id="origin"
          name="origin"
          placeholder="Origen"
          value={formData.origin}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="destination">Destino:</label>
        <input
          type="text"
          id="destination"
          name="destination"
          placeholder="Destino"
          value={formData.destination}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="arrival_time">Llegada:</label>
        <input
          type="datetime-local"
          id="arrival_time"
          name="arrival_time"
          value={formData.arrival_time}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="departure_time">Salida:</label>
        <input
          type="datetime-local"
          id="departure_time"
          name="departure_time"
          value={formData.departure_time}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-actions">
        <button type="button" onClick={clearEdit} className="cancel-button">
          Cancelar
        </button>
        <button type="submit" className="submit-button">
          {flightToEdit ? "Actualizar" : "Crear"}
        </button>
      </div>
    </form>
  );
};

export default FlightForm;