import pytest
from Ejercicios.Ejercicio2 import consola


# PRUEBAS DE COMANDOS VALIDOS


def test_guardar():
    assert consola("Guardar") == "Guardando archivo..."

def test_cargar():
    assert consola("Cargar") == "Cargando archivo..."

def test_salir():
    assert consola("Salir") == "Saliendo del programa..."



# PRUEBAS DE COMANDOS INVALIDOS


def test_comando_invalido():
    assert consola("otro") == "ERROR, Comando no reconocido."

def test_comando_vacio():
    with pytest.raises(ValueError, match= "ERROR, el comando no puede estar vacío."):
        consola("")

def test_comando_con_numeros():
    with pytest.raises(ValueError, match= "ERROR, el comando no puede contener numeros."):
        consola("1234567890")

def test_comando_con_caracteres_especiales():
    with pytest.raises(ValueError, match= "ERROR, el comando no puede contener caracteres especiales."):
        consola("$!#%&/()=?¡¿',.-_{}[]^~*+@|°")