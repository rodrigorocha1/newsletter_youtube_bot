from typing import Any, Dict, List, Optional
from src.service.iservice_api import IServiceAPI
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from datetime import datetime

load_dotenv()


class YoutubeService(IServiceAPI):

    def __init__(self):
        self.__api_key = os.environ['YOUTUBE_API_KEY']
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)

    def obter_id_canal(nm_canal: str) -> Optional[str]:
        pass

    def obter_video_por_data(id_canal: str, data_inicio: datetime) -> List[Dict[str, Any]]:
        pass

    def obter_transcricao_video(id_video: str) -> str:
        return super().obter_transcricao_video()
