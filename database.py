#файл конфигурации Бд

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = "sqlite:///./sql.app.db"
engine = create_engine(SQL_URL, create_engine="check_same_thread": False)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
	db = Sessionlocal()
	try:
		yield db
	except Exception:
		print("Error!!!")
	finally:
		db.close()