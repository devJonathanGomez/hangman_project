# Hangman (Ahorcado)

Juego del ahorcado en consola, escrito en Python. El programa elige una palabra al azar de una lista, y el jugador tiene que adivinarla letra por letra antes de quedarse sin intentos.

## Características

- Elige una palabra aleatoria desde `wordlist.txt`.
- Acepta palabras con espacios o guiones (por ejemplo `dos palabras` o `mother-in-law`); los espacios y guiones se muestran tal cual, sin pedir que los adivines.
- Compara en minúsculas: no importa si escribís la letra en mayúscula o minúscula, ni si la palabra secreta tiene mayúsculas.
- Muestra el progreso, los errores cometidos y los intentos restantes en cada turno.
- Valida la entrada: avisa si escribís más de una letra, algo que no es letra, o una letra que ya probaste.
- Al terminar una partida, pregunta si querés jugar de nuevo (`y` / `n`).

## Requisitos

- Python 3.6 o superior (no usa librerías externas).

## Cómo ejecutarlo

Desde la carpeta del proyecto:

```bash
python3 main.py
```

> ⚠️ **Advertencia:** ejecutá el juego desde la carpeta del proyecto, porque `utils.py` abre `wordlist.txt` con una ruta relativa.

## Cómo se juega

1. Se muestra la palabra con un `_` por cada letra oculta.
2. Ingresá una letra y presioná Enter.
3. Si la letra está en la palabra, se revela en todas sus posiciones. Si no está, suma un error.
4. Ganás si descubrís todas las letras antes de llegar a **6 errores**. Perdés si llegás a 6.
5. Al final se muestra la palabra secreta y podés elegir jugar otra partida.

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `main.py` | Punto de entrada. Contiene la interfaz de consola: pide letras, valida la entrada y controla las partidas. |
| `game.py` | Lógica del juego (clase `HangmanGame`): guarda las letras probadas, cuenta errores y decide si se ganó o se perdió. |
| `utils.py` | Funciones auxiliares, como `get_random_word()`, que lee `wordlist.txt` y devuelve una palabra al azar. |
| `wordlist.txt` | Lista de palabras posibles, una por línea. |

## Agregar palabras

Editá `wordlist.txt` y escribí una palabra por línea. Las líneas vacías no están contempladas, así que evitá dejarlas al final del archivo.

## Configuración

- La cantidad máxima de errores está definida en `HangmanGame.__init__` (`max_errors = 6`) dentro de `game.py`.
