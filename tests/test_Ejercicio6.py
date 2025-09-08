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
    with pytest.raises(ValueError, match="Solo se permite ingresar una letra"):
        encontrar_indices("Hola", "ab")


def test_error_letra_numero():
    with pytest.raises(ValueError, match="Solo se permite ingresar una letra"):
        encontrar_indices("Hola", "3")


def test_error_letra_caracter_especial():
    """Prueba que lanza ValueError si 'letra' es un caracter especial."""
    with pytest.raises(ValueError, match="Solo se permite ingresar una letra"):
        encontrar_indices("Hola", "!")

