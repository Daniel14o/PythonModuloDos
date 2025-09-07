def juego_aventura():
    print("Intenta escapar de la casa")
    print("Inicias en la sala de una casa de la que intentas escapar")
    print("Tu objetivo es encontrar la forma de salir.\n")

    habitacion = "sala"
    jugando = True

    while jugando:
        if habitacion == "sala":
            print("Te encuentras en la sala, que camino eliges para intentar salir:")
            print(" 1 Ir al 'norte' hacia el garaje")
            print(" 2 Ir al 'este' hacia la puerta principal")
            accion = input("¿Qué haces? ").lower()

            if accion == "1":
                habitacion = "garaje"
            elif accion == "2":
                habitacion = "puerta"
            else:
                print("Opcion no valida.")

        elif habitacion == "Garaje":
            print("\nHas entrado al garaje...")
            print("Hay un llavero con unas llaves en una mesa. Puedes:")
            print(" 1 'Intentar prender el carro'")
            print(" 2 'Intentar abrir la puerta principal'")
            accion = input("¿Qué haces? ").lower()

            if accion == "1":
                print("\nSubes al carro...")
                print("Intentas encender el carro...")
                print("Te escuchan intentar prenderlo...")
                print("logras encender el carro a tiempo...")
                print("Atraviesas la puerta del garaje con el carro...")
                print("\Has escapado Ganaste")
                jugando = False
            elif accion == "2":
                habitacion = "Puerta"
            else:
                print("Opcion no valida.")

        elif habitacion == "Puerta":
            print("\nllegaste a la puerta...")
            print("la puerta esta cerrada con llave.")
            print("Intentas forzar la puerta...")
            print("Haces mucho ruido te descubren y te disparan. Has perdido")
            print("Vuelve a iniciar el juego\n")
            habitacion="Sala"


if __name__ == "__main__":
    juego_aventura()