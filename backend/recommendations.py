def generate_recommendations(scores):
    """
    Generate recommendations based on scores
    """
    recommendations = {
        "instagram": [],
        "google_maps": [],
        "website": [],
        "brand_consistency": [],
        "customer_engagement": []
    }
    
    # Instagram recommendations
    if scores["instagram_score"] < 60:
        if scores["instagram_score"] < 30:
            recommendations["instagram"].append("🚨 Create an Instagram business account immediately")
        recommendations["instagram"].append("📱 Post at least 3-5 times per week")
        recommendations["instagram"].append("💬 Engage with followers by responding to comments")
        recommendations["instagram"].append("📊 Complete your Instagram bio with website and contact info")
    
    # Google Maps recommendations
    if scores["google_maps_score"] < 60:
        recommendations["google_maps"].append("📍 Claim and verify your Google Business Profile")
        recommendations["google_maps"].append("⭐ Encourage customers to leave reviews")
        recommendations["google_maps"].append("📸 Add 10+ photos of your business")
        recommendations["google_maps"].append("🕐 Set accurate business hours")
    
    # Website recommendations
    if scores["website_score"] < 60:
        recommendations["website"].append("🌐 Create a professional website")
        recommendations["website"].append("📱 Make your website mobile-friendly")
        recommendations["website"].append("⚡ Improve website loading speed")
        recommendations["website"].append("📞 Display contact information prominently")
    
    # Brand consistency recommendations
    if scores["brand_consistency_score"] < 70:
        recommendations["brand_consistency"].append("🎨 Use the same business name across all platforms")
        recommendations["brand_consistency"].append("🖼️ Use the same logo everywhere")
        recommendations["brand_consistency"].append("🌈 Maintain consistent brand colors")
    
    # Customer engagement recommendations
    if scores["customer_engagement_score"] < 60:
        recommendations["customer_engagement"].append("💬 Reply to all customer reviews")
        recommendations["customer_engagement"].append("📱 Activate WhatsApp Business for quick communication")
        recommendations["customer_engagement"].append("⏰ Respond to customer inquiries within 1 hour")
    
    return recommendations