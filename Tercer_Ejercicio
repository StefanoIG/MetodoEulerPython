import numpy as np

# Parámetros
T0 = 70.0  # Temperatura inicial del café (°C)
Ta = 20.0  # Temperatura ambiente (°C)
k = 0.019  # Constante de proporcionalidad (por minuto)
t0 = 0.0  # Tiempo inicial
t_final = 10.0  # Tiempo final
delta_t = 2.0  # Tamaño de paso (minutos)

# Número de pasos
num_pasos = int((t_final - t0) / delta_t)

# Arreglos para almacenar los resultados
t = np.zeros(num_pasos + 1)
T = np.zeros(num_pasos + 1)

# Condiciones iniciales
t[0] = t0
T[0] = T0

# Método de Euler
for i in range(num_pasos):
    t[i + 1] = t[i] + delta_t
    dTdt = -k * (T[i] - Ta)
    T[i + 1] = T[i] + delta_t * dTdt

# Imprimir los resultados
for i in range(num_pasos + 1):
    print(f"t = {t[i]:.1f} minutos, T = {T[i]:.2f} °C")
