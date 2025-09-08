import pytest
from Ejercicios.Ejercicio15 import crear_tablero, colocar_barco, traducir_coordenada

def test_crear_tablero_dimensiones():
    tablero = crear_tablero()
    assert len(tablero) == 5
    assert all(len(fila) == 5 for fila in tablero)
    assert all(casilla == "~" for fila in tablero for casilla in fila)

def test_colocar_barco_posiciones_validas():
    barco = colocar_barco()
    assert len(barco) == 3
    for fila, col in barco:
        assert 0 <= fila < 5
        assert 0 <= col < 5

def test_traducir_coordenada_valida():
    assert traducir_coordenada("A1") == (0, 0)
    assert traducir_coordenada("E5") == (4, 4)
    assert traducir_coordenada("c3") == (2, 2)

def test_traducir_coordenada_invalida():
    assert traducir_coordenada("") is None
    assert traducir_coordenada("F1") is None
    assert traducir_coordenada("A0") is None
    assert traducir_coordenada("A6") is None
    assert traducir_coordenada("1A") is None
    assert traducir_coordenada("AA") is None
    assert traducir_coordenada("A") is None
    assert traducir_coordenada("A12") is None
