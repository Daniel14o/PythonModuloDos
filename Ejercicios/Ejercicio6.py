def encontrar_indices(frase: str, letra: str) -> list:
    """
    Devuelve una lista con las posiciones en las que aparece 'letra' dentro de 'frase'.
    Solo se permiten letras (no números ni caracteres especiales).
    """
    if not letra.isalpha() or len(letra) != 1:
        print("Solo se permite ingresar una letra (no numeros ni caracteres especiales).")
        exit()  # Finaliza el programa inmediatamente

    indices = []
    for i, caracter in enumerate(frase):
        if caracter.lower() == letra.lower():
            indices.append(i)
    return indices


# Programa principal
if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    letra = input("Escribe una letra a buscar: ")

    resultado = encontrar_indices(frase, letra)
    print(f"La letra '{letra}' aparece en las posiciones: {resultado}")