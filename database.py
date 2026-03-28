from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_URL

engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},
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
    """Retourne une session directe (pour usage dans les callbacks)."""
    return SessionLocal()