## Enunciado: 
## Crea un algoritmo que identifique si un numero es par o impar 

numeros_ingresados = []

nombre = (input("Hola, por favor ingrese su nombre "))
print(" ")
print(f"Bienvenido al clasificador de numeros {nombre}")
print("A continuacion el menu, disponible")
print(" ")

while True: 
 print("Menu")
 print("1. Clasificar un numero")
 print("2. Listar los numeros ingresados")
 print("3. Salir del sistema")
 print(" ")
 
 try:
  opcion = int(input("Por favor elija una opcion "))
 except ValueError:  
  print(" Ingresa un numero valido para el sistema")
  continue
 
 print(" ")
 
 match opcion:
   case 1:
      while True:
       try:
        var_numero = int(input("Ahora por favor ingresa el numero que deseas clasificar "))
       except ValueError:
                print("Debes ingresar un número entero. ")
                print(" ") 
                continue
       
       numeros_ingresados.append(var_numero)
       residuo = var_numero % 2
       print (f"Su residuo es: {residuo}")
       print(" ") 

       if residuo == 0: 
          print(f"El numero ingresado: ({var_numero}) es par ")
          print(" ") 
       else:
          print(f"El numero ingresado: ({var_numero}) es impar ")  
          print(" ")  

       repetir = input("Quieres ingresar otro numero ? (S/N)").lower()
       print(" ") 
       if repetir != "s":
          break 

   case 2:  
      if numeros_ingresados: 
         print("\n Números ingresados: ")
         print(" ") 
         for var_numero in numeros_ingresados:
          tipo = "par" if var_numero % 2 == 0 else "impar"
          print(f"- {var_numero} ({tipo})")
          print(" ") 
      else: 
         print(" No has ingresado ningun numero hasta ahora")

   case 3: 
      print(" Saliendo del sistema")
      break

   case _: 
      print(" Opcion no valida")
      
print(" ")
print(" Gracias por usar nuestro sistema")
print(" ")












