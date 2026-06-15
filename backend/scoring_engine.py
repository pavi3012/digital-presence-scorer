def compute_total_score(data):
    """
    Calculate scores based on business input data
    """
    # Instagram Score (0-100)
    instagram_score = 0
    if data.instagram_handle:
        if data.instagram_followers:
            instagram_score += min(data.instagram_followers / 10000 * 20, 20)
        if data.instagram_posts_per_week:
            instagram_score += min(data.instagram_posts_per_week * 5, 25)
        if data.instagram_engagement_rate:
            instagram_score += min(data.instagram_engagement_rate * 10, 30)
        if data.instagram_bio_complete:
            instagram_score += 25
    
    # Google Maps Score (0-100)
    google_maps_score = 0
    if data.google_maps_listed:
        google_maps_score += 20
        if data.google_maps_rating:
            google_maps_score += (data.google_maps_rating / 5) * 30
        if data.google_maps_reviews:
            google_maps_score += min(data.google_maps_reviews / 50 * 30, 30)
        if data.google_maps_photos:
            google_maps_score += min(data.google_maps_photos / 20 * 10, 10)
        if data.google_maps_hours_set:
            google_maps_score += 10
    
    # Website Score (0-100)
    website_score = 0
    if data.has_website:
        website_score += 30
        if data.website_mobile_friendly:
            website_score += 25
        if data.website_load_fast:
            website_score += 25
        if data.website_contact_visible:
            website_score += 20
    
    # Brand Consistency Score (0-100)
    brand_consistency_score = 0
    if data.same_name_across_platforms:
        brand_consistency_score += 40
    if data.same_logo_across_platforms:
        brand_consistency_score += 30
    if data.consistent_colors:
        brand_consistency_score += 30
    
    # Customer Engagement Score (0-100)
    customer_engagement_score = 0
    if data.replies_to_reviews:
        customer_engagement_score += 40
    if data.whatsapp_business_active:
        customer_engagement_score += 30
    if data.average_response_time_hours:
        if data.average_response_time_hours <= 1:
            customer_engagement_score += 30
        elif data.average_response_time_hours <= 24:
            customer_engagement_score += 20
        elif data.average_response_time_hours <= 48:
            customer_engagement_score += 10
    
    # Total Score (average of all scores)
    total_score = (
        instagram_score +
        google_maps_score +
        website_score +
        brand_consistency_score +
        customer_engagement_score
    ) / 5
    
    # Determine rating
    if total_score >= 90:
        rating = "Excellent"
        color = "#4CAF50"
    elif total_score >= 75:
        rating = "Good"
        color = "#8BC34A"
    elif total_score >= 60:
        rating = "Average"
        color = "#FFC107"
    elif total_score >= 40:
        rating = "Poor"
        color = "#FF9800"
    else:
        rating = "Critical"
        color = "#F44336"
    
    return {
        "instagram_score": round(instagram_score, 2),
        "google_maps_score": round(google_maps_score, 2),
        "website_score": round(website_score, 2),
        "brand_consistency_score": round(brand_consistency_score, 2),
        "customer_engagement_score": round(customer_engagement_score, 2),
        "total_score": round(total_score, 2),
        "rating": rating,
        "color": color
    }