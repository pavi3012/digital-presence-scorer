import { useState } from "react";
import { scoreBusinesss } from "../api";

const defaultForm = {
  name: "", category: "Restaurant", city: "Madurai",
  instagram_handle: "", instagram_followers: 0,
  instagram_posts_per_week: 0, instagram_engagement_rate: 0,
  instagram_bio_complete: false,
  google_maps_listed: false, google_maps_rating: 0,
  google_maps_reviews: 0, google_maps_photos: 0,
  google_maps_hours_set: false,
  has_website: false, website_mobile_friendly: false,
  website_load_fast: false, website_contact_visible: false,
  same_name_across_platforms: false,
  same_logo_across_platforms: false, consistent_colors: false,
  replies_to_reviews: false, whatsapp_business_active: false,
  average_response_time_hours: 48,
};

export default function BusinessForm({ onResult }) {
  const [form, setForm] = useState(defaultForm);
  const [loading, setLoading] = useState(false);

  const set = (key, val) => setForm(f => ({ ...f, [key]: val }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const result = await scoreBusinesss(form);
      onResult(result);
    } catch (err) {
      alert("Error scoring business. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const Field = ({ label, name, type = "text", ...rest }) => (
    <div className="mb-3">
      <label className="block text-sm font-medium text-gray-700 mb-1">{label}</label>
      <input
        type={type}
        value={form[name]}
        onChange={e => set(name, type === "number" ? Number(e.target.value) : e.target.value)}
        className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        {...rest}
      />
    </div>
  );

  const Check = ({ label, name }) => (
    <label className="flex items-center gap-2 text-sm text-gray-700 mb-2 cursor-pointer">
      <input type="checkbox" checked={form[name]} onChange={e => set(name, e.target.checked)}
             className="w-4 h-4 accent-blue-600" />
      {label}
    </label>
  );

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-gray-900 mb-4">Business details</h2>
        <Field label="Business name *" name="name" required />
        <div className="mb-3">
          <label className="block text-sm font-medium text-gray-700 mb-1">Category</label>
          <select value={form.category} onChange={e => set("category", e.target.value)}
                  className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm">
            {["Restaurant","Salon","Retail","Tutor","Mechanic","Home Cook","Other"].map(c =>
              <option key={c}>{c}</option>)}
          </select>
        </div>
        <Field label="City" name="city" />
      </div>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-gray-900 mb-4">Instagram (25 pts)</h2>
        <Field label="Instagram handle" name="instagram_handle" />
        <Field label="Followers" name="instagram_followers" type="number" min="0" />
        <Field label="Posts per week" name="instagram_posts_per_week" type="number" min="0" step="0.5" />
        <Field label="Engagement rate (%)" name="instagram_engagement_rate" type="number" min="0" step="0.1" />
        <Check label="Bio is complete (link, phone, location, CTA)" name="instagram_bio_complete" />
      </div>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-gray-900 mb-4">Google Maps (25 pts)</h2>
        <Check label="Listed on Google Maps" name="google_maps_listed" />
        <Check label="Business hours are set" name="google_maps_hours_set" />
        <Field label="Star rating (0–5)" name="google_maps_rating" type="number" min="0" max="5" step="0.1" />
        <Field label="Number of reviews" name="google_maps_reviews" type="number" min="0" />
        <Field label="Photos uploaded" name="google_maps_photos" type="number" min="0" />
      </div>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-gray-900 mb-4">Website (20 pts)</h2>
        <Check label="Has a website" name="has_website" />
        <Check label="Mobile-friendly" name="website_mobile_friendly" />
        <Check label="Loads in under 3 seconds" name="website_load_fast" />
        <Check label="Contact info visible on homepage" name="website_contact_visible" />
      </div>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-gray-900 mb-4">Brand consistency (15 pts)</h2>
        <Check label="Same business name across all platforms" name="same_name_across_platforms" />
        <Check label="Same logo across all platforms" name="same_logo_across_platforms" />
        <Check label="Consistent brand colors" name="consistent_colors" />
      </div>

      <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-gray-900 mb-4">Customer engagement (15 pts)</h2>
        <Check label="Replies to Google reviews" name="replies_to_reviews" />
        <Check label="WhatsApp Business account active" name="whatsapp_business_active" />
        <Field label="Avg. response time (hours)" name="average_response_time_hours" type="number" min="0" />
      </div>

      <button type="submit" disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl text-base transition disabled:opacity-60">
        {loading ? "Scoring…" : "Generate score →"}
      </button>
    </form>
  );
}