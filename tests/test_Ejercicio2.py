import pytest
from Ejercicios.Ejercicio2 import consola

# PRUEBAS DE COMANDOS VÁLIDOS

def test_guardar():
    assert consola("Guardar")

def test_cargar():
    assert consola("Cargar")

def test_salir():
    assert consola("Salir")


# PRUEBAS DE COMANDOS INVÁLIDOS

def test_comando_invalido():
    assert consola("Otro")

def test_comando_vacio():
    assert consola("")

def test_comando_con_numeros():
    assert consola("1234567890")

def test_comando_con_caracteres_especiales():
    assert consola("$!#%&/()=?¡¿',.-_{}[]^~*+@|°")

def test_comando_con_emojis():
        assert consola("😎")