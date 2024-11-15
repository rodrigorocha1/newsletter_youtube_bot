from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

CAMINHO_BANCO = os.path.join(os.getcwd(), 'database', 'youtube.db')

DATABASE_URL = f'sqlite:///{CAMINHO_BANCO}'

Base = declarative_base()


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
