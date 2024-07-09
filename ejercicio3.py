# Construir el diccionario con los valores de las letras en Scrabble
puntajes = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def calcular_puntaje(palabra):
    puntaje = 0
    for letra in palabra:
        puntaje += puntajes.get(letra, 0)  # Obtener el puntaje de la letra, si no existe, asignar 0
    return puntaje

while True:
    try:
        # Pedir al usuario que ingrese una palabra
        palabra_usuario = input("Ingresa una palabra: ")

        # Convertir la palabra a minúsculas
        palabra_usuario = palabra_usuario.lower()

        # Verificar si la palabra contiene solo letras
        if not palabra_usuario.isalpha():
            raise ValueError("¡Error! Ingresa solo letras, sin números ni caracteres especiales.")

        # Calcular el puntaje de la palabra ingresada por el usuario
        puntaje_palabra = calcular_puntaje(palabra_usuario)

        # Mostrar el puntaje
        print(f"El puntaje de la palabra '{palabra_usuario}' en Scrabble es: {puntaje_palabra}")

        # Salir del bucle ya que la entrada fue válida
        break

    except ValueError as e:
        print(e)