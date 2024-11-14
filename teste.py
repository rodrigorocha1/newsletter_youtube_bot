from src.service.youtube_service import YoutubeService
from datetime import datetime

ys = YoutubeService()

canal = '@TLESGames'


id_canal = ys.obter_id_canal(nm_canal=canal)
print(id_canal)
data_inicio = datetime(2024, 11, 11)
id_videos = ys.obter_video_por_data(id_canal=id_canal, data_inicio=data_inicio)
print(id_videos)

for id_video in id_videos:
    try:
        print(ys.obter_transcricao_video(id_video=id_video))
    except:
        pass
