const API_URL = "http://localhost:8888/flights";

export const getFlights = async () => {
  const response = await fetch(API_URL);
  return await response.json();
};

export const getFlightById = async (id) => {
  const response = await fetch(`${API_URL}/${id}`);
  return await response.json();
};

export const createFlight = async (flight) => {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(flight),
  });
  return await response.json();
};

export const updateFlight = async (id, flight) => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(flight),
  });
  return await response.json();
};

export const deleteFlight = async (id) => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: "DELETE",
  });
  return await response.json();
};
