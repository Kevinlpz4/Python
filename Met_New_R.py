"""
Método de Newton–Raphson con entrada por consola.
- Permite ingresar la función N(t) por consola.
- Permite ingresar la semilla por consola.
- Usa valores predeterminados si se deja ENTER.
- Muestra tabla en la consola y la gráfica en pantalla.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd

# -------------------- CONFIGURACIÓN POR DEFECTO --------------------
DEFAULT_FUNCTION = "3*exp(0.87*t)/(11*t)"   # función del enunciado
DEFAULT_SEED_HOURS = 432.0                 # semilla del profe (18 días)
tol = 0.002                                 # criterio de paro
max_iter = 100                              # máx. iteraciones
round_decimals = 5                          # decimales en la tabla
MOSTRAR_GRAFICA = True                      # mostrar gráfica
# -------------------------------------------------------------------


# ======= ENTRADA POR CONSOLA =======

print("\n=== MÉTODO DE NEWTON–RAPHSON ===\n")

# Función
user_func = input(f"Ingrese la función N(t) (ENTER para usar '{DEFAULT_FUNCTION}'): ").strip()
if user_func == "":
    N_expr = DEFAULT_FUNCTION
else:
    N_expr = user_func

# Semilla en horas
user_seed = input(f"Ingrese la semilla en horas (ENTER para usar {DEFAULT_SEED_HOURS}): ").strip()
if user_seed == "":
    seed_hours = DEFAULT_SEED_HOURS
else:
    seed_hours = float(user_seed)

print("\nFunción seleccionada: N(t) =", N_expr)
print("Semilla ingresada:", seed_hours, "horas\n")


# ======= PREPARAR FUNCIÓN =======

t = sp.symbols("t")
expr = sp.sympify(N_expr) - 115      # f(t) = N(t) - 115
dexpr = sp.diff(expr, t)             # derivada simbólica

f = sp.lambdify(t, expr, "numpy")
fprime = sp.lambdify(t, dexpr, "numpy")

print("f(t) = N(t) - 115 =", expr)
print("f'(t) =", dexpr, "\n")


# ======= CONVERTIR SEMILLA =======
seed_days = seed_hours / 24.0
print(f"Semilla convertida: {seed_hours} horas = {seed_days} días\n")


# ======= MÉTODO DE NEWTON =======

def newton(f, fprime, x0):
    rows = []
    x_n = float(x0)

    for n in range(max_iter):
        fx = float(f(x_n))
        fpx = float(fprime(x_n))

        if abs(fpx) < 1e-12:
            raise ZeroDivisionError("La derivada es muy pequeña, método no puede continuar.")

        x_next = x_n - fx / fpx

        err_rel = abs((x_next - x_n) / x_next)
        err_abs_f = abs(f(x_next))

        rows.append({
            "n": n,
            "x_n (días)": x_n,
            "f(x_n)": fx,
            "f'(x_n)": fpx,
            "x_{n+1}": x_next,
            "err_rel": err_rel,
            "err_abs_f": err_abs_f
        })

        if err_rel < tol:
            return x_next, n+1, pd.DataFrame(rows)

        x_n = x_next

    return x_n, max_iter, pd.DataFrame(rows)


# ======= EJECUTAR =======

root, iters, df = newton(f, fprime, seed_days)

# Redondear tabla
df_print = df.copy()
for col in df_print.columns:
    if col != "n":
        df_print[col] = df_print[col].apply(lambda v: round(float(v), round_decimals))

print("\n=== TABLA DE ITERACIONES ===\n")
print(df_print.to_string(index=False))

print(f"\nRaíz encontrada: {root:.5f} días  ≈  {24*root:.5f} horas")
print(f"Iteraciones: {iters}")
print(f"Error absoluto final |f(t*)| = {df.iloc[-1]['err_abs_f']}\n")


# ======= GRÁFICA =======
if MOSTRAR_GRAFICA:
    xs = df["x_n (días)"].to_numpy()
    X = np.linspace(max(1, xs.min()-1), xs.max()+1, 400)
    Y = np.array([f(x) for x in X])

    plt.figure(figsize=(8,5))
    plt.plot(X, Y, label="f(t) = N(t) - 115")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.scatter(df["x_n (días)"], df["f(x_n)"], zorder=5, label="Iteraciones")
    plt.title("Método de Newton–Raphson")
    plt.xlabel("t (días)")
    plt.ylabel("f(t)")
    plt.grid(True)
    plt.legend()
    plt.show()
