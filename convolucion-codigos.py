# -*- coding: utf-8 -*-
"""
=============================================================================
PRÁCTICA DE LABORATORIO – CONVOLUCIÓN Y CORRELACIÓN
Universidad Militar Nueva Granada
Asignatura: Procesamiento Digital de Señales

PARTE A – Convolución de señales discretas usando Python

Este script:
  1. Define h[n] y x[n] a partir de los datos personales del estudiante
  2. Calcula la señal y[n] resultante de la convolución usando np.convolve
  3. Muestra la representación secuencial en consola
  4. Genera la representación gráfica de las tres señales

=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# PASO 1 – DEFINICIÓN DE LAS SEÑALES
# =============================================================================
# h[n]: dígitos del código del estudiante
# x[n]: dígitos de la cédula del estudiante

h = np.array([5, 6, 0, 0, 9, 1, 3, 5, 6, 0, 0, 9, 4, 5])
x = np.array([1, 0, 7, 0, 0, 0, 5, 6, 8, 9, 1, 0, 7, 7, 1, 4, 4, 0, 6, 0])

print("=" * 60)
print("  PARTE A – CONVOLUCIÓN DE SEÑALES DISCRETAS")
print("=" * 60)
print(f"\n  h[n] (sistema)  : {list(h)}")
print(f"  Longitud h[n]   : {len(h)}")
print(f"\n  x[n] (entrada)  : {list(x)}")
print(f"  Longitud x[n]   : {len(x)}")

# =============================================================================
# PASO 2 – CÁLCULO DE LA CONVOLUCIÓN
# =============================================================================
y = np.convolve(h, x)

print(f"\n  Longitud y[n]   : {len(y)}  (= {len(h)} + {len(x)} - 1)")
print("\n y[n] = h[n] * x[n]:")
print(f"  {list(y)}")

# Representación secuencial índice por índice
print("\n" + "-" * 60)
print("  Representación secuencial de y[n]:")
print("-" * 60)
for n, val in enumerate(y):
    print(f"  y[{n:2d}] = {int(val)}")

# =============================================================================
# PASO 3 – REPRESENTACIÓN GRÁFICA
# =============================================================================
n_h = np.arange(len(h))
n_x = np.arange(len(x))
n_y = np.arange(len(y))

fig, axes = plt.subplots(3, 1, figsize=(13, 9))
fig.suptitle("Parte A – Convolución de señales discretas\n"
             "Universidad Militar Nueva Granada | PDS",
             fontsize=13, fontweight='bold')

# ── Gráfica 1: h[n] ──────────────────────────────────────────────────────────
axes[0].stem(n_h, h, linefmt='#1565C0', markerfmt='o', basefmt='k-')
axes[0].set_title("Sistema  h[n]", fontsize=11, fontweight='bold')
axes[0].set_xlabel("n", fontsize=10)
axes[0].set_ylabel("Amplitud", fontsize=10)
axes[0].set_xticks(n_h)
axes[0].grid(True, alpha=0.3)

# ── Gráfica 2: x[n] ──────────────────────────────────────────────────────────
axes[1].stem(n_x, x, linefmt='#2E7D32', markerfmt='o', basefmt='k-')
axes[1].set_title("Señal de entrada  x[n]", fontsize=11, fontweight='bold')
axes[1].set_xlabel("n", fontsize=10)
axes[1].set_ylabel("Amplitud", fontsize=10)
axes[1].set_xticks(n_x)
axes[1].grid(True, alpha=0.3)

# ── Gráfica 3: y[n] = h[n] * x[n] ───────────────────────────────────────────
axes[2].stem(n_y, y, linefmt='#C62828', markerfmt='o', basefmt='k-')
axes[2].set_title("Señal de salida  y[n] = h[n] * x[n]", fontsize=11, fontweight='bold')
axes[2].set_xlabel("n", fontsize=10)
axes[2].set_ylabel("Amplitud", fontsize=10)
axes[2].set_xticks(n_y)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("parte_A_convolucion.png", dpi=150, bbox_inches='tight')
plt.show()

print("\n✓ Gráfica guardada como 'parte_A_convolucion.png'")
print("=" * 60)