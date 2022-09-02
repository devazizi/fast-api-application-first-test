from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def session_maker():
    database_engine = create_engine('mysql+pymysql://root:@localhost/go_ecommerce')
    Session = sessionmaker(bind=database_engine)
    session = Session()

    return session
