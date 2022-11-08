def cadenaInvertida():
    invertirCadena = ""
    while palabra:
        for letra in palabra:
            invertirCadena = letra + invertirCadena
            cadena = [invertirCadena]
            for x in cadena:
                print(x)
        break

if __name__ == "__main__":
    palabra = input("Introduzca una palabra:")
    cadenaInvertida()