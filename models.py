"""
Modèles SQLAlchemy – base SQLite locale.
"""

import uuid
from datetime import datetime, date

from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

import enum


class CaseStatus(str, enum.Enum):
    pending = "pending"
    validated = "validated"
    rejected = "rejected"


class Association(Base):
    __tablename__ = "associations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    cases = relationship("Case", back_populates="association")

    def __repr__(self):
        return f"<Association {self.name}>"


class Case(Base):
    __tablename__ = "cases"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    association_id = Column(String, ForeignKey("associations.id"), nullable=True)
    region = Column(String, nullable=False)
    prefecture = Column(String, nullable=False)
    type_violence = Column(String, nullable=False)
    victim_age = Column(Integer, nullable=True)
    victim_gender = Column(String, nullable=True)
    date_incident = Column(Date, nullable=False)
    status = Column(String, default="pending", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    association = relationship("Association", back_populates="cases")

    def to_dict(self):
        return {
            "id": str(self.id),
            "association_id": str(self.association_id) if self.association_id else None,
            "region": self.region,
            "prefecture": self.prefecture,
            "type_violence": self.type_violence,
            "victim_age": self.victim_age,
            "victim_gender": self.victim_gender,
            "date_incident": self.date_incident.isoformat() if self.date_incident else None,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
