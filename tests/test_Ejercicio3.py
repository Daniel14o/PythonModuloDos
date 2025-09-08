import pytest
from Ejercicios.Ejercicio3 import Validar_claves


# PRUEBAS DE CONTRASEÑAS VALIDAS

def test_clave_valida():
    assert Validar_claves("Clave123") == "La contraseña es aceptable."



# PRUEBAS DE COMANDOS INVALIDOS


def test_clave_muy_corta():
    assert Validar_claves("Clav1") == "ERROR, la contraseña debe tener al menos 8 caracteres."

def test_clave_sin_mayuscula():
    assert Validar_claves("contrase1") == "ERROR, la contraseña debe contener al menos una mayuscula."

def test_clave_sin_numero():
    assert Validar_claves("Contrasena") == "ERROR, la contraseña debe contener al menos un numero."


def test_clave_vacia():
    with pytest.raises(ValueError, match="ERROR, la contraseña no puede estar vacia."):
        Validar_claves("")

def test_clave_solo_espacios():
    with pytest.raises(ValueError, match="ERROR, la contraseña no puede estar vacia."):
        Validar_claves("     ")

def test_clave_con_caracteres_especiales():
    with pytest.raises(ValueError, match="ERROR, la contraseña solo puede contener letras y numeros."):
        Validar_claves("Clave123!$!#%&/()=?¡¿',.-_{}[]^~*+@|°")