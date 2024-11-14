from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime


class IServiceAPI(ABC):

    @abstractmethod
    def obter_id_canal(self, nm_canal: str) -> Optional[str]:
        pass

    @abstractmethod
    def obter_video_por_data(self, id_canal: str, data_inicio: datetime) -> List[str]:
        pass

    @abstractmethod
    def obter_transcricao_video(self, id_video: str) -> str:
        pass
