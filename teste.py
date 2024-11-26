from src.service.youtube.youtube_service import YoutubeService
from src.service.agente_ia.ia_google_gemini import IaAgenteGemini
from datetime import datetime
from src.controllers.youtube_controller import YoutubeController
ys = YoutubeService()
yc = YoutubeController(ia_agente=IaAgenteGemini())

canal = 'UCrOH1V-FyMunBIMrKL0y0xQ'


data_inicio = datetime(2024, 11, 11)


for vídeo in ys.obter_video_por_data(id_canal=canal, data_inicio=data_inicio):
    print(vídeo)
