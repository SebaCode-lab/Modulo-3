# Definición de variables
suma = 0

# Bucle para leer los números
while True:
  numero = input("Ingrese un número (Enter para terminar): ")

  # Verificamos si el usuario desea finalizar el programa
  if numero == "":
    break

  # Validamos que el número sea válido
  try:
    numero = int(numero)
  except ValueError:
    print("El número ingresado no es válido.")
    continue

  # Sumamos el número
  suma += numero

# Imprimimos la suma
print("La suma es:", suma)
