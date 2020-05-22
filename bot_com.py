import metodos as met
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

d_coor, d_magn, d_nom = met.leer_coord("Archivos/stars.txt")


def start(update, context):
    """
    Envía una descripción de los comandos disponibles.

    :param update:
    :param context:
    """
    update.message.reply_text("<b>Comandos</b>\n"
                              "/estrellas - Recibe una imagen de todas las estrellas.\n"
                              "/constelaciones - Recibe una imagen de todas las constelaciones sobre las estrellas.\n"
                              "/elegir_constelacion - Abre un menú que permitirá seleccionar la constelación deseada y "
                              "recibir la imagen de esta sobre las estrellas."
                              , parse_mode=ParseMode.HTML)


def estrellas(update, context):
    """
    Metodo que manda a telegram una imagen con todas las estrellas.

    :param update:
    :param context:
    """
    met.graficar_por_magnitud(d_coor, d_magn)
    met.plt.axis('off')
    met.plt.savefig('stars.png', bbox_inches='tight', facecolor='black')

    chatid = update.effective_chat.id
    img = open('stars.png', 'rb')
    context.bot.send_photo(chat_id=chatid, photo=img)
    met.plt.clf()


def constelaciones(update, context):
    """
    Metodo que manda a telegram todas las estrellas y constelaciones en formato de imagen.

    :param update:
    :param context:
    """
    #Grafica las estrellas
    met.graficar_por_magnitud(d_coor, d_magn)
    #Lista de los nombres archivos de constelaciones
    allfiles = os.listdir("Archivos/constelaciones/")
    for i in allfiles:
        direccion = "Archivos/constelaciones/" + i
        #Grafica la constelación i.
        met.graficar_constelacion(direccion, d_nom, d_coor)
    met.plt.axis('off')
    met.plt.savefig('stars.png', bbox_inches='tight', facecolor='black')

    chatid = update.effective_chat.id
    img = open('stars.png', 'rb')
    context.bot.send_photo(chat_id=chatid, photo=img)
    met.plt.clf()


def elegir_constelacion(update, context):
    """
    Metodo que manda un menú con todas las constelaciones disponibles.

    :param update:
    :param context:
    """
    allfiles = os.listdir("Archivos/constelaciones/")
    #Lista de botones
    button_list = []
    for i in allfiles:
        text = i.replace(".txt", "")
        #Agrega boton de telegram a lista de botones
        button_list.append(InlineKeyboardButton(text, callback_data=i))
    #Crea menú de botones
    reply_markup = InlineKeyboardMarkup(met.build_menu(button_list, n_col=2))
    chatid = update.effective_chat.id
    #Manda el menú de botones
    context.bot.send_message(chat_id=chatid, text="Elija una constelación", reply_markup=reply_markup)


def constelacion(update, context):
    """
    De acuerdo a la constelación elegida en el menú, manda una imagen a telegram con todas las estrellas
        y la contelación seleccionada.
    """

    direccion = "Archivos/constelaciones/" + update.callback_query.data
    met.graficar_por_magnitud(d_coor, d_magn)
    met.graficar_constelacion(direccion, d_nom, d_coor)
    met.plt.axis('off')
    met.plt.savefig('stars.png', bbox_inches='tight', facecolor='black')

    chatid = update.effective_chat.id
    img = open('stars.png', 'rb')
    context.bot.send_photo(chat_id=chatid, photo=img)
    met.plt.clf()