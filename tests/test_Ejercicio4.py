import pytest
from unittest.mock import patch
from Ejercicios.Ejercicio4 import juego_piedra_papel_tijeras

# Test para validar que el juego termina cuando el jugador gana 3 veces
@patch('builtins.input', side_effect=["piedra", "piedra", "papel", "papel", "tijeras", "papel"])
@patch('random.choice', side_effect=["tijeras", "papel", "piedra", "tijeras", "papel", "piedra"])
def test_jugador_gana(mock_choice, mock_input, capsys):
    juego_piedra_papel_tijeras()
    salida = capsys.readouterr().out
    assert "¡Felicidades! Ganaste el juego." in salida

# Test para validar que el juego termina cuando la computadora gana 3 veces
@patch('builtins.input', side_effect=["piedra", "papel", "tijeras", "piedra", "papel", "tijeras"])
@patch('random.choice', side_effect=["papel", "tijeras", "piedra", "papel", "tijeras", "piedra"])
def test_computadora_gana(mock_choice, mock_input, capsys):
    juego_piedra_papel_tijeras()
    salida = capsys.readouterr().out
    assert "La computadora gano el juego. ¡Suerte la próxima!" in salida

# Test para validar entrada inválida
@patch('builtins.input', side_effect=["invalid", "piedra", "papel", "tijeras", "piedra", "papel", "tijeras"])
@patch('random.choice', side_effect=["papel", "tijeras", "piedra", "papel", "tijeras", "piedra"])
def test_entrada_invalida(mock_choice, mock_input, capsys):
    juego_piedra_papel_tijeras()
    salida = capsys.readouterr().out
    assert "Opcion no valida, intenta de nuevo." in salida


