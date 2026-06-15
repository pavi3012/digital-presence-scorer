import RadarChartView from "./RadarChart";

const COLOR_MAP = { Excellent: "#16a34a", Good: "#ca8a04", Average: "#ea580c", Poor: "#dc2626" };
const PILLAR_LABELS = {
  instagram: "Instagram", google_maps: "Google Maps",
  website: "Website", brand_consistency: "Brand", customer_engagement: "Engagement"
};

export default function ScoreDashboard({ result, onReset }) {
  const color = COLOR_MAP[result.rating] || "#6b7280";

  const downloadReport = () => {
    window.open(`http://localhost:8000/api/report/1`, "_blank");
  };

  return (
    <div className="space-y-6">
      {/* Total score card */}
      <div className="rounded-xl p-8 text-white text-center" style={{ background: color }}>
        <p className="text-lg font-medium opacity-90">{result.business_name}</p>
        <p className="text-7xl font-bold mt-2">{result.total_score}</p>
        <p className="text-2xl mt-1 opacity-90">/ 100</p>
        <p className="mt-3 text-xl font-semibold">{result.rating}</p>
      </div>

      {/* Radar chart */}
      <RadarChartView scores={result} />

      {/* Recommendations */}
      <div className="space-y-4">
        {Object.entries(result.recommendations).map(([pillar, tips]) => (
          <div key={pillar} className="bg-white rounded-xl shadow p-5">
            <h3 className="font-semibold text-gray-900 mb-3">{PILLAR_LABELS[pillar]}</h3>
            <ul className="space-y-2">
              {tips.map((tip, i) => (
                <li key={i} className="flex gap-2 text-sm text-gray-700">
                  <span className="text-blue-500 mt-0.5">→</span>
                  <span>{tip}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className="flex gap-3">
        <button onClick={downloadReport}
                className="flex-1 bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded-xl transition">
          Download PDF report
        </button>
        <button onClick={onReset}
                className="flex-1 border border-gray-300 text-gray-700 font-semibold py-3 rounded-xl hover:bg-gray-50 transition">
          Score another business
        </button>
      </div>
    </div>
  );
}