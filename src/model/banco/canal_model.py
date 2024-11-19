from src.model.banco.canais import Canais
from src.model.banco.database_connection import DatabaseConnection


class CanalModel:
    def __init__(self):
        self.__db = DatabaseConnection()
        self.__db.iniciar_banco()

    def obter_sessao(self):
        return self.__db.obter_sessao()

    def inserir_canal(self, id_canal: str, nm_canal: str):

        sessao = self.obter_sessao()
        canais = Canais(id_canal=id_canal, nome_canal=nm_canal)
        sessao.add(canais)
        sessao.commit()
