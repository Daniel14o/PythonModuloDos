def Validar_claves(clave: str) -> str:
    """
    Escribe un programa que pida al usuario crear una contraseña y la valide usando un bucle while.
     El bucle solo terminará cuando la contraseña cumpla todos los criterios:

    - Mínimo 8 caracteres.
    - Que contenga al menos una letra mayúscula.
    - Que contenga al menos un número.

    Parámetros:
        contrasena (str): contraseña a validar.

    Retorna:
        str: "Contraseña válida." si cumple todas las reglas,
             o un mensaje con la primera regla incumplida.

        Conceptos aplicados: Bucle while True, if/elif/else, len(), métodos de string (isupper(),
         islower(), isdigit()), break.
    """
    if len(clave) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not any(c.isupper() for c in clave):
        return "La contraseña debe contener al menos una mayuscula."
    if not any(c.isdigit() for c in clave):
        return "La contraseña debe contener al menos un numero."
    return "Contraseña es aceptable."


if __name__ == "__main__":
    intentos=3
    while True:
        pwd = input("Cree una contraseña: ")
        resultado = Validar_claves(pwd)
        print(resultado)
        if resultado == "La contraseña es aceptable.":
            break

    while True:
        confirmar = input("Ingrese la clave: ")
        if pwd == confirmar:
            print("La clave correcta es correcta.")
            exit(0)
        else:
            print("La regla no se cumplio.")
            intentos= intentos-1
            print(f"Te quedan {intentos} intentos.")
        if intentos == 0:
            print("Te quedaste sin intentos.")
            exit(0)