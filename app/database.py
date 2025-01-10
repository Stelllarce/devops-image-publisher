from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import Base

DATABASE_URL = "jdbc:db2://62.44.108.24:50000/SAMPLE:currentSchema=FN24_2MI0700130"
DB_USER = "db2admin"
DB_PASSWORD = "db2admin"

engine = create_engine(f"ibm_db_sa://{DB_USER}:{DB_PASSWORD}@{DATABASE_URL}")
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)