from abc import ABC, abstractmethod


class IIaagente(ABC):
    @abstractmethod
    def gerar_resumo(texto: str) -> str:
        pass
