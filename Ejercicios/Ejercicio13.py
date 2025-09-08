def juego_aventura():
    print("Intenta escapar de la casa")
    print("Inicias en la sala de una casa de la que intentas escapar")
    print("Tu objetivo es encontrar la forma de salir.\n")

    habitacion = "sala"
    jugando = True

    while jugando:
        if habitacion == "sala":
            print("Te encuentras en la sala. ¿Qué camino eliges para intentar salir?")
            print(" 1. Ir al 'norte' hacia el garaje")
            print(" 2. Ir al 'este' hacia la puerta principal")
            accion = input("¿Qué haces? ").strip().lower()

            if accion == "1":
                habitacion = "garaje"
            elif accion == "2":
                habitacion = "puerta"
            else:
                print("Opción no válida. Intenta de nuevo.\n")

        elif habitacion == "garaje":
            print("\nHas entrado al garaje...")
            print("Hay un llavero con unas llaves en una mesa. Puedes:")
            print(" 1. 'Intentar prender el carro'")
            print(" 2. 'Intentar abrir la puerta principal'")
            accion = input("¿Qué haces? ").strip().lower()

            if accion == "1":
                print("\nSubes al carro...")
                print("Intentas encender el carro...")
                print("¡Te escuchan intentar prenderlo!")
                print("¡Pero logras encender el carro a tiempo!")
                print("Atraviesas la puerta del garaje con el carro...")
                print("¡Has escapado! ¡Ganaste!\n")
                jugando = False
            elif accion == "2":
                habitacion = "puerta"
            else:
                print("Opción no válida. Intenta de nuevo.\n")

        elif habitacion == "puerta":
            print("\nLlegaste a la puerta principal...")
            print("La puerta está cerrada con llave.")
            print("Intentas forzar la puerta...")
            print("Haces mucho ruido. Te descubren y te disparan.")
            print("Has perdido. Vuelve a iniciar el juego.\n")
            habitacion = "sala"
