import pytest
from Ejercicios.Ejercicio11 import validar_cedula

def test_cedula_valida():
    # suma = 2+4+4+4 = 14 (par)
    assert validar_cedula("2444") == True

def test_cedula_no_valida_suma_impar():
    # suma = 1+2+3 = 6 (par), pero probemos suma impar
    assert validar_cedula("123") == True
    # suma impar ejemplo
    assert validar_cedula("111") == False

def test_cedula_con_caracteres_especiales():
    assert validar_cedula("1234abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ") == False
    assert validar_cedula("12$!#%&/()=?¡¿',.-_{}[]^~*+@|°34") == False

def test_cedula_con_espacios():
    assert validar_cedula(" 1234") == False
    assert validar_cedula("1234 ") == False
    assert validar_cedula("1 2 3 4") == False


def test_cedula_con_decimales():
    assert validar_cedula("123.45") == False
