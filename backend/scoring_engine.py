def score_instagram(data) -> float:
    score = 0.0

    # Follower count (max 5 pts)
    followers = data.instagram_followers or 0
    if followers >= 5000:   score += 5
    elif followers >= 1000: score += 4
    elif followers >= 500:  score += 3
    elif followers >= 100:  score += 2
    elif followers >= 10:   score += 1

    # Posts per week (max 8 pts)
    ppw = data.instagram_posts_per_week or 0
    if ppw >= 5:   score += 8
    elif ppw >= 3: score += 6
    elif ppw >= 2: score += 4
    elif ppw >= 1: score += 2

    # Engagement rate (max 7 pts)
    er = data.instagram_engagement_rate or 0.0
    if er >= 5.0:   score += 7
    elif er >= 3.0: score += 5
    elif er >= 1.5: score += 3
    elif er >= 0.5: score += 1

    # Bio completeness (max 5 pts)
    if data.instagram_bio_complete:
        score += 5

    return min(score, 25.0)


def score_google_maps(data) -> float:
    score = 0.0

    if data.google_maps_listed:    score += 5   # Listed at all
    if data.google_maps_hours_set: score += 3   # Business hours filled

    # Rating (max 7 pts)
    rating = data.google_maps_rating or 0.0
    if rating >= 4.5:   score += 7
    elif rating >= 4.0: score += 5
    elif rating >= 3.5: score += 3
    elif rating >= 3.0: score += 1

    # Number of reviews (max 6 pts)
    reviews = data.google_maps_reviews or 0
    if reviews >= 100: score += 6
    elif reviews >= 50: score += 5
    elif reviews >= 20: score += 3
    elif reviews >= 5:  score += 1

    # Photos uploaded (max 4 pts)
    photos = data.google_maps_photos or 0
    if photos >= 20:  score += 4
    elif photos >= 10: score += 3
    elif photos >= 5:  score += 2
    elif photos >= 1:  score += 1

    return min(score, 25.0)


def score_website(data) -> float:
    score = 0.0
    if data.has_website:            score += 8
    if data.website_mobile_friendly: score += 5
    if data.website_load_fast:       score += 4
    if data.website_contact_visible: score += 3
    return min(score, 20.0)


def score_brand_consistency(data) -> float:
    score = 0.0
    if data.same_name_across_platforms:  score += 5
    if data.same_logo_across_platforms:  score += 5
    if data.consistent_colors:           score += 5
    return min(score, 15.0)


def score_customer_engagement(data) -> float:
    score = 0.0
    if data.replies_to_reviews:       score += 5
    if data.whatsapp_business_active: score += 5

    # Response time scoring (max 5 pts)
    hours = data.average_response_time_hours or 48
    if hours <= 1:    score += 5
    elif hours <= 3:  score += 4
    elif hours <= 12: score += 3
    elif hours <= 24: score += 2
    elif hours <= 48: score += 1

    return min(score, 15.0)


def get_rating(total: float) -> tuple[str, str]:
    if total >= 80:   return "Excellent", "#16a34a"
    elif total >= 60: return "Good",      "#ca8a04"
    elif total >= 40: return "Average",   "#ea580c"
    else:             return "Poor",      "#dc2626"


def compute_total_score(data) -> dict:
    insta   = score_instagram(data)
    google  = score_google_maps(data)
    website = score_website(data)
    brand   = score_brand_consistency(data)
    engage  = score_customer_engagement(data)
    total   = insta + google + website + brand + engage
    rating, color = get_rating(total)

    return {
        "instagram_score":           insta,
        "google_maps_score":         google,
        "website_score":             website,
        "brand_consistency_score":   brand,
        "customer_engagement_score": engage,
        "total_score":               round(total, 1),
        "rating":                    rating,
        "color":                     color,
    }