"""
Service CRUD pour les cas VBG.
"""

from datetime import date
from typing import Optional

from sqlalchemy.orm import Session
from models import Case, CaseStatus


def get_validated_cases(
    db: Session, year: Optional[int] = None, region: Optional[str] = None
):
    """Retourne les cas validés, avec filtres optionnels."""
    q = db.query(Case).filter(Case.status == CaseStatus.validated)
    if year:
        q = q.filter(
            Case.date_incident >= date(year, 1, 1),
            Case.date_incident <= date(year, 12, 31),
        )
    if region and region != "Toutes":
        q = q.filter(Case.region == region)
    return q.order_by(Case.date_incident.desc()).all()


def get_pending_cases(db: Session):
    """Retourne tous les cas en attente de validation."""
    return (
        db.query(Case)
        .filter(Case.status == CaseStatus.pending)
        .order_by(Case.created_at.desc())
        .all()
    )


def get_all_cases(
    db: Session, year: Optional[int] = None, region: Optional[str] = None
):
    """Retourne tous les cas (validés + pending) pour l'espace association."""
    q = db.query(Case)
    if year:
        q = q.filter(
            Case.date_incident >= date(year, 1, 1),
            Case.date_incident <= date(year, 12, 31),
        )
    if region and region != "Toutes":
        q = q.filter(Case.region == region)
    return q.order_by(Case.created_at.desc()).all()


def update_case_status(db: Session, case_id: str, new_status: str) -> Optional[Case]:
    """Met à jour le statut d'un cas (validated ou rejected)."""
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        return None
    case.status = new_status
    db.commit()
    db.refresh(case)
    return case


def create_case(db: Session, data: dict) -> Case:
    """Insère un nouveau cas avec statut pending."""
    case = Case(
        region=data["region"],
        prefecture=data["prefecture"],
        type_violence=data["type_violence"],
        victim_age=data.get("victim_age"),
        victim_gender=data.get("victim_gender"),
        date_incident=data["date_incident"],
        status=CaseStatus.pending,
        association_id=data.get("association_id"),
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


def get_all_cases_count(db: Session) -> int:
    """Retourne le nombre total de cas validés."""
    return db.query(Case).filter(Case.status == CaseStatus.validated).count()
