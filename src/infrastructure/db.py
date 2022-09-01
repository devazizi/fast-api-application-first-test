from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:@localhost:3306/go_ecommerce"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

database_engine = create_engine('mysql+pymysql://root:@localhost/go_ecommerce')
Base = declarative_base()

Session = sessionmaker(bind=database_engine)

session = Session()