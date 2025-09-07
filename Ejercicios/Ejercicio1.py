def entradas(edad: int, es_estudiante: str) -> int:
    """
    Crea un programa que calcule el precio de una entrada de cine basándose en la edad del cliente y si es estudiante

    tarifas:
    - Niños (Menores de 12): $10,000
    - Jóvenes (12 a 17): $15,000
    - Adultos (Mayores de 18): $20,000
    - Si es estudiante, aplica 10% de descuento sobre el precio.

    Parámetros:
        edad (int): Edad del cliente (debe ser >= 0).
        es_estudiante (str): 'si' o 'no', indicando si es estudiante.

Conceptos aplicados: if/elif/else anidados, operadores lógicos (and, or), input(), int(), lower(), f-strings.

    Retorna:
        int: Precio final de la entrada.
    """
    if edad <= 0:
        raise ValueError("La edad no puede ser menor o igual a 0.")
    if edad < 12:
        precio = 10000
    elif edad <= 17:
        precio = 15000
    else:
        precio = 20000

    return int(precio * 0.9) if es_estudiante == "Si" else precio


if __name__ == "__main__":
    try:
        edad_usuario = int(input("Ingrese su edad: "))
        estudiante_usuario = input("¿Es estudiante? (Si/No): ").strip().lower().replace(" ", "")
        precio_final = entradas(edad_usuario, estudiante_usuario)
        print(f"El precio de la entrada es: ${precio_final}")
    except ValueError as e:
        print(f"Error: {e}")