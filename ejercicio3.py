def cuenta(palabra,letra):
    contador = 0
    for letras in palabra:
        if letras == letra:
            contador = contador+1
    print(contador)

if __name__ == "__main__":
    palabra = input("Introduzca una palabra:")
    letra = input("Introduzca una letra que quiere colocar:")

    cuenta(palabra,letra)

