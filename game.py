"""contiene la lógica del juego"""


class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """muestra el estado actual del juego"""
        palabra = [letter if not letter.isalpha() or letter.lower() in self.guessed_letters else "_" for letter in self.word]
        print("Palabra:", " ".join(palabra))
        print("Errores:", self.errors)
        print("Intentos restantes:", self.max_errors - self.errors)
        return palabra

    def process_guess(self, letter):
        """procesa la letra ingresada por el jugador"""
        if letter in self.guessed_letters:
            return("Ya has ingresado esa letra.")
        elif letter in self.word.lower():       #aseguramos que la letra ingresada sea minúscula para compararla con la palabra
            self.guessed_letters.append(letter)
            return("Correcto!")
        else:
            self.errors += 1
            return("Incorrecto!")

    def is_won(self):
        """verifica si el jugador ha ganado el juego"""
        return all(not letter.isalpha() or letter.lower() in self.guessed_letters for letter in self.word)

    def is_lost(self):
        """verifica si el jugador ha perdido el juego"""
        return self.errors >= self.max_errors


if __name__ == "__main__":
    print("Test parcial del juego")
    game = HangmanGame()
    while game.errors < game.max_errors:
        if "".join(game.display_progress()) == game.word:
            break
        letter = input("Ingresa una letra: ").lower()
        if letter in game.word:
            game.guessed_letters.append(letter)
        else:
            game.errors += 1

    game.display_progress()
    palabra = "".join([letter if letter in game.guessed_letters else "_" for letter in game.word])
    print("Palabra:", palabra)  #imprime la palabra completa si se ha ganado el juego
    if game.errors == game.max_errors:
        print("Perdiste! La palabra era:", game.word)  #imprime la palabra completa si se ha perdido el juego
    else:
        print("¡Ganaste! La palabra era:", game.word)  #imprime la palabra completa si se ha ganado el juego
    print("Fin del juego.")  #imprime "Fin del juego." si se ha ganado el juego
