## Enunciado:
## Crea un programa que reciba una lista de edades y diga si cada persona es:
## Niño (0 a 11)
## Adolescente (12 a 17)
## Adulto (18 a 59)
## Adulto mayor (60 en adelante)

# Mensaje inicial para el usuario
print("Bienvenid@ al Clasificador de Edades.")

# ---------------------------------------------------------
# FUNCIÓN 1: solicitar_edades
# ---------------------------------------------------------
def solicitar_edades(): 
    # Creamos una lista vacía donde guardaremos las edades
    edades = []
    
    # Repetimos el proceso 7 veces (i va de 0 a 6)
    for i in range(7):
        # Pedimos una edad al usuario.
        # El 'int()' convierte el texto ingresado a número entero.
        # El 'f' en el string permite insertar variables dentro del texto.
        edad = int(input(f"Ingrese la edad #{i + 1}: "))
        
        # Agregamos la edad a la lista usando append()
        edades.append(edad)
    
    # Devolvemos la lista completa de edades ingresadas
    return edades

# ---------------------------------------------------------
# FUNCIÓN 2: clasificar_edades
# ---------------------------------------------------------
def clasificar_edades(lista_edades):
    # Creamos una lista vacía para guardar el resultado de la clasificación
    clasificaciones = []
    
    # Recorremos cada edad en la lista que recibimos como parámetro
    for edad in lista_edades:
        
        # Clasificamos según el rango de la edad
        if edad < 12:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los niñ@s")
        
        elif edad > 11 and edad <= 17:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los adolescentes")
        
        elif edad >= 18 and edad <= 59:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los adultos")
        
        else:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los adultos mayores")    
    
    # Devolvemos la lista de clasificaciones como resultado final
    return clasificaciones

# ---------------------------------------------------------
# FLUJO PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# 1️ Llamamos a la función que solicita las edades y guardamos el resultado en edades_ingresadas
edades_ingresadas = solicitar_edades()

# 2️ Mostramos las edades ingresadas
# '\n' sirve para dejar una línea en blanco antes del texto
print("\nEdades ingresadas:", edades_ingresadas)

# 3️ Llamamos a la función clasificar_edades, pasándole la lista de edades como parámetro
# Guardamos el resultado (otra lista, pero con textos de clasificación) en clasificaciones_finales
clasificaciones_finales = clasificar_edades(edades_ingresadas)

# 4️ Imprimimos un título antes de mostrar la clasificación
print("\nClasificación de edades:")
print(" ")  # Línea vacía adicional para separar visualmente

# 5️ Recorremos cada elemento de la lista clasificaciones_finales
# 'clasificacion' es una variable temporal que en cada vuelta contiene un texto diferente
for clasificacion in clasificaciones_finales:
    # Imprimimos cada clasificación en su propia línea
    print(clasificacion)

