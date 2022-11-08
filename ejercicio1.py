def cadenaInvertida():
    invertirCadena = ""
    while palabra:
        for letra in palabra:
            invertirCadena = letra + invertirCadena
        break

    print(invertirCadena)

if __name__ == "__main__":
    palabra = input("Introduzca una palabra:")
    cadenaInvertida()