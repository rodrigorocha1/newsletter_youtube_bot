from src.interfaces.iiagente_ia import IIaagente
from src.service.youtube.youtube_service import YoutubeService
from src.model.banco.canal_model import CanalModel


class YoutubeController:

    def __init__(self, ia_agente: IIaagente):
        self.__youtube = YoutubeService()
        self.__ia_agente = ia_agente
        self.__canal_model = CanalModel()

    def gravar_canal(self, nome_canal: str):
        id_canal, nome_canal = self.__youtube.obter_id_canal(
            nm_canal=nome_canal)

        self.__canal_model.inserir_canal(
            id_canal=id_canal, nm_canal=nome_canal)
