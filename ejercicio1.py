def ordenar_numeros():
    # Inicializar una lista para almacenar los números
    numeros = []

    # Leer números hasta que se ingrese un 0
    while True:
        try:    
            numero = int(input("Ingrese un número (0 para finalizar): "))
            
            if numero == 0:
                break  # Salir del bucle si se ingresa 0
            else:
                numeros.append(numero)  # Agregamos a la lista

            # Si la lista tiene mas de 20 numeros se rompe el ciclo
            if len(numeros) >= 20:
                print("Ingresaste 20 o más números. A continuación, los mostraremos ordenados.")
                break
        
        except ValueError:
            print("Ingresa un número válido")
    return (numeros)

numeros = ordenar_numeros()

    # Validar que se hayan ingresado al menos 10 números
if len(numeros) < 10:
        print("Debes ingresar como mínimo 10 números. Intenta nuevamente.")
        numeros = ordenar_numeros() # llamamos a la funcion para comenzar desde 0

    # Ordenar la lista en orden descendente (de mayor a menor)
numeros.sort(reverse=True)

    # Mostrar los números ordenados sin incluir el 0
print("Números ordenados de mayor a menor (sin incluir el 0):")
for numero in numeros:
    print(numero)
