from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import json

from database import get_db, init_db, Business, AuditScore
from models import BusinessInput, ScoreResponse
from scoring_engine import compute_total_score
from recommendations import generate_recommendations
from pdf_report import generate_pdf_report

app = FastAPI(title="Digital Presence Scorer API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.post("/api/score", response_model=ScoreResponse)
def score_business(data: BusinessInput, db: Session = Depends(get_db)):
    scores = compute_total_score(data)
    recommendations = generate_recommendations(scores)

    # Save business
    business = Business(
        name=data.name,
        category=data.category,
        city=data.city,
        instagram_handle=data.instagram_handle,
        google_maps_url=data.google_maps_url if hasattr(data, "google_maps_url") else None,
        website_url=data.website_url if hasattr(data, "website_url") else None,
    )
    db.add(business)
    db.commit()
    db.refresh(business)

    # Save audit
    audit = AuditScore(
        business_id=business.id,
        instagram_score=scores["instagram_score"],
        google_maps_score=scores["google_maps_score"],
        website_score=scores["website_score"],
        brand_consistency_score=scores["brand_consistency_score"],
        customer_engagement_score=scores["customer_engagement_score"],
        total_score=scores["total_score"],
        rating=scores["rating"],
        recommendations=json.dumps(recommendations),
    )
    db.add(audit)
    db.commit()

    return ScoreResponse(
        business_name=data.name,
        **scores,
        recommendations=recommendations,
    )

@app.get("/api/businesses")
def list_businesses(db: Session = Depends(get_db)):
    businesses = db.query(Business).all()
    return businesses

@app.get("/api/report/{business_id}")
def download_report(business_id: int, db: Session = Depends(get_db)):
    from fastapi.responses import FileResponse
    business = db.query(Business).filter(Business.id == business_id).first()
    audit = db.query(AuditScore).filter(AuditScore.business_id == business_id).order_by(AuditScore.id.desc()).first()
    if not business or not audit:
        raise HTTPException(status_code=404, detail="Business not found")
    path = generate_pdf_report(business, audit)
    return FileResponse(path, media_type="application/pdf", filename=f"{business.name}_report.pdf")