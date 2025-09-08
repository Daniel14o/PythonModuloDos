from typing import List

def validar_matriz(matriz: List[List[int]]):
    if not isinstance(matriz, list) or len(matriz) == 0:
        raise ValueError("La matriz debe ser una lista no vacía")
    for fila in matriz:
        if not isinstance(fila, list):
            raise ValueError("Cada fila debe ser una lista")
    longitudes = [len(fila) for fila in matriz]
    if len(set(longitudes)) != 1:
        raise ValueError("Todas las filas deben tener la misma longitud")

def transponer_matriz_for(matriz: List[List[int]]) -> List[List[int]]:
    validar_matriz(matriz)
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []

    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)

    return transpuesta

def transponer_matriz_comprehension(matriz: List[List[int]]) -> List[List[int]]:
    validar_matriz(matriz)
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6]]

    print("Matriz original:", matriz)
    print("Transpuesta en for:", transponer_matriz_for(matriz))
    print("Transpuesta con comprehension:", transponer_matriz_comprehension(matriz))
