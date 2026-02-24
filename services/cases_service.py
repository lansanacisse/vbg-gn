"""
Service CRUD pour les cas VBG.
"""

from datetime import date
from typing import Optional

from sqlalchemy.orm import Session
from models import Case


def get_validated_cases(db: Session, year: Optional[int] = None,
                         region: Optional[str] = None):
    """Retourne les cas validés, avec filtres optionnels."""
    q = db.query(Case).filter(Case.status == "validated")
    if year:
        q = q.filter(
            Case.date_incident >= date(year, 1, 1),
            Case.date_incident <= date(year, 12, 31),
        )
    if region and region != "Toutes":
        q = q.filter(Case.region == region)
    return q.order_by(Case.date_incident.desc()).all()


def create_case(db: Session, data: dict) -> Case:
    """Insère un nouveau cas avec statut pending."""
    case = Case(
        region=data["region"],
        prefecture=data["prefecture"],
        type_violence=data["type_violence"],
        victim_age=data.get("victim_age"),
        victim_gender=data.get("victim_gender"),
        date_incident=data["date_incident"],
        status="pending",
        association_id=data.get("association_id"),
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


def get_all_cases_count(db: Session) -> int:
    return db.query(Case).filter(Case.status == "validated").count()
