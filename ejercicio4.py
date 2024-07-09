def son_anagramas(palabra_1, palabra_2):
    try:
        # Esta función toma dos palabras y verifica si son anagramas.

        # Convertimos las palabras a minúsculas y luego a listas de letras
        palabra_1 = palabra_1.lower()
        palabra_2 = palabra_2.lower()

        # Verificar si las palabras contienen solo letras
        if not palabra_1.isalpha() or not palabra_2.isalpha():
            raise ValueError("¡Error! Ingresa solo letras, sin números ni caracteres especiales.")

        # Listas
        palabra_1 = list(palabra_1)
        palabra_2 = list(palabra_2)

        # Ordenamos las palabras
        palabra_1.sort()
        palabra_2.sort()

        # Comparamos las palabras ordenadas
        if palabra_1 == palabra_2:
            return "Las palabras son anagramas."
        else:
            return "Las palabras no son anagramas."

    except ValueError as e:
        return str(e)

# Solicitamos al usuario que ingrese las palabras
palabra_1 = input("Ingrese la primera palabra: ")
palabra_2 = input("Ingrese la segunda palabra: ")

# Llamamos a la función y mostramos el resultado
resultado = son_anagramas(palabra_1, palabra_2)
print(resultado)
