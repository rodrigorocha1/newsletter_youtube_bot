from src.service.youtube.youtube_service import YoutubeService
from src.service.agente_ia.ia_google_gemini import IaAgenteGemini
from datetime import datetime
from src.controllers.youtube_controller import YoutubeController
ys = YoutubeService()
yc = YoutubeController(ia_agente=IaAgenteGemini())

canal = '@crazygamerfabinho'


data_inicio = datetime(2024, 11, 11)

nome_canal, id_canal = yc.gravar_canal(url_canal=canal)
yc.gravar_video(id_canal=id_canal, data_inicio=data_inicio,
                nome_canal=nome_canal)
