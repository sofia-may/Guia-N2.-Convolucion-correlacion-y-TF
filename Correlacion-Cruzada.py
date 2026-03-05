# -*- coding: utf-8 -*-
"""
=============================================================================
PRÁCTICA DE LABORATORIO – CONVOLUCIÓN Y CORRELACIÓN
Universidad Militar Nueva Granada
Asignatura: Procesamiento Digital de Señales

PARTE B – Correlación cruzada entre señales discretas

Este script:
  1. Define las señales x1[nTs] = cos(2π·100·nTs) y x2[nTs] = sin(2π·100·nTs)
     con Ts = 1.25 ms, para 0 ≤ n < 9
  2. Calcula la correlación cruzada entre ambas señales
  3. Genera la representación gráfica de las tres señales
  4. Describe la secuencia resultante
  5. Responde cuándo es útil aplicar la correlación cruzada en PDS

=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# PASO 1 – DEFINICIÓN DE LAS SEÑALES
# =============================================================================
Ts = 1.25e-3          # Período de muestreo [s] = 1.25 ms
f0 = 100              # Frecuencia de las señales [Hz]
n  = np.arange(0, 9)  # Índices: 0 ≤ n < 9

x1 = np.cos(2 * np.pi * f0 * n * Ts)   # Señal coseno
x2 = np.sin(2 * np.pi * f0 * n * Ts)   # Señal seno

print("=" * 60)
print("  PARTE B – CORRELACIÓN CRUZADA")
print("=" * 60)
print(f"\n  Ts  = {Ts*1e3} ms")
print(f"  f0  = {f0} Hz")
print(f"  n   = {list(n)}")
print("\n  x1[nTs] = cos(2π·100·nTs):")
print(f"  {np.round(x1, 6).tolist()}")
print("\n  x2[nTs] = sin(2π·100·nTs):")
print(f"  {np.round(x2, 6).tolist()}")

# =============================================================================
# PASO 2 – CORRELACIÓN CRUZADA
# =============================================================================
# np.correlate con mode='full' calcula R_x1x2[lag] = Σ x1[n] · x2[n + lag]
# La secuencia resultante tiene longitud 2N - 1

Rxy = np.correlate(x1, x2, mode='full')
lags = np.arange(-(len(n) - 1), len(n))   # Retardos de -(N-1) a +(N-1)

print(f"\n  Longitud correlación cruzada : {len(Rxy)}  (= 2×{len(n)} - 1)")
print(f"\n  Retardos (lags) : {list(lags)}")
print("\n  R_x1x2[lag]:")
for lag, val in zip(lags, Rxy):
    print(f"    lag = {lag:+d}  →  {round(val, 6)}")

# Lag donde ocurre el máximo
lag_max = lags[np.argmax(np.abs(Rxy))]
print(f"\n  Máximo valor absoluto en lag = {lag_max}")

# =============================================================================
# PASO 3 – REPRESENTACIÓN GRÁFICA
# =============================================================================
t_eje = n * Ts * 1e3   # Tiempo en ms para graficar

fig, axes = plt.subplots(3, 1, figsize=(12, 9))
fig.suptitle("Parte B – Correlación cruzada entre señales discretas\n"
             "Universidad Militar Nueva Granada | PDS",
             fontsize=13, fontweight='bold')

# ── Gráfica 1: x1[nTs] ───────────────────────────────────────────────────────
axes[0].stem(t_eje, x1, linefmt='#1565C0', markerfmt='o', basefmt='k-')
axes[0].set_title("x₁[nTₛ] = cos(2π·100·nTₛ)", fontsize=11, fontweight='bold')
axes[0].set_xlabel("Tiempo (ms)", fontsize=10)
axes[0].set_ylabel("Amplitud", fontsize=10)
axes[0].set_xticks(t_eje)
axes[0].set_xticklabels([f"{v:.2f}" for v in t_eje], fontsize=8)
axes[0].grid(True, alpha=0.3)

# ── Gráfica 2: x2[nTs] ───────────────────────────────────────────────────────
axes[1].stem(t_eje, x2, linefmt='#2E7D32', markerfmt='o', basefmt='k-')
axes[1].set_title("x₂[nTₛ] = sin(2π·100·nTₛ)", fontsize=11, fontweight='bold')
axes[1].set_xlabel("Tiempo (ms)", fontsize=10)
axes[1].set_ylabel("Amplitud", fontsize=10)
axes[1].set_xticks(t_eje)
axes[1].set_xticklabels([f"{v:.2f}" for v in t_eje], fontsize=8)
axes[1].grid(True, alpha=0.3)

# ── Gráfica 3: Correlación cruzada R_x1x2[lag] ───────────────────────────────
axes[2].stem(lags, Rxy, linefmt='#C62828', markerfmt='o', basefmt='k-')
axes[2].set_title("Correlación cruzada  R_{x₁x₂}[lag]", fontsize=11, fontweight='bold')
axes[2].set_xlabel("Retardo (lag)", fontsize=10)
axes[2].set_ylabel("Amplitud", fontsize=10)
axes[2].set_xticks(lags)
axes[2].axvline(lag_max, color='orange', ls='--', lw=1.4,
                label=f'Máximo en lag = {lag_max}')
axes[2].axhline(0, color='black', lw=0.8)
axes[2].legend(fontsize=9)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("parte_B_correlacion.png", dpi=150, bbox_inches='tight')
plt.show()

# =============================================================================
# PASO 4 – DESCRIPCIÓN DE LA SECUENCIA RESULTANTE
# =============================================================================
print("\n" + "="*60)
print("  DESCRIPCIÓN DE LA SECUENCIA RESULTANTE")
print("="*60)
print("""
  La correlación cruzada entre cos y sen de la misma frecuencia
  produce una secuencia que refleja el desfase de 90° (π/2 rad)
  entre ambas señales. El valor máximo de |R_x1x2| ocurre en el
  lag donde las señales tienen mayor similitud desplazada, y la
  secuencia es antisimétrica respecto al lag=0, lo cual es
  característico de dos señales en cuadratura (desfasadas 90°).
""")

# =============================================================================
# PASO 5 – ¿CUÁNDO ES ÚTIL LA CORRELACIÓN CRUZADA EN PDS?
# =============================================================================
print("="*60)
print("  ¿EN QUÉ SITUACIONES ES ÚTIL LA CORRELACIÓN CRUZADA?")
print("="*60)
print("""
  1. Detección de retardo entre señales: permite identificar
     cuánto tiempo tarda una señal en llegar a otro sensor
     (ej: localización de fuentes sonoras o sísmicas).

  2. Identificación de similitud entre señales: útil para
     comparar una señal de referencia con una señal ruidosa
     y determinar si contiene el patrón buscado.

  3. Procesamiento de señales biomédicas: por ejemplo, para
     detectar relaciones entre dos canales de EEG, o entre
     una señal de estimulación y la respuesta fisiológica.

  4. Radar y sonar: para estimar la distancia a un objeto
     correlacionando la señal emitida con el eco recibido.

  5. Comunicaciones: para sincronización y detección de
     señales en presencia de ruido e interferencias.
""")

print("✓ Gráfica guardada como 'parte_B_correlacion.png'")
print("="*60)