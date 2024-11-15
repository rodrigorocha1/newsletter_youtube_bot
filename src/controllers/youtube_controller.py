from model.youtube.youtube_service import YoutubeService
from model.agente_ia.iiagente_ia import IIaagente


class YoutubeController:

    def __init__(self, ia_agente: IIaagente):
        self.__youtube = YoutubeService()
        self.__ia_agente = ia_agente

    def obter_videos(self):
        pass

    def gravar_videos(self):
        pass

    def obter_canal(self):
        pass

    def gravar_canal(self):
        pass
