from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
import os

Base = declarative_base()

class Database:
    def __init__(self, db_path: str = None):
        if db_path:
            self.db_url = f"sqlite:///{db_path}"
        else:
            self.db_url = os.getenv("DATABASE_URL", "sqlite:///default.db")
        
        self.engine = create_engine(self.db_url, echo=False, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_tables(self):
        Base.metadata.create_all(self.engine)


db = Database("mydb.sqlite")
