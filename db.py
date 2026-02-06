from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Use SQLite for Hugging Face Spaces deployment
# The database file is stored in /app/data for persistence
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:////app/data/resume.db"
)

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()