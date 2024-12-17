from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:nasir1@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)
Base = declarative_base()


# try:
#     conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'nasir1', cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("database connected successfully")
# except Exception as error:
#     print("connection fail try again")
#     print("Error : ", error)
#     time.sleep(2)
