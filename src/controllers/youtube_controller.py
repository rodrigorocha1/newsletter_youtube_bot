from model.youtube.youtube_service import YoutubeService
from model.agente_ia.iiagente_ia import IIaagente
from model.banco.db import SessionLocal


class YoutubeController:

    def __init__(self, ia_agente: IIaagente):
        self.__youtube = YoutubeService()
        self.__ia_agente = ia_agente
        self.__database = SessionLocal()

    def gravar_videos(self):
        id_canal = self.__youtube.obter_id_canal()
        lista_videos = self.__youtube.obter_video_por_data()
        for id_video in lista_videos:
            self.__youtube.obter_transcricao_video()

    def listar_resumos(self):
        pass

    def listar_videos(self):
        pass

    def gravar_canal(self):
        pass

    def listar_canal(self):
        pass
