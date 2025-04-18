import { FaPen, FaTrash } from 'react-icons/fa';

const FlightList = ({ flights, onDelete, onEdit, isAdmin }) => {
  return (
    <div className="flight-list-container">
      <table className="flight-table">
        <thead>
          <tr>
            <th>Aerolínea</th>
            <th>Número</th>
            <th>Origen</th>
            <th>Destino</th>
            <th>Llegada</th>
            <th>Salida</th>
            <th className="actions-column">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {flights.map((flight) => (
            <tr key={flight.id}>
              <td>{flight.airline}</td>
              <td>{flight.flight_number}</td>
              <td>{flight.origin}</td>
              <td>{flight.destination}</td>
              <td>{new Date(flight.arrival_time).toLocaleString()}</td>
              <td>{new Date(flight.departure_time).toLocaleString()}</td>
              <td className="actions-column">
                <button onClick={() => onEdit(flight)} className="edit-button"><FaPen/> Editar</button>
                {isAdmin && (
                  <button onClick={() => onDelete(flight.id)} className="delete-button"><FaTrash/> Eliminar</button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FlightList;