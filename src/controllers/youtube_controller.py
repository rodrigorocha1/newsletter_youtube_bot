from src.interfaces.iiagente_ia import IIaagente
from src.service.youtube.youtube_service import YoutubeService
from src.model.banco.canal_model import CanalModel


class YoutubeController:

    def __init__(self, ia_agente: IIaagente):
        self.__youtube = YoutubeService()
        self.__ia_agente = ia_agente
        self.__canal_model = CanalModel()

    def gravar_canal(self, url_canal: str):
        dados_canal = self.__canal_model.selecionar_canal(url_canal=url_canal)

        if dados_canal[0]:
            return  # Canal já cadastrado

        id_canal, nome_canal = self.__youtube.obter_id_canal(
            url_canal=url_canal)
        if id_canal:
            self.__canal_model.inserir_canal(
                id_canal=id_canal, nm_canal=nome_canal, url_canal=url_canal)
            return dados_canal  # Canal inserido
        else:
            return  # Canal não encontrado
