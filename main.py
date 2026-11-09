"""donde comienza el juego"""

from game import HangmanGame


def pedir_letra(intentadas):
    """pide una letra hasta que el jugador ingrese una válida"""
    while True:
        letra = input("Ingresa una letra: ").strip().lower()
        if len(letra) > 1:
            print("Ingresá una sola letra.\n")
        elif not letra.isalpha():
            print("Ingresa una letra.\n")
        elif letra in intentadas:
            print("Ya probaste esa letra, probá con otra.\n")
        else:
            return letra


def pedir_jugar_de_nuevo():
    """pregunta si quiere jugar otra vez hasta recibir si o no"""
    while True:
        respuesta = input("¿Querés jugar de nuevo? (y/n): ").strip().lower()
        if respuesta == "y":
            print()
            return True
        if respuesta == "n":
            print()
            return False
        print("Respondé 'y' o 'n'.\n")


def jugar_partida():
    juego = HangmanGame()
    intentadas = []  # todas las letras probadas, tanto aciertos como errores

    while not juego.is_won() and not juego.is_lost():
        juego.display_progress()
        print("Ya probaste: ", " ".join(intentadas))
        letra = pedir_letra(intentadas)
        intentadas.append(letra)
        print(juego.process_guess(letra) + "\n")  # salto de línea extra al final de cada intento

    # estado final del juego
    juego.display_progress()
    if juego.is_won():
        print("Ganaste! La palabra era:", juego.word)
    else:
        print("Perdiste! La palabra era:", juego.word)
    print("\n")


def main():
    while True:
        jugar_partida()
        if not pedir_jugar_de_nuevo():
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()