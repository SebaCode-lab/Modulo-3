def palabras():
    # Lista donde almacenaremos los nombres de las ciudades
    palabras = []

    # Iniciamos un bucle infinito para capturar las entradas del usuario
    while True:
        try:            
            palabra = str(input("Ingrese una palabra o *** terminar: "))

            # Si el usuario ingresa "***", rompemos el bucle
            if palabra == "***":
                break

            # Si la ciudad no está en nuestra lista, la añadimos
            if palabra not in palabras:
                palabras.append(palabra)
        except ValueError:
            print("favor ingrese datos validos")

    # Ordenamos la lista de ciudades alfabéticamente
    palabras.sort()

    # Mostramos las ciudades ingresadas sin repetición y en orden alfabético
    print("\nCiudades ingresadas sin repetición y en orden alfabético:")
    for palabra in palabras:
        print(palabra)

# llamamos a la función main
palabras()