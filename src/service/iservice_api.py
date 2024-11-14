from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime


class IServiceAPI(ABC):

    @abstractmethod
    def obter_id_canal(nm_canal: str) -> Optional[str]:
        pass

    @abstractmethod
    def obter_video_por_data(id_canal: str, data_inicio: datetime) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def obter_transcricao_video(id_video: str) -> str:
        pass
