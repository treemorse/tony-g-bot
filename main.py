import os
import telegram

def telegram_bot(request):
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])