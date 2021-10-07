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

# TOKEN = os.getenv('TELEGRAM_BOT_API')
TOKEN = '1962700368:AAHWnhQY_Q5O1O47o7x4JpEHW6TN5xCKRyY'
WHAT_DO, RANDOM_NHENTAI, CHECK_NUMBERS, ASK_CONTINUE = range(4)

def start(update, context):
    update.message.reply_text("nHentai bot initialized")
    update.message.reply_text("Diga o que fazer: \n"
                              "\n"
                              "'random' - para um hentai aleatorio \n"
                              "'manual' - para entrar um numero de hentai \n"
                              "'exit' - termina tudo \n")
    # update.message.reply_text("Digite 6 digitos que te dou um link pra vc fapar >D")

    return WHAT_DO

def what_do(update, usr_action):

    usr_action = update.message.text

    if usr_action == 'exit':
        update.message.reply_text("Ok, até mais")

        return ConversationHandler.END

    elif usr_action == 'random':
        update.message.reply_text("OK, te darei um nhentai random")

        return RANDOM_NHENTAI

    elif usr_action == 'manual':
        update.message.reply_text("Digite os numeros magicos")

        return CHECK_NUMBERS

def random_nhentai(update, magic_numbers):

    magic_numbers = str(random.randint(100000, 999999))

    page = "https://nhentai.net/g/" + magic_numbers + "/"
    update.message.reply_text(page)
    update.message.reply_text("Deseja continuar? 'continue'/'end'")

    return ASK_CONTINUE


def check_numbers(update, context):

    magic_numbers = update.message.text

    if magic_numbers.isdigit() and len(str(magic_numbers)) == 6:

        page = "https://nhentai.net/g/" + magic_numbers + "/"
        update.message.reply_text(page)
        update.message.reply_text("Deseja continuar?\n" 
                                  "\n"
                                  "'continue' para continuar \n"
                                  "'end' para finalizar \n")

        return ASK_CONTINUE

    else:
        update.message.reply_text("Invalid magic numbers")
        update.message.reply_text("Numeros de 6 digitos e sem letras")

        return CHECK_NUMBERS

def ask_continue(update, answer):

    answer = update.message.text
    if answer.lower() == 'continue':
        update.message.reply_text("OK, la vamos nós")
        update.message.reply_text("Diga o que fazer: \n"
                                  "\n"
                                  "'random' - para um hentai aleatorio \n"
                                  "'manual' - para entrar um numero de hentai \n"
                                  "'exit' - termina tudo \n")

        return WHAT_DO

    elif answer.lower() == 'end':
        update.message.reply_text("Até mais, fapador")

        return ConversationHandler.END


updater = Updater(TOKEN, use_context=True)

entregador = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    fallbacks=[],

    states={
        WHAT_DO: [MessageHandler(Filters.text, what_do)],
        RANDOM_NHENTAI: [MessageHandler(Filters.text, random_nhentai)],
        CHECK_NUMBERS: [MessageHandler(Filters.text, check_numbers)],
        ASK_CONTINUE: [MessageHandler(Filters.text, ask_continue)]

    },
)


entregador.add_handler(conv_handler)


updater.start_polling()
updater.idle()

