from src.service.youtube.youtube_service import YoutubeService
from src.service.agente_ia.ia_google_gemini import IaAgenteGemini
from datetime import datetime
from src.controllers.youtube_controller import YoutubeController
ys = YoutubeService()
yc = YoutubeController(ia_agente=IaAgenteGemini())

canal = '@Sandeco'


yc.gravar_canal(nome_canal=canal)
