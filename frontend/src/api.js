const BASE = "http://localhost:8000/api";

export async function scoreBusinesss(formData) {
  const res = await fetch(`${BASE}/score`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  });
  if (!res.ok) throw new Error("Scoring failed");
  return res.json();
}