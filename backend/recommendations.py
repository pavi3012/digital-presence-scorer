TIPS = {
    "instagram": {
        "low": [
            "Post at least 3 times per week — consistency beats perfection.",
            "Add your WhatsApp number, location, and a clear call-to-action to your Instagram bio.",
            "Use 5–10 local hashtags like #ChennaiFood or #MaduraiShops in every post.",
        ],
        "medium": [
            "Experiment with Instagram Reels — they get 3× more reach than regular posts.",
            "Run a 'Follow + Tag a Friend' contest to grow followers organically.",
            "Pin your best-performing post to the top of your profile.",
        ],
    },
    "google_maps": {
        "low": [
            "Claim your Google Business Profile at business.google.com — it's completely free.",
            "Upload at least 10 high-quality photos of your shop, products, and team.",
            "Fill in your business hours, phone number, and a short description.",
        ],
        "medium": [
            "Ask every satisfied customer to leave a Google review — even 5 more reviews boost ranking.",
            "Post weekly updates (offers, events) directly on your Google Business Profile.",
            "Add your WhatsApp number as a contact method on Google Maps.",
        ],
    },
    "website": {
        "low": [
            "Create a free website on Google Sites or Wix — takes under 2 hours.",
            "Make sure your phone number and address are visible on every page.",
            "Test your site on a mobile phone — over 80% of local searches happen on mobile.",
        ],
        "medium": [
            "Add an SSL certificate (https://) — Google penalises sites without it.",
            "Include a WhatsApp chat button so customers can contact you instantly.",
            "Add customer testimonials and photos to your homepage.",
        ],
    },
    "brand_consistency": {
        "low": [
            "Use the exact same business name on Google Maps, Instagram, and your website.",
            "Pick 2–3 brand colors and use them consistently across all platforms.",
            "Create a simple logo using Canva — free templates make this easy.",
        ],
        "medium": [
            "Create a brand kit in Canva with your logo, fonts, and colors for quick content creation.",
            "Audit all your profiles quarterly to ensure nothing has drifted.",
            "Use the same profile photo across all platforms for instant recognition.",
        ],
    },
    "customer_engagement": {
        "low": [
            "Reply to every Google review within 24 hours — even negative ones politely.",
            "Set up a WhatsApp Business account — it's free and shows you're responsive.",
            "Enable auto-reply on WhatsApp for after-hours messages.",
        ],
        "medium": [
            "Respond to Instagram comments within 6 hours to boost your content's reach.",
            "Ask customers to send voice notes or short videos as testimonials.",
            "Use WhatsApp broadcast lists to send weekly offers to existing customers.",
        ],
    },
}

THRESHOLDS = {
    "instagram":           {"max": 25, "low": 12},
    "google_maps":         {"max": 25, "low": 12},
    "website":             {"max": 20, "low": 10},
    "brand_consistency":   {"max": 15, "low": 8},
    "customer_engagement": {"max": 15, "low": 8},
}

def generate_recommendations(scores: dict) -> dict:
    result = {}
    pillars = {
        "instagram":           scores["instagram_score"],
        "google_maps":         scores["google_maps_score"],
        "website":             scores["website_score"],
        "brand_consistency":   scores["brand_consistency_score"],
        "customer_engagement": scores["customer_engagement_score"],
    }
    for pillar, score in pillars.items():
        threshold = THRESHOLDS[pillar]["low"]
        level = "low" if score < threshold else "medium"
        result[pillar] = TIPS[pillar][level]
    return result