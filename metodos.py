import matplotlib.pyplot as plt


def coords_a_pixel(cx, cy):
    """
    Adapta las coordenadas estelares a coordenadas cartesianas del primer cuadrante.

    :param cx: Coordenada x.
    :param cy: Coordenada y.
    :return: Tupla con las nuevas coordenadas x, y.
    """
    v = 500
    y = cy * v + v
    x = cx * v + v
    return x, y


def leer_coord(direccion: str):
    """
    Lee los datos del archivo de texto y los asigna a 3 directorios.

    :param direccion: String con la direccion del archivo de texto
    :return: Tupla de diccionarios (d_cord, d_magn, d_nom)
        d_cord - Contiene las coordenas de las estrellas con llaves Henry Draper.
        d_magn - Contiene las magnitudes de las estrellas con llaves Henry Draper.
        d_nom - Contiene los numeros Henry Draper con llaves de los nombres de las estrellas.
    """
    file = open(direccion, "r")
    d_cord = {}
    d_magn = {}
    d_nom = {}

    while True:
        line = file.readline()
        if not line:
            break
        datos = line.split()
        henry = datos[3]
        d_cord[henry] = (float(datos[0]), float(datos[1]))
        d_magn[henry] = float(datos[4])
        if len(datos) > 6:
            names = " ".join(datos[6:])
            names = names.split("; ")
            for i in names:
                d_nom[i] = henry
    return d_cord, d_magn, d_nom


def graficar_por_magnitud(coor: dict, magni: dict):
    """
    Grafica las estrellas con sus tamaños correspondientes.

    :param coor: Diccionario de coordenadas.
    :param magni: Diccionario de magnitudes.
    """
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)

    for i in coor:
        star_size = round(5.0 / magni[i] + 2)
        x, y = coords_a_pixel(coor[i][0], coor[i][1])
        plt.scatter(x, y, s=star_size, c='white')

def graficar_constelacion(direccion, nom: dict, coor: dict):
    """
    Grafica una constelación.

    :param direccion: String con la direccion del archivo de la constelación correspondiente.
    :param nom: Diccionario de nombres de estrellas.
    :param coor: Diccionario de coordenadas de estrellas.
    """
    file = open(direccion, "r")
    while True:
        line = file.readline()
        line = line.replace("\n", "")
        if not line:
            break
        arista = line.split(",")
        #Cambia los nombres por numeros Henry Draper
        arista[0] = nom[arista[0]]
        arista[1] = nom[arista[1]]
        origen = coords_a_pixel(coor[arista[0]][0], coor[arista[0]][1])
        destino = coords_a_pixel(coor[arista[1]][0], coor[arista[1]][1])
        x_coor = [origen[0], destino[0]]
        y_coor = [origen[1], destino[1]]
        plt.plot(x_coor, y_coor, c='yellow')

def build_menu(buttons, n_col, header_buttons=None, footer_buttons=None):
    """
    Crea un menú de Telegram.

    .. note:: Obtenido de https://github.com/python-telegram-bot/python-telegram-bot/wiki/
        Code-snippets#build-a-menu-with-buttons
    :param buttons: Lista de botones a colocar en el menú
    :param n_col: Número de columnas en el menú.
    :param header_buttons: Botones en el tope del menú.
    :param footer_buttons: Botones en el fondo del menú.
    :return: El menú.
    """
    menu = [buttons[i:i + n_col] for i in range(0, len(buttons), n_col)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu
