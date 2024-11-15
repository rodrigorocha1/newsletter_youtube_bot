import telebot
import os
from dotenv import load_dotenv
load_dotenv()


class TelegramBot:
    def __init__(self):
        self.__bot = telebot.TeleBot(os.environ['TOKEN_TELEGRAM'])

    def start(self):
        @self.__bot.message_handler(commands=['start'])
        def exibir_boas_vindas(message):
            self.__bot.reply_to(
                message,
                """
                <b>Bem-vindo ao Bot NewsLetterYoutube!</b> \n
                Use <b>/cadastrar_canal</b> para adicionar o canal \n
                <b>/listar_canal</b> para ver o conteúdo cadastrado.
        """,
                parse_mode='HTML'
            )

    def run(self):
        self.start()
        self.__bot.polling()


bot = TelegramBot()
bot.run()
