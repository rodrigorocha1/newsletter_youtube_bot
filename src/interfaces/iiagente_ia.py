from abc import ABC, abstractmethod


class IIaagente(ABC):
    @abstractmethod
    def gerar_resumo(self, texto: str, nome_canal: str, titulo_video: str) -> str:
        pass
