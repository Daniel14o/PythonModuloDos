def encontrar_indices(frase: str, letra: str) -> list:
    """
    Devuelve una lista con las posiciones en las que aparece 'letra' dentro de 'frase'.
    Solo se permiten letras (no números ni caracteres especiales).
    No distingue entre mayúsculas y minúsculas.
    """
    if not letra.isalpha() or len(letra) != 1:
        raise ValueError("Solo se permite ingresar una letra")

    indices = []
    for i, caracter in enumerate(frase):
        if caracter.lower() == letra.lower():
            indices.append(i)
    return indices


if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    letra = input("Escribe una letra a buscar: ")

    try:
        resultado = encontrar_indices(frase, letra)
        print(f"La letra '{letra}' aparece en las posiciones: {resultado}")
    except ValueError as e:
        print(e)
