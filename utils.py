"""funciones auxiliares como validar la entrada o mostrar el estado actual del juego"""

import random

def get_random_word():
    """obtiene una palabra aleatoria del archivo wordlist.txt"""
    with open("wordlist.txt", "r") as file:
        words = file.readlines()
        return random.choice(words).strip()  #elije una palabra y elimina el salto de línea con strip()

if __name__ == "__main__":
    print("Teste de obtener palabra aleatoria")
    for i in range(10):
        print(get_random_word())  #imprime 10 palabras aleatorias
