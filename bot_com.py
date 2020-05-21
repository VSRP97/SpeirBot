import metodos as met
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

d_coor, d_magn, d_nom = met.leer_coord("Archivos/stars.txt")


def start(update, context):
    update.message.reply_text("Hola mundo.")


def prueba(update, context):
    nombre = update.message.chat.first_name
    mensaje = "Bienvenido, {}".format(nombre)
    update.message.reply_text(mensaje)


def estrellas(update, context):
    """
    Metodo que manda a telegram una imagen con todas las estrellas.

    :param update:
    :param context:
    """
    met.plt.clf()
    met.graficar_por_magnitud(d_coor, d_magn)
    met.plt.axis('off')
    met.plt.savefig('stars.png', bbox_inches='tight', facecolor='black')

    chatid = update.effective_chat.id
    img = open('stars.png', 'rb')
    context.bot.send_photo(chat_id=chatid, photo=img)


def constelaciones(update, context):
    """
    Metodo que manda a telegram todas las estrellas y constelaciones en formato de imagen.

    :param update:
    :param context:
    """
    met.plt.clf()
    met.graficar_por_magnitud(d_coor, d_magn)
    allfiles = os.listdir("Archivos/constelaciones/")
    for i in allfiles:
        direccion = "Archivos/constelaciones/" + i
        met.graficar_constelacion(direccion, d_nom, d_coor)
    met.plt.axis('off')
    met.plt.savefig('stars.png', bbox_inches='tight', facecolor='black')

    chatid = update.effective_chat.id
    img = open('stars.png', 'rb')
    context.bot.send_photo(chat_id=chatid, photo=img)


def elegir_constelacion(update, context):
    """
    Metodo que manda un menú con todas las constelaciones disponibles.

    :param update:
    :param context:
    """
    allfiles = os.listdir("Archivos/constelaciones/")
    button_list = []
    for i in allfiles:
        text = i.replace(".txt","")
        button_list.append(InlineKeyboardButton(text, callback_data=i))
    reply_markup = InlineKeyboardMarkup(met.build_menu(button_list, n_col=2))
    chatid = update.effective_chat.id
    context.bot.send_message(chat_id=chatid, text="Elija una constelación", reply_markup=reply_markup)

def constelacion(update, context):
    """
    De acuerdo a la constelación elegida en el menú, manda una imagen a telegram con todas las estrellas
        y la contelación seleccionada.

    :rtype: object
    """
    met.plt.clf()
    direccion = "Archivos/constelaciones/"+update.callback_query.data
    met.graficar_por_magnitud(d_coor, d_magn)
    met.graficar_constelacion(direccion, d_nom, d_coor)
    met.plt.axis('off')
    met.plt.savefig('stars.png', bbox_inches='tight', facecolor='black')

    chatid = update.effective_chat.id
    img = open('stars.png', 'rb')
    context.bot.send_photo(chat_id=chatid, photo=img)



