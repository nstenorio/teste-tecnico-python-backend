from fastapi import FastAPI

from app.database import Base, engine
from app.models.focus_session import FocusSession
from app.routes.focus_session_routes import router as focus_session_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(focus_session_router)

@app.get("/")
def home():
    return {
        "message": "Focus Performance API is running!"
    }