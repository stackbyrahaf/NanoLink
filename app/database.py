from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Engine manages the connection to PostgreSQL
# this engine is SQLALchemy's interface connecting to the database
# FastAPI -> SQLAlchemy -> PostgreSQL. engine know how to connect to the database and execute SQL commands
engine = create_engine(DATABASE_URL)

# SessionLocal creates a new database session for each request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class that all SQLAlchemy models will inherit from
Base = declarative_base()