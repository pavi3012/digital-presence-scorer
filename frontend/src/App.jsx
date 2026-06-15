import { useState } from "react";
import BusinessForm from "./components/BusinessForm";
import ScoreDashboard from "./components/ScoreDashboard";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200 px-6 py-4">
        <div className="max-w-2xl mx-auto">
          <h1 className="text-xl font-bold text-gray-900">Digital Presence Scorer</h1>
          <p className="text-sm text-gray-500">Analyze · Score · Grow — Pavi Creations</p>
        </div>
      </header>
      <main className="max-w-2xl mx-auto px-4 py-8">
        {result
          ? <ScoreDashboard result={result} onReset={() => setResult(null)} />
          : <BusinessForm onResult={setResult} />
        }
      </main>
    </div>
  );
}