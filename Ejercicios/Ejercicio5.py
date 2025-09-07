def clasificar_numero(numero: int) -> str:
    """
    Clasificacion de numeros pares e inpares y si es múltiplo de 5 sale un mensaje adicional

    Parámetros:
        numero (int): Número a clasificar.

    Retorna:
        str: Texto indicando si es par o impar y si es múltiplo de 5.

        Conceptos aplicados: Operador ternario, operador módulo (%), if.
    """
    resultado: str = "Es par" if numero % 2 == 0 else "Es impar"
    if numero % 5 == 0:
        return f"{resultado} y múltiplo de 5"
    return resultado


if __name__ == "__main__":
    try:
        numero_ingresado: int = int(input("Ingrese un número: "))
        print(clasificar_numero(numero_ingresado))
    except ValueError:
        print("Debe ingresar un valor valido.")