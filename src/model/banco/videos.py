from sqlalchemy import Column, String, ForeignKey
from src.model.banco.config_base import Base
from sqlalchemy.orm import mapped_column, Mapped


class Videos(Base):
    __tablename__ = 'VIDEOS'
    id_video: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        index=True
    )
    id_canal: Mapped[str] = mapped_column(
        String, ForeignKey('CANAIS.id_canal'))  # Corrigido aqui
    nm_video: Mapped[str] = mapped_column(String)
    transcricao: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return (
            f'Videos[id_video={self.id_video}, ID_CANAL={self.id_canal}, NM_VIDEO={self.nm_video}, TRANSCRICAO={self.transcricao}'
        )
