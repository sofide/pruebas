preguntas = ["Admitis que sofi te ama mas?",
             "vas a aprender a asar antes de que termine el 2012?",
             "vas a cocinarle a sofi con frecuencia?",
             "Amas a sofi mas que a cualquier otra mujer?",
             "Te gustaria tener MAS de un hijo con sofi?",
             "vas a dejar de hacerle cosquilas a sofi?",
             "sos feliz con sofi?",
             "vas a ver muchas series con sofi?",
             "Te gusta ver peliculas romanticas con Sofi?",
             "vas a aguantar a Sofi toda la vida",
             "Le vas a tener paciencia a sofi a pesar de todo?"]

import random


def dibujarMapa(mapa):
    """Dibuja el mapa

    mapa: mapa actual para dibujar"""
    print "Esta es tu posicion actual en el mapa"
    for linea in mapa:
        for elemento in linea:
            print elemento + "\t",
        print "\n"


def preguntar(preguntas):
    print "Antes de moverte deberas responder la siguiente pregunta"
    print random.choice(preguntas) + "\n" + "a. Si" + "\n" + "b. No"
    respuesta = raw_input()
    while respuesta != "a" and respuesta != "b":
        print "La respuesta ingresada no es valida. " \
              "Por favor ingrese nuevamente su respuesta"
        respuesta = raw_input()

    if respuesta == "a":
        print "Felicitaciones! Respondiste de forma correcta!" + "\n" + "presione enter para continuar"
        raw_input()
        print "Hacia donde te deseas mover?" + "\n" + "a. Arriba" + "\n" "b.Derecha"
        return raw_input()
    elif respuesta == "b":
        print  "Lo siento, esa no era la respuesta correcta... Con esa actitud, no podras conquistar a sofi"
        return "perdio"


def detectarPosicion(mapaActual, jugador):
    i = 0
    while i < len(mapaActual):
        j = 0
        while j < len(mapaActual[i]):
            if mapaActual[i][j] == jugador:
                posicion = [i, j]
                return posicion
            j = j + 1
        i = i + 1


def moverse(direccion, posicionActual, mapaActual, jugador):
    if direccion == "a":
        if posicionActual[0] == 0:
            print "No es posible moverse hacia arriba!" + "\n" + "Sera movido automaticamente hacia la derecha"
            return moverse("b", posicionActual, mapaActual, jugador)
        else:
            mapaActual[posicionActual[0]][posicionActual[1]] = "x"
            mapaActual[posicionActual[0] - 1][posicionActual[1]] = jugador
            return mapaActual

    elif direccion == "b":
        if posicionActual[1] == 3:
            print "no es posible moverse hacia abajo!" + "\n" "Sera movido automaticamente hacia arriba"
            return moverse("a", posicionActual, mapaActual, jugador)
        else:
            mapaActual[posicionActual[0]][posicionActual[1]] = "x"
            mapaActual[posicionActual[0]][posicionActual[1] + 1] = jugador
            return mapaActual
    else:
        print "la opcion ingresada no es correcta"
        return mapaActual


def jugar(preguntas):
    print "Bienvenido a este maravilloso juego!", "\n", "Para comenzar, por favor ingrese aqui su nombre (preferentemente en letras minusculas): ",
    jugador = raw_input()

    mapa = [["x", "x", "x", "sofi"], ["x", "x", "x", "x"],
            ["x", "x", "x", "x"], [jugador, "x", "x", "x"]]

    print "\n", "Ok, " + jugador,

    dibujarMapa(mapa)

    print " presione enter para continuar"

    raw_input()

    print "El objetivo del juego es superar los diferentes desafios para llegar hasta donde esta sofi y conquistarla!" + "\n" + "Debes pensar bien tus respuestas, ya que una vez elegida una opcion, no puedes dar marcha atras..."

    while detectarPosicion(mapa, jugador) != [0, 3]:
        respuesta = preguntar(preguntas)
        if respuesta == "perdio":
            print "volvelo a intentar!"
            jugar(preguntas)
            return
        dibujarMapa(moverse(respuesta, detectarPosicion(mapa, jugador), mapa, jugador))
    if jugador == "juan" or jugador == "fisa" or jugador == "fifi" or jugador == "fisa" or jugador == "ashton kutcher" or jugador == "roger federer":
        print "Felicitaciones! Lograste conquistar a Sofi!" + "\n" + "Si tus respuestas fueron sinceras, seguramente van a ser muy felices juntos para siempre!"
    else:
        print "Lo siento... Superaste todas las pruebas, pero no sos la persona que sofi esta esperando..."

jugar(preguntas)



