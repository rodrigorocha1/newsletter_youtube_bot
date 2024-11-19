from src.model.banco.videos import Videos
from src.model.banco.database_connection import DatabaseConnection
from sqlalchemy.sql import func


class VideoModel:
    def __init__(self):
        self.__db = DatabaseConnection()
        self.__db.iniciar_banco()

    def obter_sessao(self):
        return self.__db.obter_sessao()

    def inserir_video(self, id_video: str, nm_video: str, transcricao: str, id_canal: str):

        sessao = self.obter_sessao()
        video = Videos(
            id_video=id_video,
            id_canal=id_canal,
            nm_video=nm_video,
            transcricao=transcricao
        )
        sessao.add(video)
        sessao.commit()
        sessao.close()

    def selecionar_video(self, id_video: str):
        sessao = self.obter_sessao()
        video = sessao.query(Videos).filter(
            Videos.id_video == id_video).first()
        if video:
            id_video = Videos.id_video
            return id_video
        return None
