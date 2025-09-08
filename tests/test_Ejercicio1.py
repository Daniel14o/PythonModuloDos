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

# Casos inválidos

def test_estudiante_no_acepta_numero():
    with pytest.raises(TypeError):
        entradas(es_estudiante=10)

def test_no_vacios():
    with pytest.raises(TypeError):
        entradas("")

def test_edad_no_decimales():
    with pytest.raises(TypeError):
        entradas(edad=10.5)

def test_no_acepta_letras():
    with pytest.raises(TypeError):
        entradas("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def test_no_acepta_caracteres_especiales():
            with pytest.raises(TypeError):
                entradas("@!#$%&/()=?¡'¿¨´+*~}{][_-.,+")

def test_no_acepta_emojis():
            with pytest.raises(TypeError):
                entradas("😁")
