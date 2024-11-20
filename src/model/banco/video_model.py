from typing import Optional, Tuple
from src.model.banco.videos import Videos
from src.model.banco.database_connection import DatabaseConnection
from sqlalchemy.orm.session import Session


class VideoModel:
    def __init__(self):
        self.__db = DatabaseConnection()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        """Método para obter sessão

        Returns:
            Session: retorna a sessão do sql alchemy
        """
        return self.__db.obter_sessao()

    def inserir_video(self, id_video: str, nm_video: str, transcricao: str, id_canal: str):
        """Método para inserir o vídeo

        Args:
            id_video (str): id do vídeo
            nm_video (str): nome do vídeo
            transcricao (str): transcrição 
            id_canal (str): id do canal
        """

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

    def selecionar_video_canal(self, id_canal: str) -> Tuple[str, ...]:
        """Método para obter uma lista de vídeos usando o id canal

        Args:
            id_canal (str): id do canal

        Returns:
            Tuple[str, ...]: uma tupla com os dados do nome do vídeo
        """
        sessao = self.obter_sessao()
        videos = sessao.query(Videos.nm_video).filter(
            Videos.id_canal == id_canal)
        sessao.close()
        return tuple(video.nm_video for video in videos)

    def selecionar_video(self, id_video: str) -> Optional[str]:
        """Método para obter o id_vídeo usando o nome do vídeo

        Args:
            id_video (str): nome do vídeo

        Returns:
            Optional[str]: retorna o id vídeo
        """
        sessao = self.obter_sessao()
        video = sessao.query(Videos).filter(
            Videos.id_video == id_video).first()

        if video:
            sessao.close()
            id_video = str(video.id_video)
            return id_video

        sessao.close()
        return None

    def selecionar_video_nome(self, nome_video: str) -> Optional[str]:
        """Método para obter a trasncrição do vídeo

        Args:
            nome_video (str): nome do vídeo

        Returns:
            Optional[str]: a transcrição do vídeo ou False se não encontrar
        """
        try:
            sessao = self.obter_sessao()
            videos = sessao.query(Videos.transcricao).filter(
                Videos.nm_video == nome_video
            ).first()

            if videos:
                return videos.transcricao
            return None
        except Exception as e:
            return None
        finally:
            sessao.close()
