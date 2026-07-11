from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.user_model import User

from app.routes.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StreamSphere AI API",
    version="1.0.0"
)

app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to StreamSphere AI 🚀",
        "status": "Running Successfully"
    }