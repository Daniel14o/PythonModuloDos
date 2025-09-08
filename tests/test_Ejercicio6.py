import pytest
from Ejercicios.Ejercicio6 import encontrar_indices

def test_encontrar_indices_letra_en_frase():
    frase = "Hola SENA"
    letra = "a"
    resultado = encontrar_indices(frase, letra)
    assert resultado == [3, 8]

def test_encontrar_indices_mayus_minus():
    frase = "Python PYTHON"
    letra = "p"
    resultado = encontrar_indices(frase, letra)
    assert resultado == [0, 7]

def test_encontrar_indices_sin_ocurrencias():
    frase = "Hola"
    letra = "z"
    resultado = encontrar_indices(frase, letra)
    assert resultado == []

def test_error_letra_multiple():
    with pytest.raises(ValueError, match="una unica letra valida"):
        encontrar_indices("Hola", "ab")

def test_error_letra_numero():
    with pytest.raises(ValueError, match="Una unica letra valida"):
        encontrar_indices("Hola", "3")

def test_error_letra_caracter_especial():
    with pytest.raises(ValueError, match="Una unica letra valida"):
        encontrar_indices("Hola", "!")

def test_error_frase_con_numeros():
    with pytest.raises(ValueError, match="La frase solo puede contener letras y espacios"):
        encontrar_indices("Hola1234567890", "a")

def test_error_frase_con_caracteres_especiales():
    with pytest.raises(ValueError, match="La frase solo puede contener letras y espacios"):
        encontrar_indices("Hola@,.-_{[]}+*´¨'?¿¡!#$%&/()=+~`^^<>", "a")