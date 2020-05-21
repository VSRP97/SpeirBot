from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot_com import *
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("prueba", prueba))
    dispatcher.add_handler(CommandHandler("estrellas", estrellas))
    dispatcher.add_handler(CommandHandler("constelaciones", constelaciones))
    dispatcher.add_handler(CommandHandler("elegir_constelacion", elegir_constelacion))
    dispatcher.add_handler(CallbackQueryHandler(constelacion))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()