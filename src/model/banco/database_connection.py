from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.banco.config_base import Base
import os


class DatabaseConnection:

    def __init__(self) -> None:
        self.__CAMINHO_BANCO = os.path.join(
            os.getcwd(), 'database', 'youtube.dv'
        )
        self.__DATABASE_URL = 'sqlite:///' + self.__CAMINHO_BANCO
        self.engine = create_engine(
            self.__DATABASE_URL, echo=False, isolation_level="AUTOCOMMIT", connect_args={'timeout': 30})
        self.session_local = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)

    def obter_sessao(self):

        session = self.session_local()
        try:
            return session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def iniciar_banco(self):
        Base.metadata.create_all(bind=self.engine)
