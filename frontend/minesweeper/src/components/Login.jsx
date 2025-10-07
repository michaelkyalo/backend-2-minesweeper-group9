import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../utils/auth";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    try {
      const data = await login({ username, password });

      // backend should return { access_token: "...", user: {...} } or similar
      if (data?.access_token) {
        localStorage.setItem("mws_token", data.access_token);
        // optionally save user info
        localStorage.setItem("mws_user", JSON.stringify(data.user || {}));
        navigate("/game");
      } else {
        setError(data?.message || "Login failed");
      }
    } catch (err) {
      setError(err.message || "Network or server error");
    }
  }

  return (
    <div style={{ maxWidth: 420, margin: "40px auto" }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: 8 }}>
          <label>
            Username
            <input
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              autoFocus
            />
          </label>
        </div>
        <div style={{ marginBottom: 8 }}>
          <label>
            Password
            <input
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              type="password"
            />
          </label>
        </div>

        {error && <div style={{ color: "red", marginBottom: 8 }}>{error}</div>}

        <button type="submit">Log in</button>
      </form>
    </div>
  );
}

export default Login;
