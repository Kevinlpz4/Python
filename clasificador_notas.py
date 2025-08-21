## Enunciado: 
## Clasificar notas (aprobado/reprobado/excelente)

import random

nombres = ["laura", "tommy", "angela"]
codigos = ["0001", "0002", "0003"]

print("Bienvenid@ al sistema de calificación para docentes")
print(" ")

nombre = input("Por favor ingrese su nombre ")

if nombre in nombres: 
    indice = nombres.index(nombre)
    contador = 0 

    while contador < 3: 
        code = input("Ahora su codigo docente para validar credenciales ")

        if code == codigos[indice]:
            calificaciones = [round(random.uniform(1.0, 10.0), 1) for _ in range(10)]
            for nota in calificaciones:
                print(nota)
                if nota < 6.0:
                    print (f"Tu nota es de: ({nota}). Has Reprobado")
                elif nota >= 6.0 and nota < 9.9: 
                    print(f"Tu nota es de: ({nota}). Has Aprobado")
                else:
                    print(f"Tu nota es de: ({nota}). EXCELENTE !!")
            break        
        else: 
            contador += 1
            print("Ha ocurrido un error en el sistema")
    if contador == 3:
        print(" Acceso denegado. Se acabaron los intentos.")        
else: 
    print("Tu nombre no esta en el sistema, por favor reinicia e intenta de nuevo")
