import requests
import json
import random
import os

from telegram.ext import (
Updater,
CommandHandler,
MessageHandler,
Filters,
ConversationHandler,
CallbackContext,
)

TOKEN = os.getenv('TELEGRAM_BOT_API')
CHECK_NUMBERS, ASK_CONTINUE = range(2)

def start(update, context):
    update.message.reply_text("nHentai bot initialized")
    update.message.reply_text("Digite 6 digitos que te dou um link pra vc fapar >D")

    return CHECK_NUMBERS


def check_numbers(update, context):

    magic_numbers = update.message.text

    if magic_numbers.isdigit() and len(str(magic_numbers)) == 6:

        page = "https://nhentai.net/g/" + magic_numbers + "/"
        update.message.reply_text(page)
        update.message.reply_text("Deseja continuar? 'continue'/'end'")

        return ASK_CONTINUE

    else:
        update.message.reply_text("Invalid magic numbers")
        update.message.reply_text("Numeros de 6 digitos e sem letras")

        return CHECK_NUMBERS

def ask_continue(update, answer):

    answer = update.message.text
    if answer.lower() == 'continue':
        update.message.reply_text("OK, la vamos nós")
        update.message.reply_text("Digite os SEIS numerozinhos magicos")

        return CHECK_NUMBERS

    elif answer.lower() == 'end':
        update.message.reply_text("Até mais, fapador")

        return ConversationHandler.END


updater = Updater(TOKEN, use_context=True)

entregador = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    fallbacks=[],

    states={
        CHECK_NUMBERS: [MessageHandler(Filters.text, check_numbers)],
        ASK_CONTINUE: [MessageHandler(Filters.text, ask_continue)]

    },
)


entregador.add_handler(conv_handler)


updater.start_polling()
updater.idle()


