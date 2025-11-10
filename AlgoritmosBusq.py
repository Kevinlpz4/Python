# ==========================
#   IMPLEMENTAR BÚSQUEDA VORAZ Y A*
# ==========================

# Lista global para guardar rutas
rutas = [ ]

# -----------------------------
#  GRAFO PRINCIPAL (distancias)
# -----------------------------

# Se crea un diccionarioa anidado en el cual guarda cada ciudad como otro diccionario donde tienen la su conexion de cada nodo por clave:valor
grafo = { 
    "Bilbao" : {"Huesca": 371, "Logroño": 136, "Burgos": 158}, 
    "Burgos" : {"Bilbao": 158, "Logroño": 132, "Madrid": 249},
    "Logroño" : {"Bilbao": 136, "Huesca": 239, "Zaragoza": 170, "Soria": 100, "Burgos": 132},
    "Huesca" : {"Tarragona": 212, "Zaragoza": 74, "Logroño": 239, "Bilbao": 371},
    "Soria" : {"Logroño": 100, "Guadalajara": 170, "Madrid": 231},
    "Zaragoza" : {"Huesca": 74, "Tarragona": 236, "Teruel": 170, "Guadalajara": 256, "Logroño": 170},
    "Tarragona" : {"Castellon": 187, "Zaragoza": 236, "Huesca": 212},
    "Madrid" : {"Burgos": 249, "Soria": 231, "Guadalajara": 62, "Cuenca": 165},
    "Guadalajara" : {"Soria": 170, "Zaragoza": 256, "Teruel": 244, "Cuenca": 136, "Madrid": 62}, 
    "Teruel" : {"Zaragoza": 170, "Castellon": 144, "Guadalajara": 244},
    "Castellon" : {"Tarragona": 187, "Valencia": 73, "Teruel": 144},
    "Cuenca" : {"Valencia": 199, "Madrid": 165, "Guadalajara": 136},
    "Valencia" : {"Castellon": 73, "Cuenca": 199},
}

# Normalizamos todo el grafo a minúsculas
grafo = {
    ciudad.casefold(): {vecino.casefold(): distancia for vecino, distancia in conexiones.items()}
    for ciudad, conexiones in grafo.items()
}

# -----------------------------
#  HEURÍSTICA VORAZ
# -----------------------------

# Se replica el diccionario numero 1 pero esta vez con sus equivalencias en euristica para el metodo voraz
heuristicaVoraz = {
    "Bilbao" : {"Huesca": 242, "Logroño": 97, "Burgos": 119}, 
    "Burgos" : {"Bilbao": 119, "Logroño": 103, "Madrid": 214},
    "Logroño" : {"Bilbao": 97, "Huesca": 172, "Zaragoza": 157, "Soria": 77, "Burgos": 103},
    "Huesca" : {"Tarragona": 177, "Zaragoza": 67, "Logroño": 172, "Bilbao": 242},
    "Soria" : {"Logroño": 77, "Guadalajara": 138, "Madrid": 182},
    "Zaragoza" : {"Huesca": 67, "Tarragona": 187, "Teruel": 146, "Guadalajara": 221, "Logroño": 157},
    "Tarragona" : {"Castellon": 167, "Zaragoza": 187, "Huesca": 177},
    "Madrid" : {"Burgos": 214, "Soria": 182, "Guadalajara": 51, "Cuenca": 138},
    "Guadalajara" : {"Soria": 138, "Zaragoza": 221, "Teruel": 176, "Cuenca": 106, "Madrid": 51}, 
    "Teruel" : {"Zaragoza": 146, "Castellon": 98, "Guadalajara": 176},
    "Castellon" : {"Tarragona": 167, "Valencia": 63, "Teruel": 98},
    "Cuenca" : {"Valencia": 164, "Madrid": 138, "Guadalajara": 106},
    "Valencia" : {"Castellon": 63, "Cuenca": 164},
}

# Normalizamos heurística voraz a minusculas
heuristicaVoraz = {
    ciudad.casefold(): {vecino.casefold(): valor for vecino, valor in conexiones.items()}
    for ciudad, conexiones in heuristicaVoraz.items()
}

# -----------------------------
#  HEURÍSTICA A*
# -----------------------------

# Se crea un 3er diccionario con la heuristca de cada ciudad hasta meta(Valencia).
heuristicaA = {
    "Bilbao" : {"Valencia": 473}, 
    "Burgos" : {"Valencia": 424},
    "Logroño" : {"Valencia": 375},
    "Huesca" : {"Valencia": 296},
    "Soria" : {"Valencia": 311},
    "Zaragoza" : {"Valencia": 246},
    "Tarragona" : {"Valencia": 229},
    "Madrid" : {"Valencia": 302},
    "Guadalajara" : {"Valencia": 270}, 
    "Teruel" : {"Valencia": 115},
    "Castellon" : {"Valencia": 63},
    "Cuenca" : {"Valencia": 164},
    "Valencia" : {"Valencia": 0},
}

# Normalizamos heurística A* a minusculas
heuristicaA = {
    ciudad.casefold(): {vecino.casefold(): valor for vecino, valor in conexiones.items()}
    for ciudad, conexiones in heuristicaA.items()
}

# ======================================================
# FUNCIÓN DE BÚSQUEDA VORAZ
# ======================================================

def busquedaVoraz(grafo, heuristicaVoraz, inicio, meta, rutas):
    actual = inicio                     # Nodo actual donde empieza la búsqueda
    camino = [actual]                   # Lista con el recorrido del camino
    heuristicas_camino = []             # Guarda los valores heurísticos de cada paso
    visitados = set([actual])           # Registra las ciudades ya visitadas para no repetirlas

    while actual != meta:               # Mientras no se llegue al destino...
        print(f"\nEstoy en {actual}")
        mejor_vecino = None
        mejor_h = float("inf")          # Valor inicial muy grande (representa infinito)

        # Recorremos todos los vecinos del nodo actual
        for vecino, distancia in grafo[actual].items():
            if vecino in visitados:     # Evita devolverse o visitar nodos ya recorridos
                continue

            # Obtiene la heurística hacia ese vecino
            hv = heuristicaVoraz[actual].get(vecino, float("inf"))
            print(f"{vecino} → Distancia: {distancia} | Heurística: {hv}")

            # Escoge el vecino con menor valor heurístico
            if hv < mejor_h:
                mejor_h = hv
                mejor_vecino = vecino

        if mejor_vecino is None:        # Si no hay vecinos válidos, se detiene
            print("No hay vecinos válidos para continuar.")
            break

        # Se muestra la elección hecha
        print(f"Elijo avanzar hacia {mejor_vecino} con heurística {mejor_h}")

        # Avanza al siguiente nodo
        actual = mejor_vecino
        camino.append(actual)           # Añade el vecino al camino
        heuristicas_camino.append(mejor_h)  # Guarda la heurística usada
        visitados.add(actual)           # Marca el nodo como visitado

        if actual == meta:              # Si llega al destino, termina el bucle
            print("\n¡Meta alcanzada!")
            break

    # Muestra los resultados finales
    print("\n=== RESULTADOS DE LA BÚSQUEDA VORAZ ===")
    print("Camino encontrado:", " → ".join(camino))
    print("Heurísticas de cada paso:", heuristicas_camino)
    print("Suma total de heurísticas:", sum(heuristicas_camino))

    # Guarda los resultados en la lista global de rutas
    total = sum(heuristicas_camino)
    rutas.append((camino.copy(), heuristicas_camino.copy(), total))

    return camino, heuristicas_camino

# ======================================================
# FUNCIÓN DE BÚSQUEDA A*
# ======================================================

def busqueda_A(grafo, heuristicaA, inicio, meta, rutas):
    actual = inicio
    camino = [actual]                       # Lista del recorrido
    acumulado = [0]                         # g(n): costo real acumulado desde el inicio
    heuristicas = [heuristicaA.get(actual, {}).get(meta, float("inf"))]  # h(n) inicial
    visitados = set([actual])               # Nodos visitados

    while actual != meta:                   # Bucle principal hasta llegar a la meta
        print(f"\nEstoy en: {actual}")
        mejor_vecino = None
        mejor_f = float("inf")              # f(n) = g(n) + h(n)
        mejor_g = None
        mejor_h = None

        # Explora todos los vecinos del nodo actual
        for vecino, distancia in grafo[actual].items():
            if vecino in visitados:         # Evita repetir nodos
                continue

            g = acumulado[-1] + distancia   # Suma el costo acumulado más la distancia al vecino
            h = heuristicaA.get(vecino, {}).get(meta, float("inf"))  # Heurística del vecino
            f = g + h                       # Costo total estimado

            print(f"Vecino {vecino}: g = {g}, h = {h}, f = {f}")

            # Selecciona el vecino con el valor f más bajo
            if f < mejor_f:
                mejor_f = f
                mejor_vecino = vecino
                mejor_g = g
                mejor_h = h

        if mejor_vecino is None:            # Si no hay vecinos válidos, termina
            print("No hay más vecinos disponibles. No se encontró un camino.")
            return camino, acumulado, heuristicas

        # Se muestra el movimiento elegido
        print(f"Elijo avanzar hacia {mejor_vecino} con f(n) = {mejor_f}")

        # Se actualizan las listas con el mejor vecino
        camino.append(mejor_vecino)
        acumulado.append(mejor_g)
        heuristicas.append(mejor_h)
        visitados.add(mejor_vecino)
        actual = mejor_vecino

    # Resultados finales
    print("\n=== RESULTADOS DE LA BÚSQUEDA A* ===")
    print("Camino encontrado:", " → ".join(camino))
    print("Heurísticas por paso:", heuristicas)
    print("Costos reales (g):", acumulado)
    print("Costo total:", acumulado[-1])
    print("Suma total de heurísticas:", sum(heuristicas))

    # Guarda toda la información en la lista global
    resultado = {
        "camino": camino.copy(),
        "heuristicas": heuristicas.copy(),
        "costos_reales": acumulado.copy(),
        "costo_total": acumulado[-1],
        "suma_heuristicas": sum(heuristicas)
    }
    rutas.append(resultado)

    return camino, acumulado, heuristicas


# ======================================================
# MENÚ PRINCIPAL
# ======================================================

while True: # Bucle principal del menu 

    print("\n" + "="*40)
    print("Menu")
    print("="*40)
    print("1. Realizar busqueda voraz")
    print("2. Realizar busque A*")
    print("3. Cargar rutas realizadas")
    print("4. Salir")

    

    try:
        opcion = int(input("\nElige una opcion: "))
    except ValueError:
        print("Por favor ingresa un número válido (1, 2, 3, 0 4).")
        continue  # vuelve al inicio del while principal

    match opcion: 
        case 1:
            try:
                inicio = input("Elige tu ciudad de partida: ").casefold().strip()
                meta = input("Elige tu ciudad destino: ").casefold().strip()
            except ValueError:
                print("Por favor escriba ciudades validas")
                continue # vuelve al inicio del while principal
        
            busquedaVoraz(grafo, heuristicaVoraz, inicio, meta, rutas) 
        case 2: 
            try:
                inicio = input("Elige tu ciudad de partida: ").casefold().strip()
                meta = input("Elige tu ciudad destino: ").casefold().strip()
            except ValueError:
                print("Por favor escriba ciudades validas")
                continue # vuelve al inicio del while principal
            busqueda_A(grafo, heuristicaA, inicio, meta, rutas) 
        case 3:
            print("\n=== TODAS LAS RUTAS GENERADAS ===")

            for i, ruta in enumerate(rutas, 1):
                print(f"\nRuta {i}:")

                # Si la ruta es una tupla (como la de búsqueda voraz)
                if isinstance(ruta, tuple):
                    camino, heuristicas, total = ruta
                    print("Algoritmo: Búsqueda Voraz")
                    print("Camino encontrado:", " → ".join(camino))
                    print("Heurísticas por paso:", heuristicas)
                    print("Suma total de heurísticas:", total)

               # Si la ruta es un diccionario (como la de A*)
                elif isinstance(ruta, dict):
                    print("Algoritmo: A*")
                    print("Camino encontrado:", " → ".join(ruta['camino']))
                    print("Heurísticas por paso:", ruta['heuristicas'])
                    print("Costos reales (g):", ruta['costos_reales'])
                    print("Costo total:", ruta['costo_total'])
                    print("Suma total de heurísticas:", ruta['suma_heuristicas'])
        case 4:
            print("Gracias por usar nuestro sistema")
            break
        case _:
            print("Has ingresado una opcion no valida, por favor intente de nuevo") 

    salida = int(input("\nDeseas ir al menu principal o salir del programa? (1 = para menu, 2 = para salir): "))
    if salida == 2:
        print("Gracias por usar nuestro sistema")
        break

print("Hasta pronto... ")


