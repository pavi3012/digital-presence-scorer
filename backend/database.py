from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker  # ✅ updated import
from datetime import datetime

DATABASE_URL = "sqlite:///./scorer.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Business(Base):
    __tablename__ = "businesses"
    id               = Column(Integer, primary_key=True, index=True)
    name             = Column(String, nullable=False)
    category         = Column(String)
    instagram_handle = Column(String)
    google_maps_url  = Column(String)
    website_url      = Column(String)
    whatsapp_number  = Column(String)
    city             = Column(String, default="Tamil Nadu")
    created_at       = Column(DateTime, default=datetime.utcnow)

class AuditScore(Base):
    __tablename__ = "audit_scores"
    id                        = Column(Integer, primary_key=True, index=True)
    business_id               = Column(Integer, ForeignKey("businesses.id"))  # ✅ added
    instagram_score           = Column(Float, default=0)
    google_maps_score         = Column(Float, default=0)
    website_score             = Column(Float, default=0)
    brand_consistency_score   = Column(Float, default=0)
    customer_engagement_score = Column(Float, default=0)
    total_score               = Column(Float, default=0)
    rating                    = Column(String)
    recommendations           = Column(Text)
    audited_at                = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()