from telegram.ext import Updater, CommandHandler
from comandos_bot import *
import metodos as met
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("prueba", prueba))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    #main()
    d_coor, d_magn, d_nom = met.leer_coord("Archivos/stars.txt")
    met.graficar_por_magnitud(d_coor, d_magn)
    met.graficar_constelacion("Archivos/constelaciones/OsaMayor.txt", d_nom, d_coor)
    met.plt.show()