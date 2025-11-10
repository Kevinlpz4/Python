import math
from tabulate import tabulate  # para imprimir la tabla bonita

# ==============================
# FUNCIONES MATEMÁTICAS
# ==============================

def f(x, A, B, C):
    """Evalúa la función cuadrática."""
    return A*x**2 + B*x + C


def metodo_directo(A, B, C):
    """Calcula las raíces reales de la ecuación ax² + bx + c = 0."""
    resultados = {}
    disc = B**2 - 4*A*C
    if disc < 0:
        print("\nNo existen raíces reales (discriminante < 0).")
        resultados["tipo"] = "sin_raices"
    elif abs(disc) < 1e-14:
        x = -B / (2*A)
        print(f"\n🔹 Raíz doble: x = {x:.6f}")
        resultados["tipo"] = "doble"
        resultados["raices"] = [x]
    else:
        sqrt_d = math.sqrt(disc)
        x1 = (-B + sqrt_d) / (2*A)
        x2 = (-B - sqrt_d) / (2*A)
        print("\nMétodo directo (Fórmula Cuadrática):")
        print(f"Raíz 1: {x1:.6f}")
        print(f"Raíz 2: {x2:.6f}")
        print(f"Verificación: f(x1)={f(x1,A,B,C):.3e}, f(x2)={f(x2,A,B,C):.3e}")
        resultados["tipo"] = "dos_raices"
        resultados["raices"] = [x1, x2]
    return resultados


def metodo_secante(A, B, C, x0, x1, tol=1e-6, max_iter=50):
    """Aplica el método de la secante para hallar una raíz de f(x)=0."""
    print("\n📘 Método de la Secante:")
    tabla = []
    fx0 = f(x0, A, B, C)
    fx1 = f(x1, A, B, C)
    for i in range(1, max_iter + 1):
        denom = fx1 - fx0
        if abs(denom) < 1e-14:
            print("Denominador demasiado pequeño, interrumpiendo.")
            break
        x2 = x1 - fx1 * (x1 - x0) / denom
        fx2 = f(x2, A, B, C)
        error = abs((x2 - x1) / x2)
        tabla.append([i, round(x0,6), round(fx0,6),
                         round(x1,6), round(fx1,6),
                         round(x2,6), round(fx2,6),
                         f"{error:.2e}"])
        if error < tol:
            print(tabulate(tabla, headers=["Iter", "x(i-1)", "f(xi-1)",
                                           "x(i)", "f(xi)", "x(i+1)",
                                           "f(xi+1)", "Error"], tablefmt="grid"))
            print(f"\nConvergencia alcanzada en {i} iteraciones.")
            print(f"Raíz aproximada: x ≈ {x2:.6f}")
            return {"raiz": x2, "iteraciones": i, "tabla": tabla}
        x0, fx0 = x1, fx1
        x1, fx1 = x2, fx2

    print(tabulate(tabla, headers=["Iter", "x(i-1)", "f(xi-1)",
                                   "x(i)", "f(xi)", "x(i+1)",
                                   "f(xi+1)", "Error"], tablefmt="grid"))
    print("\nNo se alcanzó la convergencia dentro del número máximo de iteraciones.")
    return {"raiz": x2, "iteraciones": max_iter, "tabla": tabla}


# ==============================
# ALMACENAMIENTO DE RESULTADOS
# ==============================

resultados_guardados = {
    "directos": [],
    "secantes": []
}


# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu_principal():
    while True:
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Calcular raíces (Fórmula Cuadrática)")
        print("2. Aplicar método de la Secante")
        print("3. Mostrar resultados guardados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Entrada de coeficientes
            A = float(input("\nIngrese A: "))
            B = float(input("Ingrese B: "))
            C = float(input("Ingrese C: "))
            res = metodo_directo(A, B, C)
            resultados_guardados["directos"].append(res)

        elif opcion == "2":
            A = float(input("\nIngrese A: "))
            B = float(input("Ingrese B: "))
            C = float(input("Ingrese C: "))
            x0 = float(input("Ingrese el valor inicial x0: "))
            x1 = float(input("Ingrese el valor inicial x1: "))
            tol = float(input("Ingrese la tolerancia (ej: 1e-6): ") or 1e-6)
            max_iter = int(input("Ingrese el número máximo de iteraciones (ej: 50): ") or 50)
            res = metodo_secante(A, B, C, x0, x1, tol, max_iter)
            resultados_guardados["secantes"].append(res)

        elif opcion == "3":
            print("\nResultados guardados:")
            print("1. Mostrar raíces directas")
            print("2. Mostrar resultados de la secante")
            sub = input("Seleccione: ")

            if sub == "1":
                if resultados_guardados["directos"]:
                    for i, r in enumerate(resultados_guardados["directos"], 1):
                        print(f"\n[{i}] Raíces directas: {r.get('raices', 'N/A')}")
                else:
                    print("No hay resultados directos guardados aún.")

            elif sub == "2":
                if resultados_guardados["secantes"]:
                    for i, r in enumerate(resultados_guardados["secantes"], 1):
                        print(f"\n[{i}] Raíz secante: {r.get('raiz', 'N/A')}, Iteraciones: {r.get('iteraciones', 'N/A')}")
                else:
                    print("No hay resultados de la secante guardados aún.")
            else:
                print("Opción no válida.")

        elif opcion == "4":
            print("\nFin del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")


# ==============================
# EJECUCIÓN PRINCIPAL
# ==============================

if __name__ == "__main__":
    menu_principal()
