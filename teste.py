from src.model.youtube_service import YoutubeService
from datetime import datetime

ys = YoutubeService()

canal = '@TLESGames'


id_canal = ys.obter_id_canal(nm_canal=canal)
print(id_canal)
data_inicio = datetime(2024, 11, 11)
lista_videos = ys.obter_video_por_data(
    id_canal=id_canal, data_inicio=data_inicio)
print(lista_videos)

for dados_video in lista_videos:
    try:
        print(ys.obter_transcricao_video(id_video=dados_video[0]))
    except:
        pass
