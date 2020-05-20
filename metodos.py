import matplotlib.pyplot as plt


def coords_a_pixel(cx, cy):
    v = 500
    y = cy * v + v
    x = cx * v + v
    return x, y


def leer_coord(direccion):
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
    axes = plt.gca()
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)
    axes.set_facecolor('black')
    #plt.axis("off")

    for i in coor:
        star_size = round(5.0 / magni[i] + 2)
        x, y = coords_a_pixel(coor[i][0], coor[i][1])
        plt.scatter(x, y, s=star_size, c='white')

def graficar_constelacion(direccion, nom: dict, coor: dict):
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
