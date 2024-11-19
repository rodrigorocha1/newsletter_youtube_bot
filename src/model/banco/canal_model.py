from src.model.banco.canais import Canais
from src.model.banco.database_connection import DatabaseConnection
from sqlalchemy.sql import func


class CanalModel:
    def __init__(self):
        self.__db = DatabaseConnection()
        self.__db.iniciar_banco()

    def obter_sessao(self):
        return self.__db.obter_sessao()

    def inserir_canal(self, id_canal: str, nm_canal: str, url_canal: str):

        sessao = self.obter_sessao()
        canais = Canais(id_canal=id_canal, nome_canal=nm_canal,
                        url_canal=url_canal)
        sessao.add(canais)
        sessao.commit()
        sessao.close()

    def selecionar_canal(self, url_canal: str):
        sessao = self.obter_sessao()
        canal = sessao.query(Canais).filter(
            func.lower(Canais.url_canal) == url_canal.lower()).first()
        if canal:
            nome_canal = canal.nome_canal
            id_canal = canal.id_canal
        else:
            nome_canal = id_canal = canal

        return nome_canal, id_canal
