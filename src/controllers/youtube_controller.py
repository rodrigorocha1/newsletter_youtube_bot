from datetime import datetime
from typing import Any, Literal, Optional, Tuple, Union
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

    def gravar_canal(self, url_canal: str) -> Union[
        Tuple[str, Optional[str], Literal[False]],
        Tuple[Union[str, Any], Union[str, Any], Literal[True]],
        Literal[False]
    ]:
        dados_canal = self.__canal_model.selecionar_canal(url_canal=url_canal)

        if dados_canal and dados_canal[0]:

            return dados_canal[0], dados_canal[1], False  # Canal já cadastrado

        id_canal, nome_canal = self.__youtube.obter_id_canal(
            url_canal=url_canal)
        if id_canal:
            print('a', id_canal, nome_canal)
            self.__canal_model.inserir_canal(
                id_canal=id_canal, nm_canal=nome_canal, url_canal=url_canal)
            return id_canal, nome_canal, True  # Canal inserido
        else:
            return False  # Canal não encontrado

    def gravar_video(self,  id_canal: str, data_inicio: datetime, nome_canal: str):

        lista_videos = self.__youtube.obter_video_por_data(
            id_canal=id_canal, data_inicio=data_inicio)
        for dados_video in lista_videos:
            id_video = self.__video_model.selecionar_video(
                id_video=dados_video[0])
            if not id_video:
                transcricao = self.__youtube.obter_transcricao_video(
                    id_video=dados_video[0])
                if transcricao:
                    resumo_gerado_ia = self.__ia_agente.gerar_resumo(
                        texto=str(transcricao), nome_canal=nome_canal, titulo_video=dados_video[1])
                    self.__video_model.inserir_video(
                        id_video=dados_video[0], nm_video=dados_video[1], transcricao=resumo_gerado_ia, id_canal=id_canal)

    def gerar_input_canais(self) -> Optional[Tuple[str, ...]]:
        canais = self.__canal_model.selecionar_todos_canais()
        return canais

    def gerar_input_video(self, nome_canal: str):
        id_canal = self.__canal_model.selecionar_canal_id(
            nome_canal=nome_canal)

        lista_videos = self.__video_model.selecionar_video_canal(
            id_canal=str(id_canal))
        return lista_videos

    def gerar_transcricao(self, nome_video: str):
        transcricao = self.__video_model.selecionar_video_nome(
            nome_video=nome_video)

        return transcricao
