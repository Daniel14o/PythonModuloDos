import pytest
from Ejercicios.Ejercicio12 import simulador_dados

def test_simulacion_correcta():
    resultado = simulador_dados(1000)
    assert isinstance(resultado, dict)
    # Las claves deben estar entre 2 y 12
    assert all(2 <= k <= 12 for k in resultado.keys())
    # La suma total de frecuencias debe ser igual al número de lanzamientos
    assert sum(resultado.values()) == 1000

def test_error_lanzamientos_negativos():
    with pytest.raises(ValueError, match="mayor que cero"):
        simulador_dados(-10)

def test_error_lanzamientos_cero():
    with pytest.raises(ValueError, match="mayor que cero"):
        simulador_dados(0)

def test_error_caracteres_especiales():
    with pytest.raises(ValueError, match="entero"):
        simulador_dados("$!#%&/()=?¡¿',.-_{}[]^~*+@|°")

def test_error_string_vacio():
    with pytest.raises(ValueError, match="entero"):
        simulador_dados("")

def test_error_decimal():
    with pytest.raises(ValueError, match="entero"):
        simulador_dados(100.5)

def test_error_none():
    with pytest.raises(ValueError, match="entero"):
        simulador_dados(None)

def test_error_letras():
        with pytest.raises(ValueError, match="entero"):
            simulador_dados("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
