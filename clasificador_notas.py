# Importamos el módulo random para generar calificaciones aleatorias
import random

# Lista de nombres de docentes registrados en el sistema
nombres = ["laura", "tommy", "angela"]

# Lista de códigos correspondientes a cada docente (índices coinciden con 'nombres')
codigos = ["0001", "0002", "0003"]

print("Bienvenid@ al sistema de calificación para docentes")
print(" ")

# Se solicita el nombre del docente
nombre = input("Por favor ingrese su nombre: ")

# Verificamos si el nombre está en la lista de docentes
if nombre in nombres:
    # Obtenemos el índice del docente (para comparar con su código)
    indice = nombres.index(nombre)
    
    # Contador de intentos para ingresar el código correcto
    contador = 0

    # Permitimos hasta 3 intentos
    while contador < 3:
        codigo = input("Ahora ingrese su código docente para validar credenciales: ")

        # Validamos que el código ingresado corresponda al docente
        if codigo == codigos[indice]:
            # Generamos 10 calificaciones aleatorias entre 1.0 y 10.0 con un decimal
            calificaciones = [round(random.uniform(1.0, 10.0), 1) for _ in range(10)]

            # Recorremos cada nota para clasificarla
            for nota in calificaciones:
                print(" ")
                print(f"Nota obtenida: {nota}")

                # Condicional para determinar el estado del estudiante
                if nota < 6.0:
                    print("Resultado: Has REPROBADO ")
                elif nota < 9.9:
                    print("Resultado: Has APROBADO ")
                else:
                    print("Resultado: EXCELENTE ")
            # Rompemos el bucle porque ya se validaron las credenciales
            break
        else:
            # Si el código es incorrecto, sumamos un intento
            contador += 1
            print(" Ha ocurrido un error en el sistema, código incorrecto.")

    # Si se completaron 3 intentos sin éxito
    if contador == 3:
        print(" Acceso denegado. Se acabaron los intentos.")

else:
    # Si el nombre no está en la lista de docentes
    print("Tu nombre no está en el sistema, por favor reinicia e intenta de nuevo.")

