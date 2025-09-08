import pytest
from unittest.mock import patch
from io import StringIO
from Ejercicios.Ejercicio13 import juego_aventura

def test_ganar_juego_desde_garaje():
    inputs = ["1", "1"]  # sala → garaje → encender carro
    with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as salida:
        juego_aventura()
        output = salida.getvalue().lower()
        assert "has escapado" in output
        assert "ganaste" in output

def test_perder_en_la_puerta():
    inputs = ["2"]  # sala → puerta → pierdes
    with patch("builtins.input", side_effect=inputs + ["1", "1"]), patch("sys.stdout", new_callable=StringIO) as salida:
        juego_aventura()
        output = salida.getvalue().lower()
        assert "has perdido" in output
        assert "vuelve a iniciar" in output

def test_opcion_invalida_en_sala():
    inputs = ["x", "1", "1"]  # sala → entrada inválida → sala → garaje → ganar
    with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as salida:
        juego_aventura()
        output = salida.getvalue().lower()
        assert "opción no válida" in output

def test_opcion_invalida_en_garaje():
    inputs = ["1", "x", "1"]  # sala → garaje → entrada inválida → garaje → ganar
    with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=StringIO) as salida:
        juego_aventura()
        output = salida.getvalue().lower()
        assert "opción no válida" in output  # Sin tilde si en tu código está así

