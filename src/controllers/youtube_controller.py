from model.youtube.youtube_service import YoutubeService
from model.agente_ia.iiagente_ia import IIaagente
from model.banco.database_connection import DatabaseConnection


class YoutubeController:

    def __init__(self, ia_agente: IIaagente):
        self.__youtube = YoutubeService()
        self.__ia_agente = ia_agente
        self.__database = DatabaseConnection()

    def gravar_videos(self, nome_canal: str):
        data_publicacao = self.__selecionar_data()
        id_canal = self.__youtube.obter_id_canal(nm_canal=nome_canal)
        lista_videos = self.__youtube.obter_video_por_data(
            id_canal=id_canal,
            data_inicio=data_publicacao
        )
        for id_video in lista_videos:
            self.__youtube.obter_transcricao_video(id_video=id_video)
        self.__database.obter_sessao().add()

    def listar_resumos(self):
        pass

    def listar_videos(self):
        pass

    def gravar_canal(self):
        pass

    def listar_canal(self):
        pass

    def atualizar_data(self):
        pass

    def __selecionar_data(self):
        pass
