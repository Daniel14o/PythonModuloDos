import random

def simulador_dados(lanzamientos: int = 10000) -> dict:
    """
    Simula el lanzamiento de dos dados 'lanzamientos' veces y
    cuenta la frecuencia de cada suma posible (2 a 12).

    Parámetros:
        lanzamientos (int): Número de veces que se lanzan los dados.

    Retorna:
        dict: Diccionario con las sumas como claves y su frecuencia como valores.

    Validaciones:
        - lanzamientos debe ser un entero mayor a 0.
    """
    if not isinstance(lanzamientos, int):
        raise ValueError("El número de lanzamientos debe ser un entero")
    if lanzamientos <= 0:
        raise ValueError("El número de lanzamientos debe ser mayor que cero")

    frecuencias = {}
    for _ in range(lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    return frecuencias

def reporte_frecuencias(frecuencias: dict) -> None:
    """
    Imprime un reporte con las frecuencias de cada suma.
    """
    print("Resultados:")
    for suma in range(2, 13):  # de 2 a 12
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")

if __name__ == "__main__":
    resultados = simulador_dados()
    reporte_frecuencias(resultados)
