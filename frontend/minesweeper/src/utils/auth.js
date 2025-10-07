// src/utils/auth.js
const API_BASE = process.env.REACT_APP_API_BASE || "http://127.0.0.1:5000";

export async function login({ username, password }) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await res.json();
  if (!res.ok) {
    // throw an error with message from backend or generic message
    const message = data?.message || data?.error || "Login failed";
    const err = new Error(message);
    err.response = data;
    throw err;
  }
  return data;
}
