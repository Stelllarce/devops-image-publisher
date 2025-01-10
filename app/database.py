from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import Base


DATABASE_URL = "ibm_db_sa://db2admin:db2admin@62.44.108.24:50000/\
                SAMPLE?currentSchema=FN24_2MI0700130"


engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine


Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)
