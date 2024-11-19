from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from datetime import datetime


class IServiceAPI(ABC):

    @abstractmethod
    def obter_id_canal(self, url_canal: str) -> Optional[Tuple[str, str]]:
        pass

    @abstractmethod
    def obter_video_por_data(self, id_canal: str, data_inicio: datetime) -> List[Tuple[str, str]]:
        pass

    @abstractmethod
    def obter_transcricao_video(self, id_video: str) -> str:
        pass
