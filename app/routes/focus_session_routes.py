from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.focus_session import FocusSession
from app.schemas.focus_session_schema import FocusSessionCreate
from app.services.productivity_service import (
    generate_productivity_diagnosis
)

router = APIRouter()

@router.post(
        "/focus-sessions",
        status_code=201,
        tags=["Focus Sessions"],
        summary="Criar uma nova Sessão de Foco."
    )
def create_focus_session(
    focus_session: FocusSessionCreate,
    db: Session = Depends(get_db)
):
    new_session = FocusSession(
        focus_level=focus_session.focus_level,
        duration_minutes=focus_session.duration_minutes,
        comment=focus_session.comment,
        category=focus_session.category
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return {
        "message": "Focus session created successfully",
        "data": {
            "id": new_session.id,
            "focus_level": new_session.focus_level,
            "duration_minutes": new_session.duration_minutes,
            "comment": new_session.comment,
            "category": new_session.category
        }
    }

@router.get(
        "/productivity-diagnosis",
        tags=["Productivity Diagnosis"],
        summary="Gerar Diagnóstico de Produtividade com base nas Sessões de Foco"
    )
def get_producitivity_diagnosis(
    db: Session = Depends(get_db)
):
    return generate_productivity_diagnosis(db)