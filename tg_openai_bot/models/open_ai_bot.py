from django.conf import settings

from intagration_utils_candidate.app_telegram_bot.models.abstract_bot import AbstractBot
from tg_openai_bot.models import OpenAiUser, OpenAiUserChat, OpenAiUserMessage

# Импорт библиотеки OpenAI
import openai
openai.api_key = settings.OPEN_AI_API_KEY

MODEL = "gpt-3.5-turbo"


def handle_updates():
    OpenAiBot.objects.get(pk=1).handle_updates()


# Бот на основе AbstractBot
class OpenAiBot(AbstractBot):
    USER_CLASS = OpenAiUser
    CHAT_CLASS = OpenAiUserChat
    MESSAGE_CLASS = OpenAiUserMessage
    CONTEXT = []  # Константа для будущего сохранения диалога

    # Хендлер проверяющей команды старб
    def on_start_command(self, message, t_user, t_chat, param):
        self.send_message(t_chat.telegram_id, "Команда start принята, чтобы спросить бота, напишите /gpt")

    #  Хендлер команды для запроса к GPT, используем модель gpt-3.5-turbo
    def on_gpt_command(self, message, t_user, t_chat, param):
        if not param:
            self.send_message(t_chat.telegram_id, 'Введите запрос')
            return
        OpenAiBot.CONTEXT.append({'role': 'user', 'content': param})
        completion = openai.ChatCompletion.create(
            model=MODEL,
            messages=OpenAiBot.CONTEXT
        )
        response_content = completion.choices[0].message.content
        self.send_message(t_chat.telegram_id, response_content)
        OpenAiBot.CONTEXT.append({'role': 'assistant', 'content': response_content})

    # Хендлер команды помощь
    def on_help_command(self, message, t_user, t_chat, param):
        self.send_message(t_chat.telegram_id, "На данный момент доступны следующие команды:\n"
                                              "/start - проверка бота\n"
                                              "/gpt - задать вопрос")

    # Проверка на существующую команду
    def check_command(self, message, t_user, t_chat):
        if message.text.startswith('/'):
            # Проверяем, является ли сообщение командой
            command = message.text.split(' ')[0]
            if command == '/start':
                self.on_start_command(message, t_user, t_chat, param=None)
            elif command == '/gpt':
                self.on_gpt_command(message, t_user, t_chat, param=message.text[len(command) + 1:])
            elif command == '/help':
                self.on_help_command(message, t_user, t_chat, param=None)
            else:
                # Если команда не распознана, можно отправить ответ с сообщением об ошибке
                self.send_message(t_chat.telegram_id, "Неизвестная команда. Для списка доступных команд введите /help")
