import pytest
from Ejercicios.Ejercicio8 import procesar_lista

def test_procesar_lista_correcto():
    numeros = [-5, 10, -15, 20]
    positivos, negativos, cuadrados, etiquetas = procesar_lista(numeros)

    assert positivos == [10, 20]
    assert negativos == [-5, -15]
    assert cuadrados == [25, 100, 225, 400]
    assert etiquetas == ["negativo", "positivo", "negativo", "positivo"]

def test_lista_vacia():
    positivos, negativos, cuadrados, etiquetas = procesar_lista([])
    assert positivos == []
    assert negativos == []
    assert cuadrados == []
    assert etiquetas == []

def test_error_lista_con_decimales():
    with pytest.raises(ValueError, match="Solo numeros enteros"):
        procesar_lista([1, 2.5, -3])
