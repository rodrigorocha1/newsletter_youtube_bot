from sqlalchemy import Column, String, ForeignKey
from src.model.banco.config_base import Base


class Videos(Base):
    __tablename__ = 'VIDEOS'
    id_video = Column(
        String,
        primary_key=True,
        index=True
    )
    id_canal = Column(String, ForeignKey('CANAIS.id_canal'))
    nm_video = Column(String)
    transcricao = Column(String)

    def __repr__(self):
        return (
            f'Videos[id_video={self.id_video}, ID_CANAL={self.id_canal}, NM_VIDEO={self.nm_video}, TRANSCRICAO={self.transcricao}'
        )
