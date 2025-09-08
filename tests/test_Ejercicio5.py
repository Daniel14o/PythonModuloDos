import pytest
from Ejercicios.Ejercicio5 import clasificar_numero

# COMANDOS VÁLIDOS
def test_numero_par():
    assert clasificar_numero(8) == "Es par" # Es bueno verificar el resultado esperado

def test_numero_impar():
    assert clasificar_numero(7) == "Es impar"

def test_numero_multiplo_de_5_par():
    assert clasificar_numero(10) == "Es par y múltiplo de 5"

def test_numero_multiplo_de_5_impar():
    assert clasificar_numero(15) == "Es impar y múltiplo de 5"

def test_numero_cero():
    assert clasificar_numero(0) == "Es par y múltiplo de 5"


# COMANDOS INVÁLIDOS
def test_error_letra():
    with pytest.raises(TypeError, match="La entrada debe ser un número entero."):
        clasificar_numero("abcdefghijklmnñopqestuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def test_error_caracter_especial():
    with pytest.raises(TypeError, match="La entrada debe ser un número entero."):
        clasificar_numero("@,.-_{[]}+*´¨'?¿¡!#$%&/()=+~`^^<>")

def test_error_decimal():
    with pytest.raises(TypeError, match="La entrada debe ser un número entero."):
        clasificar_numero(3.5)