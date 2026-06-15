from pydantic import BaseModel, HttpUrl
from typing import Optional

class BusinessInput(BaseModel):
    name: str
    category: str
    city: str = "Tamil Nadu"
    instagram_handle: Optional[str] = None
    instagram_followers: Optional[int] = 0
    instagram_posts_per_week: Optional[float] = 0
    instagram_engagement_rate: Optional[float] = 0.0
    instagram_bio_complete: Optional[bool] = False

    google_maps_listed: Optional[bool] = False
    google_maps_rating: Optional[float] = 0.0
    google_maps_reviews: Optional[int] = 0
    google_maps_photos: Optional[int] = 0
    google_maps_hours_set: Optional[bool] = False

    has_website: Optional[bool] = False
    website_mobile_friendly: Optional[bool] = False
    website_load_fast: Optional[bool] = False
    website_contact_visible: Optional[bool] = False

    same_name_across_platforms: Optional[bool] = False
    same_logo_across_platforms: Optional[bool] = False
    consistent_colors: Optional[bool] = False

    replies_to_reviews: Optional[bool] = False
    whatsapp_business_active: Optional[bool] = False
    average_response_time_hours: Optional[float] = 48.0

class ScoreResponse(BaseModel):
    business_name: str
    instagram_score: float
    google_maps_score: float
    website_score: float
    brand_consistency_score: float
    customer_engagement_score: float
    total_score: float
    rating: str
    color: str
    recommendations: dict