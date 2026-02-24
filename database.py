"""
Connexion à la base de données via SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import SUPABASE_DB_URL

engine = create_engine(
    SUPABASE_DB_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    connect_args={"sslmode": "require"},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Générateur de session DB (context manager)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session():
    """Retourne une session directe (pour usage hors générateur)."""
    return SessionLocal()
