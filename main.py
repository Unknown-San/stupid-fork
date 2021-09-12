import requests
import json
import random

from telegram.ext import (
Updater,
CommandHandler,
MessageHandler,
Filters,
ConversationHandler
)

TOKEN = '1962700368:AAEqH4n3jnOWZD6U-eyS3BntvCseKSEBIbE'

ASK_WAIFU = range(1)


def ask_waifu(update, context):
    update.message.reply_text("Digite uma tag que eu procuro uma waifu pra vc")

    return ASK_WAIFU


def get_waifu(update, context):

    tag = update.message.text
    API_KEY = "&api_key=d4c3b61a545bde1f87abd3e0fde5ec4f4cdec0ef5a34bee5e01a19f9966b80df&user_id=602312"
    url = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&api_key=" + API_KEY + "&json=1&limit=5&tags=" + tag

    request = requests.get(url)
    json_list = request.json()  # ITS A FUCKING LIST AGAIN...which makes sense since its 5 elements
    true_json = json_list[0:5]  # returns the dict part

    random_waifu = random.choice(true_json)  # to make the program return ONE random image
    get_img_url = random_waifu.get("file_url")

    update.message.reply_text(get_img_url)

    return ConversationHandler.END


updater = Updater(TOKEN, use_context=True)
entregador = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('waifu', ask_waifu)],
    fallbacks=[],

    states={
        ASK_WAIFU: [MessageHandler(Filters.text, get_waifu)],

    },
)


entregador.add_handler(conv_handler)


updater.start_polling()
updater.idle()
