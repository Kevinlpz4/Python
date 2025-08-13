## Enunciado: 
## Crea un algoritmo que identifique si un numero es par o impar 

# Lista para almacenar los números ingresados por el usuario
numeros_ingresados = []

# Solicitar el nombre al usuario
nombre = input("Hola, por favor ingrese su nombre ")
print(" ")
print(f"Bienvenido al clasificador de números {nombre}")
print("A continuación el menú disponible")
print(" ")

# Bucle principal del programa (menú)
while True: 
    # Mostrar opciones del menú
    print("Menu")
    print("1. Clasificar un número")
    print("2. Listar los números ingresados")
    print("3. Salir del sistema")
    print(" ")
    
    # Solicitar opción al usuario con control de errores
    try:
        opcion = int(input("Por favor elija una opción "))
    except ValueError:  
        print(" Ingresa un número válido para el sistema")
        continue  # Regresa al inicio del menú
    
    print(" ")
    
    # Evaluar la opción elegida usando match-case (disponible desde Python 3.10)
    match opcion:
        case 1:
            # Bucle para clasificar múltiples números
            while True:
                try:
                    var_numero = int(input("Ahora por favor ingresa el número que deseas clasificar "))
                except ValueError:
                    print("Debes ingresar un número entero.")
                    print(" ") 
                    continue  # Vuelve a pedir el número si hay error
                
                # Guardar el número en la lista de historial
                numeros_ingresados.append(var_numero)
                
                # Calcular el residuo al dividir entre 2
                Residuo = var_numero % 2
                print(f"Su residuo es: {Residuo}")
                print(" ") 

                # Determinar si el número es par o impar
                if Residuo == 0: 
                    print(f"El número ingresado: ({var_numero}) es par")
                    print(" ") 
                else:
                    print(f"El número ingresado: ({var_numero}) es impar")  
                    print(" ")  

                # Preguntar si el usuario quiere ingresar otro número
                repetir = input("¿Quieres ingresar otro número? (S/N): ").lower()
                print(" ") 
                if repetir != "s":
                    break  # Salir del bucle de clasificación

        case 2:
            # Mostrar los números ingresados junto a su clasificación
            if numeros_ingresados:
                print("\nNúmeros ingresados:")
                print(" ") 
                for var_numero in numeros_ingresados:
                    tipo = "par" if var_numero % 2 == 0 else "impar"
                    print(f"- {var_numero} ({tipo})")
                    print(" ") 
            else: 
                print("No has ingresado ningún número hasta ahora")

        case 3:
            # Salir del sistema
            print("Saliendo del sistema")
            break

        case _:
            # Opción no válida
            print("Opción no válida")
            
# Mensaje final al salir del sistema
print(" ")
print("Gracias por usar nuestro sistema")
print(" ")
