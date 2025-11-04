## Mostar la tabla de multiplicar que el usuario elija entre 1 y 10 

lnums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listaTablas = []
contador = 0 

print("\nSea bienvenido al sistemas de tablas de multiplicar")

while True: # Bucles principal del menu 
 
    print("\nMenu")
    print("1. Multiplicar")
    print("2. Tablas generadas")
    print("3. Salir")

    try:
        opcion = int(input("\nElige una opcion: "))
    except ValueError:
        print("Por favor ingresa un número válido (1, 2 o 3).")
        continue  # vuelve al inicio del while principal

    match opcion: 
        case 1:
            # aquí empieza el bloque case 1 encargado de la creacion de tablas
            while contador != 2: 
                tabla = []
                try:
                    num = int(input("\nElige el numero con el que deseas multiplicar (1-10): "))
                except ValueError:
                    print("Introduce un número válido.")
                    continue

                print(f"\nTabla del {num}:")
                print(" ")
                for i in lnums: # for desempaqueta cada numero de la lista 
                    resultado = num * i 
                    tabla.append(f"{num} x {i} = {resultado}")
                    print(f"{num} x {i} = {resultado}") 
                listaTablas.append((num, tabla)) # Aqui guardamos la lista de esta iteracion junto con el numero multiplicado como tupla 
                contador = int(input("\n¿Deseas generar otra tabla? (1 = sí, 2 = no): "))

        case 2:
            if not listaTablas:
                print("\nNo hay tablas alamacenadas")
            else: 
                print("\nListas alamacenadas")
                for num, tabla in listaTablas:
                    print(f"\nTabla del {num}: {tabla}")

        case 3:
            print("Gracias por usar nuestro sistema")
            break

        case _:
            print("Has ingresado una opcion no valida, por favor intente de nuevo") 

    salida = int(input("\nDeseas ir al menu principal o salir del programa? (1 = para menu, 2 = para salir): "))
    if salida == 2:
        print("Gracias por usar nuestro sistema")
        break

print("Hasta pronto... ")
