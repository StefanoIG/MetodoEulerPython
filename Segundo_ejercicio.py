import numpy as np

# Parámetros
A = 1250  # Área de la superficie (m^2)
Q = 450  # Tasa de flujo constante (m^3/día)
t0 = 0  # Tiempo inicial
t_final = 10  # Tiempo final
delta_t = 0.5  # Tamaño de paso
y0 = 0  # Condición inicial

# Número de pasos
num_pasos = int((t_final - t0) / delta_t)

# Arreglos para almacenar los resultados
t = np.zeros(num_pasos + 1)
y = np.zeros(num_pasos + 1)

# Condiciones iniciales
t[0] = t0
y[0] = y0

# Método de Euler
for i in range(num_pasos):
    t[i + 1] = t[i] + delta_t
    dydt = (3 * Q / A) * np.sin(t[i])**2 - (Q / A)
    y[i + 1] = y[i] + delta_t * dydt

# Imprimir los resultados
for i in range(num_pasos + 1):
    print(f"t = {t[i]:.1f} días, y = {y[i]:.2f} metros")
