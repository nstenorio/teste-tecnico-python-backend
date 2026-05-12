from collections import Counter
from sqlalchemy.orm import Session

from app.models.focus_session import FocusSession

def generate_productivity_diagnosis(db: Session):
    sessions = db.query(FocusSession).all()

    for session in sessions:
        print(session.category)

    if not sessions:
        return {
            "message": "No focus sessions found."
        }
    
    total_sessions = len(sessions)

    total_focus_time = sum(
        session.duration_minutes
        for session in sessions
    )

    average_focus_level = round(
        sum(session.focus_level for session in sessions)
        / total_sessions,
        2
    )

    categories = [
        session.category
        for session in sessions
        if session.category
    ]

    most_productive_category = None

    if categories:
        most_productive_category = Counter(categories).most_common(1)[0][0]

    feedback = generate_feedback(
        average_focus_level,
        total_focus_time
    )

    return {
        "average_focus_level": average_focus_level,
        "total_focus_time": total_focus_time,
        "total_sessions": total_sessions,
        "most_productive_category": most_productive_category,
        "feedback": feedback
    }

def generate_feedback(
        average_focus_level: float,
        total_focus_time: int
):
    if average_focus_level >= 4.5 and total_focus_time >= 300:
        return (
            "Você está em um fluxo de alta produtividade! "
            "Mantenha o equilíbrio entre produtividade e descanso para sustentar esse desempenho."
        )
    if average_focus_level < 3:
        return (
            "Seu nível de concentração está baixo. "
            "Tente reduzir as distrações e fazer pausas estratégicas."
        )
    if total_focus_time < 60:
        return (
            "Seu tempo total de concentração é baixo. "
            "Considere aumentar as suas sessões de foco."
        )
    
    return (
        "Seu desempenho é bem equilibrado e consistente."
    )
