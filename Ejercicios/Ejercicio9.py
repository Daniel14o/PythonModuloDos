def iva(productos):
    """
    Se genera un diccionario con los nombres de los productos y los precios con IVA incluido.

    Conceptos aplicados: Dictionary comprehensions, acceso a valores de diccionario.

    Validaciones:
    - La entrada debe ser una lista.
    - Cada elemento debe ser un diccionario con claves 'nombre' y 'precio'.
    - 'precio' debe ser un número mayor o igual a 0.
    """
    if not isinstance(productos, list):
        raise ValueError("La entrada debe ser una lista de productos")

    for p in productos:
        if not isinstance(p, dict):
            raise ValueError("Cada producto debe ser un diccionario")
        if "nombre" not in p or "precio" not in p:
            raise ValueError("Cada producto debe tener las claves 'nombre' y 'precio'")
        if not isinstance(p["precio"], (int, float)) or p["precio"] < 0:
            raise ValueError("El precio debe ser un número mayor o igual a 0")

    return {i["nombre"]: round(i["precio"] * 1.19, 2) for i in productos}


if __name__ == "__main__":
    lista_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    precios_con_iva = iva(lista_productos)
    print("Precios con IVA:", precios_con_iva)
