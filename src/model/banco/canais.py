from sqlalchemy import Column, String
from src.model.banco.config_base import Base


class Canais(Base):

    __tablename__ = 'CANAIS'
    id_canal = Column(
        String,
        primary_key=True,
        index=True
    )

    nome_canal = Column(String)

    def __repr__(self):
        return f"<CANAIS(id_canal={self.id_canal}, nome_canal={self.nome_canal})>"
