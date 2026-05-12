from sqlalchemy import Column, Integer, String
from app.database import Base

class FocusSession(Base):
    __tablename__ = "focus_sessions"

    id = Column(Integer, primary_key=True, index=True)
    focus_level = Column(Integer, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    category = Column(String, nullable=True)

