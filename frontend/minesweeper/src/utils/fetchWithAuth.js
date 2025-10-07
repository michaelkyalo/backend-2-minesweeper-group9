// src/utils/fetchWithAuth.js
const API_BASE = process.env.REACT_APP_API_BASE || "http://127.0.0.1:5000";

export default async function fetchWithAuth(path, opts = {}) {
  const token = localStorage.getItem("mws_token");
  const headers = {
    ...(opts.headers || {}),
    "Content-Type": "application/json",
  };
  if (token) headers["Authorization"] = `Bearer ${token}`;

  const res = await fetch(`${API_BASE}${path}`, {
    ...opts,
    headers,
  });

  // optionally handle 401 globally
  if (res.status === 401) {
    // token invalid/expired — clear and redirect (caller should handle navigation)
    localStorage.removeItem("mws_token");
  }

  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const message = data?.message || data?.error || `Request failed: ${res.status}`;
    const err = new Error(message);
    err.response = data;
    throw err;
  }
  return data;
}
