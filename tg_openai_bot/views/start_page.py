from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from tg_openai_bot.cron import handle_bot_updates


@main_auth(on_cookies=True)
def start_page_open_ai(request):
    if request.method == 'POST':

        # Получаем токен бота и чатайди из формы юзера, для stand alone бота ниже
        # bot_token = request.POST.get('bot_token')
        # chat_id = request.POST.get('chat_id')

        while True:
            handle_bot_updates('tg_openai_bot.models.open_ai_bot.OpenAiBot')

        # Подгружаем stand alone бота в чат с приветственным сообщением
        # say_hello(register_bot(bot_token), chat_id)

    return render(request, 'open_ai_start.html')
