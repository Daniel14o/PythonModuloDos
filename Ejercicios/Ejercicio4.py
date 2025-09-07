"""
    Juego de Piedra, Papel o Tijeras contra la computadora:

    - El usuario elige una opción y la computadora elige una al azar.
    - El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
    - Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.

    Conceptos aplicados: random.choice(), bucle while, if/elif/else, contadores, f-strings.
    """
import random

def juego_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    victorias_jugador = 0
    victorias_computadora = 0

    print("Bienvenido al juego Piedra, Papel o Tijeras. El primero en llegar a 3 victorias gana")

    while victorias_jugador < 3 and victorias_computadora < 3:
        jugador = input("Elige piedra, papel o tijeras: ").lower()

        if jugador not in opciones:
            print("Opcion no valida, intenta de nuevo.")
            continue

        computadora = random.choice(opciones)
        print(f"Tú eliges: {jugador}")
        print(f"La computadora elige: {computadora}")

        if jugador == computadora:
            print("Empate.")
        elif (
            (jugador == "piedra" and computadora == "tijeras") or
            (jugador == "tijeras" and computadora == "papel") or
            (jugador == "papel" and computadora == "piedra")
        ):
            victorias_jugador += 1
            print("Ganaste esta ronda")
        else:
            victorias_computadora += 1
            print("La computadora gana esta ronda.")

        print(f"Marcador → Jugador: {victorias_jugador} | Computadora: {victorias_computadora}\n")

    if victorias_jugador == 3:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("La computadora gano el juego. ¡Suerte la próxima!")

# Ejecutar el juego
if __name__ == "__main__":
    juego_piedra_papel_tijeras()