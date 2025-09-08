from typing import List, Dict
import re
def combinar_listas(nombres: List[str], notas: List[float]) -> Dict[str, float]:
    """
    Combina dos listas en un diccionario {nombre: nota} con validaciones.

    Parámetros:
        nombres (List[str]): Lista de nombres de estudiantes.
        notas (List[float]): Lista de notas correspondientes.

    Retorna:
        Dict[str, float]: Diccionario con nombres como claves y notas como valores.

    Lanza:
        ValueError: Si las listas no tienen la misma longitud,
                    si algún nombre contiene caracteres no alfabéticos,
                    o si alguna nota está fuera del rango 0-5.
    """
    if len(nombres) != len(notas):
        raise ValueError("Las listas deben tener la misma longitud")

    for nombre in nombres:
        if not re.fullmatch(r"[A-Za-z]+", nombre):
            raise ValueError("Los nombres deben contener solo letras")

    for nota in notas:
        if not (0 <= nota <= 5):
            raise ValueError("Las notas deben estar entre 0 y 5")

    return dict(zip(nombres, notas))


def generar_reporte(estudiantes: Dict[str, float]) -> List[str]:
    """
    Genera un reporte a partir de un diccionario de estudiantes y notas.

    Parámetros:
        estudiantes (Dict[str, float]): Diccionario {nombre: nota}.

    Retorna:
        List[str]: Lista de frases con el formato "El estudiante [Nombre] tiene una nota de [Nota]".
    """
    return [
        f"El estudiante {nombre} tiene una nota de {nota}"
        for nombre, nota in estudiantes.items()
    ]


if __name__ == "__main__":
    nombres_ingresados: List[str] = input("Ingrese nombres separados por una coma: ").split(",")
    notas_ingresadas: List[float] = [float(x) for x in input("Ingrese notas separadas por una coma: ").split(",")]

    estudiantes = combinar_listas([n.strip() for n in nombres_ingresados], notas_ingresadas)
    for reporte in generar_reporte(estudiantes):
        print(reporte)
