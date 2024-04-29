#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cifradoHill import *


def inicio():
    """ Funcion inicio, pregunta que funcion requiere hacer (encriptar, desencriptar)

    Args:
        No requiere argumentos

    Returns:
        Retorna un numero entero, esperado sea 1 o 2
    """
    print(
        """
  ____ _  __               _           _      _   _ _ _ _ 
 / ___(_)/ _|_ __ __ _  __| | ___   __| | ___| | | (_) | |
| |   | | |_| '__/ _` |/ _` |/ _ \ / _` |/ _ \ |_| | | | |
| |___| |  _| | | (_| | (_| | (_) | (_| |  __/  _  | | | |
 \____|_|_| |_|  \__,_|\__,_|\___/ \__,_|\___|_| |_|_|_|_|
        """
    )
    print(
        "El cifrado Hill fue propuesto por Lester S. Hill en 1929 y es un criptosistema que se basa en emplear una matriz como clave para cifrar un texto en claro y su inversa para descifrar el criptograma correspondiente.\n")

    inicio = input("Ingrese el numero: \n 1 para encriptar \n 2 para desencriptar: \n Respuesta: ")

    try:
        inicio = int(inicio)
    except:
        inicio = 0

    return inicio


def validarOpcion(respuesta):
    """ Valida opcion de respuesta del usuario

    Args:
        respuesta ( int ): Espera un numero entero

    Returns:
        str : Entrega mensaje de confirmacion
    """
    if respuesta == 1:

        dimension = input("Ingrese la dimension de la matriz llave: ")

        try:
            llave = matriz_llave(int(dimension))
            frase = input("Ingrese una frase: ")
            textoencriptado = encriptar(frase, llave)
            print("\n Llave utilizada: \n \n", llave.tolist())
            print(f"\n Texto encriptado: '{textoencriptado}'")
            resultado = "\n Finalizo proceso --> encriptar \n "

        except:

            resultado = True

    elif respuesta == 2:

        llave = input("Ingrese la matriz llave: ")
        frase = input("Ingrese el valor encriptado: ")

        try:

            llave = convertirStraList(llave)
            desencriptado = desencriptar(frase, llave)
            print(f"\n Texto desencriptado: '{desencriptado}'")

        except:

            print("No Ingreso los datos correctamente ...")

        resultado = "\n Finalizo proceso  --> desencriptar \n "

    elif respuesta == 0 or respuesta > 2:

        resultado = "No ingreso una opcion valida ... "

    else:

        resultado = "No ingreso una opcion valida ... "

    return resultado


def convertirStraList(lista):
    """ Convertir String a Lista

    Args:
        lista ( str ): Espera una cadena string

    Returns:
        list : Retorna una lista
    """
    lista = lista[1:-1].split(", ")

    l = []
    lf = []

    for x in lista:

        try:

            x = int(x)
            l.append(x)

        except:

            if x[0] == "[":

                x = x[1:]
                l.append(int(x))

            elif x[-1] == "]":

                x = x[:-1]
                l.append(int(x))
                lf.append(l)
                l = []

    return lf


def main():
    """ Funcion principal
    """
    respuesta = inicio()
    respuestaOpcion = validarOpcion(respuesta)

    if respuestaOpcion == True:

        print(" \n Ingrese un valor numerico \n")
        main()

    else:

        print(respuestaOpcion)


if __name__ == '__main__':
    main()
