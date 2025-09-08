import pytest
from Ejercicios.Ejercicio1 import entradas

# --- Casos válidos ---
def test_nino_no_estudiante():
    assert entradas(10, "No") == 10000

def test_nino_estudiante():
    assert entradas(11, "Si") == 9000

def test_joven_no_estudiante():
    assert entradas(15, "No") == 15000

def test_joven_estudiante():
    assert entradas(17, "Si") == 13500

def test_adulto_no_estudiante():
    assert entradas(25, "No") == 20000

def test_adulto_estudiante():
    assert entradas(30, "Si") == 18000

# --- Casos inválidos ---
def test_edad_cero():
    with pytest.raises(ValueError, match=" ERROR, La edad no puede ser menor o igual a 0."):
        entradas(0, "Si")

def test_edad_negativa():
    with pytest.raises(ValueError):
        entradas(-5, "ERROR, la edad no puede ser negativa")

def test_edad_con_letras():
    with pytest.raises(ValueError):
        entradas("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ", "ERROR, No se permiten letras")

def test_edad_vacia():
    with pytest.raises(ValueError):
        entradas("", "ERROR, el campo de edad no puede estar vacio")

def test_edad_caracteres_especiales():
    with pytest.raises(ValueError):
        entradas("@,.-_{[]}+*´¨'?¿¡!#$%&/()=+~`^^<>", "ERROR, No se permiten caracteres especiales")

def test_estudiante_invalido_vacio():
    with pytest.raises(ValueError):
        entradas(20, "")

def test_estudiante_invalido_letras_raras():
    with pytest.raises(ValueError):
        entradas(20, "quizas")  