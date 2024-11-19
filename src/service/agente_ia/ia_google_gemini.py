from langchain_google_genai import ChatGoogleGenerativeAI
from src.interfaces.iiagente_ia import IIaagente
import os


class IaAgenteGemini(IIaagente):
    def __init__(self):
        self.__key = os.environ['GOOGLE_API_KEY']
        self.__llm = ChatGoogleGenerativeAI(
            api_key=self.__key,
            model='gemini-1.5-pro',
            temperature=1
        )

    def gerar_resumo(self, texto: str, nome_canal: str, titulo_video: str) -> str:
        messages = [
            (
                'system',
                f""" 
                    Você tem experiência em criar Newsletter da transcrição dos vídeos do youtube no seguinte formato:
                    Vídeo: {titulo_video}

                    Canal: {nome_canal}

                    Resumo: aqui vem a transcrição do vídeo resumida

                    Formate em markdown para exibição em metade da página do navegador
                """),
            ('human', texto),
        ]
        response = self.__llm.invoke(messages)
        return response.content
