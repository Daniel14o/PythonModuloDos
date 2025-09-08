import pytest
from Ejercicios.Ejercicio5 import clasificar_numero

#COMANDOS VALIDOS
def test_numero_par():
    assert clasificar_numero.clasificar_numero(8) == "Es par"

def test_numero_impar():
    assert clasificar_numero.clasificar_numero(7) == "Es impar"

def test_numero_multiplo_de_5_par():
    assert clasificar_numero.clasificar_numero(10) == "Es par y múltiplo de 5"

def test_numero_multiplo_de_5_impar():
    assert clasificar_numero.clasificar_numero(15) == "Es impar y múltiplo de 5"

def test_numero_cero():
    assert clasificar_numero.clasificar_numero(0) == "Es par y múltiplo de 5"


#COMANDOS INVALIDOS
def test_error_letra():
    with pytest.raises(TypeError):
        clasificar_numero.clasificar_numero("abcdefghijklmnñopqestuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ") == "ERROR, no se permiten letras"

def test_error_caracter_especial():
    with pytest.raises(TypeError):
        clasificar_numero.clasificar_numero("@,.-_{[]}+*´¨'?¿¡!#$%&/()=+~`^^<>") == "ERROR, no se permiten caracteres especiales"

def test_error_decimal():
    with pytest.raises(TypeError):
        clasificar_numero.clasificar_numero(3.5) == "ERROR, no se permiten numeros decimales"