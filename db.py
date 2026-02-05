from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Database URL configuration
# - For local development: uses PostgreSQL (default)
# - For PythonAnywhere free tier: uses SQLite (set DATABASE_URL env var)
#
# SQLite format for PythonAnywhere:
# sqlite:////home/Raaif16/resume_builder/resume.db

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:postgres@localhost:5433/lmsdb"
)

# SQLite needs special connect_args
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}  # Required for SQLite with FastAPI
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
