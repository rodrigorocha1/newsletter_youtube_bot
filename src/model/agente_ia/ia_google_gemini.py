from langchain_google_genai import ChatGoogleGenerativeAI
from src.model.agente_ia.iiagente_ia import IIaagente
import os


class IaAgenteGemini(IIaagente):
    def __init__(self):
        self.__key = os.environ['GOOGLE_API_KEY']
        self.__llm = ChatGoogleGenerativeAI(
            api_key=self.__key,
            model='gemini-1.5-pro',
            temperature=1
        )

    def gerar_resumo(self, texto: str) -> str:
        messages = [
            ('system', 'Você é um programador python com mais de 20 anos de experiência'),
            ('human', texto),
        ]
        response = self.__llm.invoke(messages)
        return response.content
