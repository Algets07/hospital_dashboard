from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root:1234@localhost/hospital_db"
engine = create_engine(DB_URL)
