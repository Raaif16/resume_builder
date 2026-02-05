from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Database URL configuration
# - For local development: uses PostgreSQL
# - For PythonAnywhere: uses MySQL (set DATABASE_URL environment variable)
#
# PythonAnywhere MySQL format:
# mysql://Raaif16:YOUR_PASSWORD@Raaif16.mysql.pythonanywhere-services.com/Raaif16$resume_builder

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:postgres@localhost:5433/lmsdb"
)

# Handle MySQL connection pooling settings for PythonAnywhere
if DATABASE_URL.startswith("mysql"):
    engine = create_engine(
        DATABASE_URL,
        pool_recycle=280,  # PythonAnywhere requires this for MySQL
        pool_pre_ping=True
    )
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
