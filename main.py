from telegram.ext import Updater, CommandHandler
from botCommands import *
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("prueba", prueba))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()