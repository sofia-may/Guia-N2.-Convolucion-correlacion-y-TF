# -*- coding: utf-8 -*-
"""
=============================================================================
PRÁCTICA DE LABORATORIO – ANÁLISIS ESTADÍSTICO DE SEÑALES
Universidad Militar Nueva Granada
Asignatura: Procesamiento Digital de Señales

PARTE C – Captura de señal con DAQ + Análisis estadístico + Fourier

Este script:
  1. Captura una señal del generador de señales biológicas usando la DAQ
  2. La guarda en formato .txt para poder usarla después
  3. Determina la frecuencia de Nyquist
  4. Caracteriza la señal: media, mediana, desv. estándar, máximo, mínimo
  5. Clasifica la señal según su tipo
  6. Aplica la Transformada de Fourier y grafica:
       a. La transformada de la señal
       b. La densidad espectral de potencia (PSD)
       c. Estadísticos en el dominio de la frecuencia:
            - Frecuencia media
            - Frecuencia mediana
            - Desviación estándar
            - Histograma de frecuencias

REQUISITOS:
  pip install nidaqmx
  python -m nidaqmx installdriver

Created on Thu Aug 21 08:36:05 2025
Modified for lab practice
@author: Carolina Corredor (base) + Lab Group (modifications)
=============================================================================
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from datetime import datetime

# =============================================================================
# PASO 1 – CONFIGURACIÓN DE LA CAPTURA
# =============================================================================
# IMPORTANTE: Ajusta estos parámetros según tu hardware y el tipo de señal
# que estés capturando del generador de señales biológicas

FS        = 500       # Frecuencia de muestreo [Hz]
                        # Para ECG usa 1000 Hz, para otras señales ajusta según Nyquist
DURACION  = 4          # Duración de la captura [segundos]
                        # Usa 10 s para que sea comparable con la Parte A

DISPOSITIVO = 'Dev6/ai0'  # ← CAMBIA ESTO según tu DAQ
                          # Para ver el nombre correcto:
                          # 1. Abre NI MAX (Measurement & Automation Explorer)
                          # 2. Ve a "Devices and Interfaces"
                          # 3. Busca tu DAQ y anota el nombre (ej: Dev1, cDAQ1, etc)
                          # 4. Los canales son ai0, ai1, ai2... para entradas analógicas

# Rango de voltaje esperado (ajustar según tu señal)
V_MIN = -5             # Voltaje mínimo [V]
V_MAX =  5             # Voltaje máximo [V]

total_muestras = int(FS * DURACION)
print("="*60)
print("  CAPTURA DE SEÑAL FISIOLÓGICA CON DAQ")
print("="*60)
print(f"  Dispositivo      : {DISPOSITIVO}")
print(f"  Frecuencia       : {FS} Hz")
print(f"  Duración         : {DURACION} s")
print(f"  Total muestras   : {total_muestras}")
print(f"  Rango            : {V_MIN} a {V_MAX} V")
print("\nIniciando captura...")


# =============================================================================
# PASO 2 – CAPTURA CON LA DAQ
# =============================================================================
try:
    with nidaqmx.Task() as task:
        # Configurar canal con rango de voltaje
        task.ai_channels.add_ai_voltage_chan(
            DISPOSITIVO,
            min_val=V_MIN,
            max_val=V_MAX
        )
        
        # Configurar reloj de muestreo
        task.timing.cfg_samp_clk_timing(
            FS,
            sample_mode=AcquisitionType.FINITE,
            samps_per_chan=total_muestras
        )
        
        # Capturar todas las muestras
        senal = task.read(number_of_samples_per_channel=total_muestras)
    
    print("✓ Captura completada exitosamente")
    
except Exception as e:
    print(f"\n✗ ERROR en la captura: {e}")
    print("\nPosibles soluciones:")
    print("  1. Verifica que la DAQ esté conectada")
    print("  2. Revisa el nombre del dispositivo en NI MAX")
    print("  3. Comprueba que el canal existe (ai0, ai1, etc.)")
    print("  4. Asegúrate de tener los drivers instalados")
    raise


# =============================================================================
# PASO 3 – GUARDAR LA SEÑAL EN ARCHIVO .TXT
# =============================================================================
# Crear nombre de archivo con timestamp para no sobrescribir capturas anteriores
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
archivo_txt = f"senal_capturada_{timestamp}.txt"

# Guardar con formato de 2 columnas: tiempo [s] | amplitud [V]
t = np.arange(len(senal)) / FS
datos_guardar = np.column_stack((t, senal))

np.savetxt(
    archivo_txt,
    datos_guardar,
    fmt='%.6f',           # 6 decimales de precisión
    delimiter='\t',       # separado por tabulación
    header=f'Captura DAQ - {timestamp}\nFs={FS} Hz, Duracion={DURACION} s, Dispositivo={DISPOSITIVO}\nTiempo[s]\tAmplitud[V]',
    comments='# '
)

print(f"✓ Señal guardada en: {archivo_txt}")


# =============================================================================
# PASO 4 – CONVERTIR A NUMPY ARRAY Y VERIFICAR
# =============================================================================
senal = np.array(senal)  # asegurar que sea numpy array

print(f"\n  Muestras capturadas : {len(senal)}")
print(f"  Valor mínimo        : {senal.min():.4f} V")
print(f"  Valor máximo        : {senal.max():.4f} V")


# =============================================================================
# PASO 5 – FRECUENCIA DE NYQUIST
# =============================================================================
# La frecuencia de Nyquist es la mitad de la frecuencia de muestreo.
# Para reconstruir una señal sin aliasing, Fs debe ser al menos 2 × f_max.
# En esta captura se usó Fs = 4 × f_Nyquist, cumpliendo el criterio de Nyquist.

f_nyquist = FS / 2

print("\n" + "="*60)
print("  PASO 5 – FRECUENCIA DE NYQUIST")
print("="*60)
print(f"  Frecuencia de muestreo  : {FS} Hz")
print(f"  Frecuencia de Nyquist   : {f_nyquist} Hz")
print(f"  Fs utilizada            : {FS} Hz  (= 4 × {f_nyquist/2:.1f} Hz)")


# =============================================================================
# PASO 6 – ESTADÍSTICOS CON FUNCIONES PREDEFINIDAS
# =============================================================================
mu  = np.mean(senal)
me  = np.median(senal)
s   = np.std(senal,  ddof=1)
v   = np.var(senal,  ddof=1)
cv  = (s / abs(mu)) * 100 if mu != 0 else np.inf
g1  = stats.skew(senal)
g2  = stats.kurtosis(senal)
vmax = senal.max()
vmin = senal.min()

print("\n" + "="*60)
print(f"  ESTADÍSTICOS – SEÑAL CAPTURADA ({DURACION} s)")
print("="*60)
print(f"  Media            : {mu:>12.6f} V")
print(f"  Mediana          : {me:12.6f} V")
print(f"  Desv. estándar   : {s:>12.6f} V")
print(f"  Varianza         : {v:>12.6f} V²")
print(f"  Máximo           : {vmax:>12.6f} V")
print(f"  Mínimo           : {vmin:>12.6f} V")
print(f"  Coef. variación  : {cv:>12.4f} %")
print(f"  Asimetría        : {g1:>12.6f}")
print(f"  Curtosis         : {g2:>12.6f}")


# =============================================================================
# PASO 7 – CLASIFICACIÓN DE LA SEÑAL
# =============================================================================
print("\n" + "="*60)
print("  CLASIFICACIÓN DE LA SEÑAL")
print("="*60)
print("  • Determinística / Aleatoria : Aleatoria")
print("    (proviene de un proceso fisiológico no predecible con exactitud)")
print("  • Periódica / Aperiódica     : Cuasiperiódica")
print("    (señal biológica con patrón repetitivo pero no estrictamente periódico)")
print("  • Analógica / Digital        : Digital")
print("    (señal continua convertida a muestras discretas mediante el ADC de la DAQ)")


# =============================================================================
# PASO 8 – GRÁFICAS EN EL DOMINIO DEL TIEMPO
# =============================================================================

# ── Gráfica 1: Señal en el tiempo ───────────────────────────────────────────
fig1, ax1 = plt.subplots(figsize=(13, 5))
fig1.suptitle(f"Señal capturada con DAQ  |  {DISPOSITIVO}  |  Fs={FS} Hz",
              fontsize=13, fontweight='bold')

ax1.plot(t, senal, color='#C62828', lw=0.8, label='Señal capturada')
ax1.axhline(mu,      color='black',   ls='--', lw=1.4,
            label=f'Media = {mu:.5f} V')
ax1.axhline(mu + s,  color='#2E7D32', ls=':',  lw=1.2,
            label=f'μ+σ = {mu+s:.4f}')
ax1.axhline(mu - s,  color='#2E7D32', ls=':',  lw=1.2,
            label=f'μ-σ = {mu-s:.4f}')
ax1.set_xlabel("Tiempo (s)", fontsize=11)
ax1.set_ylabel("Amplitud (V)", fontsize=11)
ax1.set_xlim(0, DURACION)
ax1.legend(fontsize=9, loc='upper right')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f"grafica_senal_capturada_{timestamp}.png", dpi=150, bbox_inches='tight')
plt.show()

# ── Gráfica 2: Histograma + curva normal ────────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(9, 5))
fig2.suptitle("Histograma - Señal capturada", fontsize=13, fontweight='bold')

conteos, bordes = np.histogram(senal, bins=60, density=True)
centros = (bordes[:-1] + bordes[1:]) / 2
ancho   = bordes[1] - bordes[0]

ax2.bar(centros, conteos, width=ancho*0.9, color='#EF5350',
        alpha=0.85, label='Datos capturados')

# Curva normal teórica
x_ref = np.linspace(senal.min(), senal.max(), 500)
ax2.plot(x_ref, stats.norm.pdf(x_ref, mu, s), 'k-', lw=2,
         label='Normal teórica')
ax2.axvline(mu, color='navy', ls='--', lw=1.5,
            label=f'Media = {mu:.3f}')

ax2.set_xlabel("Amplitud (V)", fontsize=11)
ax2.set_ylabel("Densidad de probabilidad", fontsize=11)
ax2.set_title(f"Asimetría={g1:.3f}  |  Curtosis={g2:.3f}", fontsize=10)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f"grafica_histograma_capturado_{timestamp}.png", dpi=150, bbox_inches='tight')
plt.show()

# ── Gráfica 3: Boxplot ───────────────────────────────────────────────────────
fig3, ax3 = plt.subplots(figsize=(5, 6))
fig3.suptitle("Box-plot – Señal capturada", fontsize=13, fontweight='bold')

ax3.boxplot(senal, patch_artist=True,
            boxprops=dict(facecolor='#FFCDD2'),
            medianprops=dict(color='red', lw=2),
            whiskerprops=dict(lw=1.2),
            flierprops=dict(marker='.', markersize=3, alpha=0.4))
ax3.set_ylabel("Amplitud (V)", fontsize=11)
ax3.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f"grafica_boxplot_capturado_{timestamp}.png", dpi=150, bbox_inches='tight')
plt.show()

print("\n✓ Gráficas del dominio del tiempo generadas y guardadas")


# =============================================================================
# PASO 9 – TRANSFORMADA DE FOURIER Y DENSIDAD ESPECTRAL DE POTENCIA
# =============================================================================
N      = len(senal)
Y      = np.fft.rfft(senal)                    # Transformada (solo frecuencias positivas)
freqs  = np.fft.rfftfreq(N, d=1/FS)            # Vector de frecuencias [Hz]
magnitud = np.abs(Y)                            # Magnitud del espectro
fase     = np.angle(Y)                          # Fase del espectro
psd      = (magnitud ** 2) / (N * FS)          # Densidad espectral de potencia [V²/Hz]

# ── Gráfica 4: Transformada de Fourier (magnitud) ───────────────────────────
fig4, axes4 = plt.subplots(2, 1, figsize=(13, 7))
fig4.suptitle("Transformada de Fourier – Señal capturada",
              fontsize=13, fontweight='bold')

axes4[0].plot(freqs, magnitud, color='#1565C0', lw=0.9)
axes4[0].set_title("Espectro de magnitud  |X(f)|", fontsize=11, fontweight='bold')
axes4[0].set_xlabel("Frecuencia (Hz)", fontsize=10)
axes4[0].set_ylabel("Magnitud", fontsize=10)
axes4[0].set_xlim(0, f_nyquist)
axes4[0].grid(True, alpha=0.3)

axes4[1].plot(freqs, fase, color='#6A1B9A', lw=0.9)
axes4[1].set_title("Espectro de fase  ∠X(f)", fontsize=11, fontweight='bold')
axes4[1].set_xlabel("Frecuencia (Hz)", fontsize=10)
axes4[1].set_ylabel("Fase (rad)", fontsize=10)
axes4[1].set_xlim(0, f_nyquist)
axes4[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f"grafica_fourier_{timestamp}.png", dpi=150, bbox_inches='tight')
plt.show()

# ── Gráfica 5: Densidad espectral de potencia ────────────────────────────────
fig5, ax5 = plt.subplots(figsize=(13, 5))
fig5.suptitle("Densidad Espectral de Potencia (PSD) – Señal capturada",
              fontsize=13, fontweight='bold')

ax5.semilogy(freqs, psd, color='#C62828', lw=0.9)
ax5.set_xlabel("Frecuencia (Hz)", fontsize=11)
ax5.set_ylabel("PSD  (V²/Hz)", fontsize=11)
ax5.set_xlim(0, f_nyquist)
ax5.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig(f"grafica_psd_{timestamp}.png", dpi=150, bbox_inches='tight')
plt.show()


# =============================================================================
# PASO 10 – ESTADÍSTICOS EN EL DOMINIO DE LA FRECUENCIA
# =============================================================================
# Se ponderan las frecuencias por la magnitud del espectro para obtener
# estadísticos representativos de la distribución energética de la señal.

mag_norm    = magnitud / magnitud.sum()          # magnitud normalizada (suma = 1)
freq_media  = np.sum(freqs * mag_norm)           # frecuencia media ponderada
cumsum      = np.cumsum(mag_norm)
freq_mediana = freqs[np.searchsorted(cumsum, 0.5)]  # frecuencia mediana
freq_std    = np.sqrt(np.sum(mag_norm * (freqs - freq_media) ** 2))  # desv. estándar

print("\n" + "="*60)
print("  ESTADÍSTICOS EN EL DOMINIO DE LA FRECUENCIA")
print("="*60)
print(f"  Frecuencia media    : {freq_media:.2f} Hz")
print(f"  Frecuencia mediana  : {freq_mediana:.2f} Hz")
print(f"  Desv. estándar      : {freq_std:.2f} Hz")

# ── Gráfica 6: Histograma de frecuencias ─────────────────────────────────────
fig6, ax6 = plt.subplots(figsize=(10, 5))
fig6.suptitle("Histograma de Frecuencias – Dominio espectral",
              fontsize=13, fontweight='bold')

ax6.bar(freqs, magnitud, width=(freqs[1]-freqs[0])*0.9,
        color='#1565C0', alpha=0.8, label='Magnitud espectral')
ax6.axvline(freq_media,   color='red',    ls='--', lw=1.5,
            label=f'Freq. media = {freq_media:.1f} Hz')
ax6.axvline(freq_mediana, color='orange', ls='--', lw=1.5,
            label=f'Freq. mediana = {freq_mediana:.1f} Hz')

ax6.set_xlabel("Frecuencia (Hz)", fontsize=11)
ax6.set_ylabel("Magnitud  |X(f)|", fontsize=11)
ax6.set_xlim(0, f_nyquist)
ax6.set_title(f"Frec. media={freq_media:.1f} Hz  |  "
              f"Frec. mediana={freq_mediana:.1f} Hz  |  "
              f"Desv. std={freq_std:.1f} Hz", fontsize=10)
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f"grafica_histograma_frecuencias_{timestamp}.png", dpi=150, bbox_inches='tight')
plt.show()

print(f"\n✓ Gráfica de histograma de frecuencias guardada")
print("\n✓ Todas las gráficas generadas y guardadas")
print("="*60)