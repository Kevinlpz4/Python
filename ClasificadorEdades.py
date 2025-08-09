## Enunciado:
## Crea un programa que reciba una lista de edades y diga si cada persona es:
## Niño (0 a 11)
## Adolescente (12 a 17)
## Adulto (18 a 59)
## Adulto mayor (60 en adelante)

print ("Bienvenid@ al Clasficador de Edades.")

def solicitar_edades(): 
    edades = []
    for i in range(7):
        edad = int(input(f"Ingrese la edad #{i + 1}: "))
        edades.append(edad)
    return edades
    
def clasificar_edades(lista_edades):
    clasificaciones = []  # Aquí guardaremos los textos
    for edad in lista_edades:
        if edad < 12:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los niñ@s")
        elif edad > 11 and edad <= 17:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los adolescentes")
        elif edad >= 18 and edad <= 59:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los adultos")
        else:
            clasificaciones.append(f"{edad} años: Pertenece al grupo de los adultos mayores")            
    return clasificaciones

# Flujo principal
edades_ingresadas = solicitar_edades()
print("\nEdades ingresadas:", edades_ingresadas)

clasificaciones_finales = clasificar_edades(edades_ingresadas)

print("\nClasificación de edades:")
for clasificacion in clasificaciones_finales:
    print(clasificacion)
