from typing import List, Optional, Tuple
from src.model.banco.canais import Canais
from src.model.banco.database_connection import DatabaseConnection
from sqlalchemy.sql import func
from sqlalchemy.orm.session import Session


class CanalModel:
    def __init__(self):
        self.__db = DatabaseConnection()
        self.__db.iniciar_banco()

    def obter_sessao(self) -> Session:
        """Método para obter sessão

        Returns:
            Session: obtem a sessão
        """

        return self.__db.obter_sessao()

    def inserir_canal(self, id_canal: str, nm_canal: str, url_canal: str):
        """Método para inserir canal

        Args:
            id_canal (str): id do canal do youtube
            nm_canal (str): nome do canal
            url_canal (str): url do canal Ex: @Sandeco
        """

        sessao = self.obter_sessao()
        canais = Canais(id_canal=id_canal, nome_canal=nm_canal,
                        url_canal=url_canal)
        sessao.add(canais)
        sessao.commit()
        sessao.close()

    def selecionar_canal(self, url_canal: str) -> Tuple[Optional[str], Optional[str]]:
        """Método para selecionar o id e nome do canal usando a url canal

        Args:
            url_canal (str): url do canal Ex: @Sandeco

        Returns:
            Tuple[Optional[str], Optional[str]]: Retorna uma tupla com o id e nome do canal ou none caso não encontre registro
        """

        sessao = self.obter_sessao()
        canal: Optional[Canais] = sessao.query(Canais).filter(
            func.lower(Canais.url_canal) == url_canal.lower()).first()

        if canal is not None:
            return str(canal.id_canal), str(canal.nome_canal)
        return None, None

    def selecionar_canal_id(self, nome_canal: str) -> Optional[str]:
        """Método para selecionar o id do canal usando o nome

        Args:
            nome_canal (str): nome do canal 

        Returns:
            Optional[str]: id do canal ou none se não encontrar resultado
        """

        try:
            sessao = self.obter_sessao()
            canal = sessao.query(Canais).filter(
                func.lower(Canais.nome_canal) == nome_canal.lower()).first()
            if canal is not None:
                return str(canal.id_canal)
            return None
        except Exception as e:
            return None
        finally:
            sessao.close()

    def selecionar_todos_canais(self) -> Optional[Tuple[str, ...]]:
        """Método para selecionar o nome de todos os canais

        Returns:
            Optional[Tuple[str, ...]]:  Tupla contendo os nomes dos canais, ou None se não encontrar registro
        """
        try:

            sessao = self.obter_sessao()
            canais = sessao.query(Canais.nome_canal).all()
            return tuple(canal.nome_canal for canal in canais)

        except Exception as e:
            return None
        finally:
            sessao.close()
