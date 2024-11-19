from datetime import datetime
import streamlit as st
from src.service.agente_ia.ia_google_gemini import IaAgenteGemini
from src.controllers.youtube_controller import YoutubeController


class ViewStreamlit:

    st.set_page_config(layout='wide')

    def __init__(self):
        self.__ia_agente = IaAgenteGemini()
        self.__controler = YoutubeController(ia_agente=self.__ia_agente)

    def gerar_input(self):
        with st.container(key='input_nome_canal'):
            url_canal = st.text_input(
                'Digite o nome do canal',
                placeholder='Ex: @TLESGames, @Sandeco'
            )
            d = st.date_input('Digite a data de públicação do vídeo',
                              datetime(2024, 10, 17, 19, 0, 46), format='DD/MM/YYYY')

            tempo = st.time_input('Digite a hora de busca')
            botao_pequisar_canal = st.button('Cadastrar Canal')
            if botao_pequisar_canal:

                data_combinada = datetime.combine(d, tempo)

                st.write("Data e hora combinadas em formato ISO 8601:",
                         type(data_combinada))

                nome_canal,  id_canal = self.__controler.gravar_canal(
                    url_canal=url_canal)
                print(id_canal, nome_canal)
                self.__controler.gravar_video(
                    data_inicio=data_combinada, id_canal=id_canal, nome_canal=nome_canal)

    def rodar_dashboard(self):
        self.gerar_input()
