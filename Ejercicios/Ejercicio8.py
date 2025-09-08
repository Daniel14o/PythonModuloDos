from typing import List, Tuple

def procesar_lista(numeros: List[int]) -> Tuple[List[int], List[int], List[str], List[int]]:
    """
    Procesa una lista de números para generar:
    1. Una lista con solo los números positivos.
    2. Una lista con solo los números negativos.
    3. Una lista con los cuadrados de todos los números.
    4. Una lista de strings "positivo" o "negativo" para cada número.

    Parámetros:
        numeros (List[int]): Lista de números enteros.

    Retorna:
        Tuple[List[int], List[int], List[int], List[str]]:
            - Lista de positivos.
            - Lista de negativos.
            - Lista de cuadrados.
            - Lista de etiquetas "positivo"/"negativo".
    """
    # Validar que todos sean enteros
    for n in numeros:
        if not isinstance(n, int):
            raise ValueError("Solo numeros enteros")

    positivos = [n for n in numeros if n > 0]
    negativos = [n for n in numeros if n < 0]
    cuadrados = [n**2 for n in numeros]
    etiquetas = ["positivo" if n > 0 else "negativo" for n in numeros]

    return positivos, negativos, cuadrados, etiquetas


if __name__ == "__main__":
    lista_inicial: List[int] = [-5, 10, -15, 20, -25, 30]
    positivos, negativos, cuadrados, etiquetas = procesar_lista(lista_inicial)

    print("Numeros positivos:", positivos)
    print("Numeros negativos:", negativos)
    print("Cuadrados:", cuadrados)
    print("Etiquetas:", etiquetas)