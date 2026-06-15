import { Radar, RadarChart, PolarGrid, PolarAngleAxis, ResponsiveContainer, Tooltip } from "recharts";

export default function RadarChartView({ scores }) {
  const data = [
    { pillar: "Instagram",  score: scores.instagram_score,           max: 25 },
    { pillar: "Google Maps",score: scores.google_maps_score,         max: 25 },
    { pillar: "Website",    score: scores.website_score,             max: 20 },
    { pillar: "Brand",      score: scores.brand_consistency_score,   max: 15 },
    { pillar: "Engagement", score: scores.customer_engagement_score, max: 15 },
  ].map(d => ({ ...d, pct: Math.round((d.score / d.max) * 100) }));

  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h3 className="font-semibold text-gray-900 mb-4">Score breakdown</h3>
      <ResponsiveContainer width="100%" height={300}>
        <RadarChart data={data}>
          <PolarGrid stroke="#e5e7eb" />
          <PolarAngleAxis dataKey="pillar" tick={{ fontSize: 12, fill: "#374151" }} />
          <Radar name="Score %" dataKey="pct" stroke="#2563eb" fill="#3b82f6" fillOpacity={0.25} strokeWidth={2} />
          <Tooltip formatter={(val) => `${val}%`} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}