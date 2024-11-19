from datetime import datetime
from src.interfaces.iiagente_ia import IIaagente
from src.service.youtube.youtube_service import YoutubeService
from src.model.banco.canal_model import CanalModel
from src.model.banco.video_model import VideoModel


class YoutubeController:

    def __init__(self, ia_agente: IIaagente):
        self.__youtube = YoutubeService()
        self.__ia_agente = ia_agente
        self.__canal_model = CanalModel()
        self.__video_model = VideoModel()

    def gravar_canal(self, url_canal: str):
        dados_canal = self.__canal_model.selecionar_canal(url_canal=url_canal)

        if dados_canal[0]:

            return dados_canal[0], dados_canal[1]  # Canal já cadastrado

        id_canal, nome_canal = self.__youtube.obter_id_canal(
            url_canal=url_canal)
        if id_canal:
            print('a', id_canal, nome_canal)
            self.__canal_model.inserir_canal(
                id_canal=id_canal, nm_canal=nome_canal, url_canal=url_canal)
            return id_canal, nome_canal  # Canal inserido
        else:
            return  # Canal não encontrado

    def gravar_video(self,  id_canal: str, data_inicio: datetime, nome_canal: str):
        print(id_canal, data_inicio, nome_canal)

        lista_videos = self.__youtube.obter_video_por_data(
            id_canal=id_canal, data_inicio=data_inicio)
        for dados_video in lista_videos:
            id_video = self.__video_model.selecionar_video(
                id_video=dados_video[0])
            if not id_video:
                transcricao = self.__youtube.obter_transcricao_video(
                    id_video=dados_video[0])
                resumo_gerado_ia = self.__ia_agente.gerar_resumo(
                    texto=transcricao, nome_canal=nome_canal, titulo_video=dados_video[1])
                self.__video_model.inserir_video(
                    id_video=dados_video[0], nm_video=dados_video[1], transcricao=resumo_gerado_ia, id_canal=id_canal)
