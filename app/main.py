from fastapi import FastAPI

from app.database import Base, engine
from app.models import URL

app = FastAPI(
    title="NanoLink API",
    version="1.0.0"
)

# Create all database tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to NanoLink 🚀"
    }