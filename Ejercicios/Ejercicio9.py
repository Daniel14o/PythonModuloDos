def iva(productos):
    """
     se genera un diccionario con los nombres de los productos y los precios con iva incluido

     Conceptos aplicados: Dictionary comprehensions, acceso a valores de diccionario.
    """
    return {i["nombre"]: round(i["precio"] * 1.19, 2) for i in productos}


if __name__ == "__main__":
    lista_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    precios_con_iva = iva(lista_productos)
    print("Precios con IVA:", precios_con_iva)