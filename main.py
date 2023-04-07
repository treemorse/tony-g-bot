import os
import telegram
import random
import linecache


def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        if update.message.text == "/phrase":
            with open('sources/phrases.txt', 'r') as f:
                num_lines = sum(1 for line in f)
            rand_line_num = random.randint(1, num_lines)
            rand_line = linecache.getline('sources/phrases.txt', rand_line_num).strip()
            bot.sendMessage(chat_id=chat_id, text=rand_line)
    return "okay"
