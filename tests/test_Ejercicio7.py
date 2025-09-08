import pytest
from Ejercicios.Ejercicio7 import combinar_listas, generar_reporte

def test_combinar_listas_correcto():
    nombres = ["Ana", "Luis", "Maria"]
    notas = [4.5, 3.0, 5.0]
    esperado = {"Ana": 4.5, "Luis": 3.0, "Maria": 5.0}
    assert combinar_listas(nombres, notas) == esperado

def test_generar_reporte_correcto():
    estudiantes = {"Ana": 4.5, "Luis": 3.0}
    reporte = generar_reporte(estudiantes)
    assert "El estudiante Ana tiene una nota de 4.5" in reporte
    assert "El estudiante Luis tiene una nota de 3.0" in reporte

def test_error_listas_diferente_longitud():
    with pytest.raises(ValueError, match="misma longitud"):
        combinar_listas(["Ana", "Luis"], [4.5])

def test_error_nombres_invalidos():
    with pytest.raises(ValueError, match="solo letras"):
        combinar_listas(["Ana", "Luis123"], [4.5, 3.0])

def test_error_notas_invalidas():
    with pytest.raises(ValueError, match="entre 0 y 5"):
        combinar_listas(["Ana", "Luis"], [4.5, 6.0])