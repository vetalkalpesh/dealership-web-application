import React, { useState } from "react";

export default function Register() {
  const [form, setForm] = useState({ username: "", first_name: "", last_name: "", email: "", password: "" });
  const [message, setMessage] = useState("");
  const update = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  async function submit(e) {
    e.preventDefault();
    setMessage("Submitting...");
    try {
      const response = await fetch("http://127.0.0.1:8000/accounts/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      const data = await response.json();
      setMessage(data.message || data.error || "Request failed");
    } catch {
      setMessage("Could not reach the Django API. Check that the server is running.");
    }
  }

  return (
    <main className="register-page">
      <form className="register-card" onSubmit={submit}>
        <h1>Sign-up</h1>
        <label>Username<input name="username" value={form.username} onChange={update} required /></label>
        <label>First Name<input name="first_name" value={form.first_name} onChange={update} required /></label>
        <label>Last Name<input name="last_name" value={form.last_name} onChange={update} required /></label>
        <label>Email<input name="email" type="email" value={form.email} onChange={update} required /></label>
        <label>Password<input name="password" type="password" value={form.password} onChange={update} required /></label>
        <button type="submit">Register</button>
        <p role="status">{message}</p>
      </form>
    </main>
  );
}
