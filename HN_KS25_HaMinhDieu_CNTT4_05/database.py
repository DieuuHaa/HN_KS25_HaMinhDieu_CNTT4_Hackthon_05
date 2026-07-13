from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://root:270703@localhost:3306/library_db"

engine = create_engine(DB_URL)

LocalSession = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush= False, 
    expire_on_commit= False
)

def get_db():
    db = LocalSession()
    try: 
        yield db 
    finally:
        db.close()