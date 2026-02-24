"""
Modèles SQLAlchemy – miroir des tables Supabase.
"""

import uuid
from datetime import datetime, date

from sqlalchemy import (
    Column, String, Integer, Date, DateTime,
    ForeignKey, Enum, text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base

import enum


class CaseStatus(str, enum.Enum):
    pending = "pending"
    validated = "validated"
    rejected = "rejected"


class Association(Base):
    __tablename__ = "associations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow,
                        server_default=text("now()"))

    cases = relationship("Case", back_populates="association")

    def __repr__(self):
        return f"<Association {self.name}>"


class Case(Base):
    __tablename__ = "cases"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))
    association_id = Column(UUID(as_uuid=True),
                            ForeignKey("associations.id"), nullable=True)
    region = Column(String, nullable=False)
    prefecture = Column(String, nullable=False)
    type_violence = Column(String, nullable=False)
    victim_age = Column(Integer, nullable=True)
    victim_gender = Column(String, nullable=True)
    date_incident = Column(Date, nullable=False)
    status = Column(
        Enum("pending", "validated", "rejected", name="case_status"),
        default="pending",
        server_default="pending",
        nullable=False,
    )
    created_at = Column(DateTime, default=datetime.utcnow,
                        server_default=text("now()"))

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
