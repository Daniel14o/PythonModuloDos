import pytest
from Ejercicios.Ejercicio10 import transponer_matriz_for, transponer_matriz_comprehension

def test_transponer_matriz_for_correcta():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert transponer_matriz_for(matriz) == esperado

def test_transponer_matriz_comprehension_correcta():
    matriz = [[1, 2], [3, 4], [5, 6]]
    esperado = [[1, 3, 5], [2, 4, 6]]
    assert transponer_matriz_comprehension(matriz) == esperado

def test_error_matriz_vacia():
    with pytest.raises(ValueError, match="no vacía"):
        transponer_matriz_for([])

def test_error_filas_irregulares():
    with pytest.raises(ValueError, match="misma longitud"):
        transponer_matriz_for([[1, 2], [3]])

def test_error_elemento_no_lista():
    with pytest.raises(ValueError, match="debe ser una lista"):
        transponer_matriz_for([1, 2, 3])
