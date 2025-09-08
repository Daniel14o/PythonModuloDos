import pytest
from unittest.mock import patch
from io import StringIO
from Ejercicios.Ejercicio14 import juego_ahorcado  # Reemplaza con el nombre real del módulo


def test_juego_ahorcado_completo():
    inputs = [
        " ",  # carácter vacío
        "3",  # número
        "@",  # especial
        "aa",  # más de una letra
        "a",  # correcta
        "a",  # repetida
        "x",  # incorrecta
        "g",  # correcta
        "t",  # correcta
        "o",  # correcta, gana
    ]

    with patch("builtins.input", side_effect=inputs), \
            patch("Ejercicios.Ejercicio14.modo_juego", return_value="gato"), \
            patch("sys.stdout", new_callable=StringIO) as salida:
        juego_ahorcado()
        output = salida.getvalue().lower()

        # Verificaciones clave
        assert "debes ingresar una sola letra" in output
        assert "ya intentaste esa letra" in output
        assert "error, la letra 'x' no está en la palabra." in output
        assert "bien, la letra 'a' está en la palabra." in output
        assert "adivinaste la palabra: gato" in output

