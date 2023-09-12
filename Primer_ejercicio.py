import numpy as np

# Parámetros
k = 0.175  # Constante de decaimiento (d^-1)
t0 = 0     # Tiempo inicial
t_final = 1  # Tiempo final
delta_t = 0.1  # Tamaño de paso
C0 = 100  # Concentración inicial (Bq/L)

# Número de pasos
num_pasos = int((t_final - t0) / delta_t)

# Arreglos para almacenar los resultados
t = np.zeros(num_pasos + 1)
C = np.zeros(num_pasos + 1)

# Condiciones iniciales
t[0] = t0
C[0] = C0

# Método de Euler
for i in range(num_pasos):
    t[i + 1] = t[i] + delta_t
    dCdt = -k * C[i]
    C[i + 1] = C[i] + delta_t * dCdt

# Imprimir los resultados
for i in range(num_pasos + 1):
    print(f"t = {t[i]:.1f} d, C = {C[i]:.2f} Bq/L")
