def generar_combinaciones(palabras, combinacion_actual=[], usadas=set()):
    # Si hemos usado todas las palabras, mostramos la combinación
    if len(usadas) == len(palabras):
        print(" -> ".join(combinacion_actual))
        return

    for i, palabra in enumerate(palabras):
        if i in usadas:
            continue  # Saltar palabras ya usadas

        if combinacion_actual and combinacion_actual[-1][0] == palabra[0]:
            continue  # Evitar palabras con la misma letra inicial consecutiva

        # Agregar la palabra a la combinación
        combinacion_actual.append(palabra)
        usadas.add(i)

        # Llamado recursivo para continuar con la combinación
        generar_combinaciones(palabras, combinacion_actual, usadas)

        # ***BACKTRACKING: Deshacemos la última decisión***
        combinacion_actual.pop()
        usadas.remove(i)

# Prueba con palabras
palabras = ["gato", "perro", "gallina", "oso"]
generar_combinaciones(palabras)
