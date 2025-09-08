import pytest
from Ejercicios.Ejercicio9 import iva

def test_iva_correcto():
    productos = [
        {"nombre": "Camisa", "precio": 10000},
        {"nombre": "Zapatos", "precio": 20000},
    ]
    esperado = {"Camisa": 11900.0, "Zapatos": 23800.0}
    assert iva(productos) == esperado

def test_lista_vacia():
    assert iva([]) == {}

def test_error_no_lista():
    with pytest.raises(ValueError, match="lista de productos"):
        iva("Camisa")

def test_error_no_diccionario():
    with pytest.raises(ValueError, match="Debe ser un diccionario"):
        iva(["Camisa", "Pantalón"])

def test_error_faltan_claves():
    with pytest.raises(ValueError, match="Claves 'nombre' y 'precio'"):
        iva([{"nombre": "Camisa"}])

def test_error_precio_negativo():
    with pytest.raises(ValueError, match="Mayor o igual a 0"):
        iva([{"Nombre": "Camisa", "Precio": -5000}])