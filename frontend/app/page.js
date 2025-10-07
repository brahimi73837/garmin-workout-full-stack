'use client'

import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("Example:\n10min Z3\n2 min rec\n15x250m at 10k pace 150m jog");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch("http://localhost:8000/create-workout", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || JSON.stringify(data));
      setResult(data);
    } catch (err) {
      setError(err.message || String(err));
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-gray-800 to-black text-gray-100 p-6">
      <div className="w-full max-w-2xl bg-gray-900/70 backdrop-blur-md rounded-2xl shadow-lg border border-gray-700 p-8">
        <h1 className="text-3xl font-bold mb-6 text-center text-white">
          🏋️ Create Garmin Workout
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <label className="block text-sm font-medium text-gray-300">
            Enter your workout text:
          </label>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={6}
            className="w-full p-3 rounded-lg bg-gray-800 text-gray-100 border border-gray-700 focus:border-blue-500 focus:ring-2 focus:ring-blue-600 font-mono text-sm outline-none"
          />

          <button
            type="submit"
            disabled={loading}
            className={`w-full py-3 mt-2 rounded-lg font-semibold transition-all ${
              loading
                ? "bg-blue-500/60 cursor-not-allowed"
                : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            {loading ? "Creating..." : "Create Workout"}
          </button>
        </form>

        {error && (
          <div className="mt-4 bg-red-900/40 border border-red-700 text-red-300 p-3 rounded-lg">
            <strong>Error:</strong> {error}
          </div>
        )}

        {result && (
          <div className="mt-6 bg-green-900/30 border border-green-700 p-4 rounded-lg">
            <h3 className="text-lg font-semibold mb-2 text-green-400">
              ✅ Workout Created!
            </h3>
            <pre className="bg-gray-800 text-gray-200 p-3 rounded-md text-sm overflow-x-auto">
              {JSON.stringify(result, null, 2)}
            </pre>

            {result.result?.workoutId && (
              <p className="mt-3">
                Workout ID:{" "}
                <span className="font-bold text-green-400">
                  {result.result.workoutId}
                </span>
                <br />
                View in{" "}
                <a
                  href="https://connect.garmin.com/modern/workouts"
                  target="_blank"
                  rel="noreferrer"
                  className="underline text-blue-400 hover:text-blue-300"
                >
                  Garmin Connect
                </a>
              </p>
            )}
          </div>
        )}
      </div>
    </main>
  );
}
