import pytest
from Ejercicios.Ejercicio3 import Validar_claves


# PRUEBAS DE CONTRASEÑAS VALIDAS

def test_clave_valida():
    assert Validar_claves("Clave123")



# PRUEBAS DE COMANDOS INVALIDOS


def test_clave_muy_corta():
    assert Validar_claves("Clav1")

def test_clave_sin_mayuscula():
    assert Validar_claves("contrase1")

def test_clave_sin_numero():
    assert Validar_claves("Contrasena")


def test_clave_vacia():
    assert Validar_claves("")

def test_clave_solo_espacios():
    assert Validar_claves("     ")

def test_clave_con_caracteres_especiales():
       assert Validar_claves("Clave123!$!#%&/()=?¡¿',.-_{}[]^~*+@|°")