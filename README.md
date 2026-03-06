# Guia-N2.-Convolucion-correlacion-y-TF
---
## Descripción
En este repositorio se presenta el informe y los resultados de la Práctica de Laboratorio #2 de Convolución, correlación y transformada de Fourier. Se trabajó con el propósito de buscamor observar el comportamiento estadístico; determinar cómo un sistema (filtro) afecta a una señal de entrada, medir la similitud entre dos señales o encontrar un patrón oculto y ver la composición de frecuencias de una señal, pasando del dominio del tiempo al de la frecuencia.
### Correlación cruzada
En el procesamiento digital de señales es fundamental analizar la relación existente entre diferentes señales para determinar similitudes, retrasos o patrones comunes. Una de las herramientas matemáticas más utilizadas para este propósito es la correlación cruzada. Esta técnica permite comparar dos señales y evaluar qué tan similares son cuando una de ellas se desplaza respecto a la otra en el tiempo. Gracias a esta propiedad, la correlación cruzada se utiliza ampliamente en áreas como las telecomunicaciones, el procesamiento de audio, el análisis de imágenes y la detección de señales en sistemas electrónicos [<sup>[1]</sup>](#ref-uni).
#### Definición
La correlación cruzada es una operación matemática que mide el grado de similitud entre dos señales en función del desplazamiento o retardo aplicado a una de ellas [<sup>[2]</sup>](#ref-Data).El resultado de esta operación es una función que indica qué tan parecidas son las señales para diferentes valores de desplazamiento.
Para señales discretas (x[n]) y (y[n]), la correlación cruzada se define matemáticamente como:

<img width="306" height="42" alt="image" src="https://github.com/user-attachments/assets/bb2f9ee0-6b27-4b0f-9a17-b3e78693a189" /> [<sup>[3]</sup>](#ref-universidad)

Donde (x[n]) y (y[n]) representan las señales a comparar y (k) es el desplazamiento o retardo entre ambas señales. Cuando el valor de la correlación es máximo, significa que las señales presentan la mayor similitud posible en ese desplazamiento.
#### Propiedades
La correlación cruzada posee varias propiedades importantes en el análisis de señales:

- No conmutativa: El resultado de correlacionar una señal con otra puede cambiar si se invierte el orden de las señales.
- Relación con la convolución: La correlación está relacionada matemáticamente con la convolución, lo que permite calcularla utilizando métodos similares.
- Simetría: Existe una relación entre la correlación de dos señales y la correlación inversa entre ellas.
- Máximo de correlación: El valor máximo de la correlación ocurre cuando las señales se alinean mejor en el tiempo.
- Relación con la autocorrelación: Si una señal se correlaciona consigo misma, el resultado se conoce como autocorrelación, la cual permite detectar periodicidad en las señales.
## Parte A
### A MANO
![WhatsApp Image 2026-03-05 at 12 17 11](https://github.com/user-attachments/assets/9877cf70-5e12-4c7e-8ebe-d5baa333ad7c)
![WhatsApp Image 2026-03-05 at 12 17 13](https://github.com/user-attachments/assets/9d5704ef-6493-4c65-baaf-e4d2889e4c55)

### EN PYTHON

<img width="1935" height="1330" alt="parte_A_convolucion" src="https://github.com/user-attachments/assets/91bf9325-8e2c-4ea9-934d-e1a188fa690a" />
en la imagen se muestra la grafica de h[n], la grafica de x[n] y la grafica de la convolucion entre ellas.

### Diagrama de flujo
<img width="1272" height="671" alt="image" src="https://github.com/user-attachments/assets/0e6ac14c-b29b-4446-a034-a47f5ede0d56" />

### Datos clave:
<img width="553" height="343" alt="image" src="https://github.com/user-attachments/assets/8d215a85-32bc-4d65-a95a-91cc60f9e6c5" />

## PARTE B
### Correlación cruzada

calculamos los componentes de las dos señales y aplicamos la correlacion cruzada entre las dos.

<img width="635" height="276" alt="image" src="https://github.com/user-attachments/assets/5784c1c2-eb01-4b90-9505-a9d3e1ccbb76" />


<img width="310" height="326" alt="image" src="https://github.com/user-attachments/assets/02092b0e-2462-4b70-842f-7ae8f9853368" />

graficamos los datos obtenidos:
<img width="1785" height="1330" alt="parte_B_correlacion" src="https://github.com/user-attachments/assets/c0aea5d0-edf4-42bd-ad1b-955d9cf2a268" />
segun el "lag" evidenciamos  que en 2 es donde mas se parecen las dos señales

#### Descripción

La correlacion cruzada entre coseno y seno de la misma frecuencia produce una secuencia que refleja el desfase de 90° (π/2 rad) entre ambas señales. El valor maximo de |R X1 y X2| ocurren en el lag donde las señales tienen mayor similitud desplazada, y la secuencia es antisimetrica respecto al lag=0, lo cual es caracteristico de dos señales en cuadratura (desfasada 90°).

 #### ¿En que situaciones es útil la correlación cruzada?

 - Deteccion de retardo entre señales: permite identificar cuanto tiempo tarda una señal en llegar a otro sensor. Por Ejemplo: localizacion de fuentes sonoras o sismicas
   
 - Identificacion de similitud entre señales: util para comparar una señal de referencia con una señal ruidosa y determinar si contiene el patron buscado.
   
 - Procesamiento de señales biomedicas: por ejemplo, para detectar relaciones entre dos canales de EEG, o entre una señal de estimulacion y la respuesta fisiológica.
 
 - Radar y sonar: para estimar la distancia a un objeto correlacionando la señal emitida con el eco recibido.
 
 -   Comunicaciones: para sincronizacion y deteccion de señales en presencia de ruido e interferencias.
### Diagrama de flujo 
<img width="737" height="496" alt="image" src="https://github.com/user-attachments/assets/6ed9fc70-07bc-414b-8801-0e0d888b32eb" />

### Datos clave:
<img width="822" height="281" alt="image" src="https://github.com/user-attachments/assets/4c933978-0c52-4078-943c-9b943d1191f6" />

## PARTE C

<img width="1937" height="744" alt="grafica_senal_capturada_20260305_140950" src="https://github.com/user-attachments/assets/1545fc86-7714-4eca-857c-8847989e9d56" />


Se obtuvo una señal de EOG con la cual se hicieron las distintas operaiones mostradas acontinuacion.

## Preguntas de discución:
- ¿Qué utilidad poseen herramientas como la convolución y la correlación en
áreas como procesamiento de imágenes?
  - En el procesamiento de imágenes, estas herramientas son fundamentales para extraer información relevante de secuencias o matrices.
    Convolución: Se utiliza principalmente para el filtrado lineal. En imágenes, esto se traduce en operaciones como el suavizado (reducción de ruido), el realce de bordes o la detección de características específicas mediante kernels.
    Correlación: Se emplea para identificar patrones o dependencias estadísticas. En imágenes, es clave para el template matching (buscar una imagen pequeña dentro de una más grande) y para el registro o alineación de imágenes.
- ¿En cuáles contextos de aplicación la transformada de Fourier ofrece un
conjunto de características con mayor poder discriminativo que las que
suelen considerarse desde el dominio temporal?
  - La Transformada de Fourier es superior cuando la información crítica de la señal no es evidente en su amplitud a través del tiempo, sino en su composición espectral.Análisis de Señales Biológicas:
    1. Permite identificar frecuencias específicas asociadas a ritmos fisiológicos (como en un ECG o EEG) que en el tiempo parecen ruido.
    2. Detección de Patologías: Ciertas enfermedades alteran el espectro de frecuencia de una señal biomédica, ofreciendo un mayor poder discriminativo para el diagnóstico que el análisis temporal simple.
    3. Filtro de Ruido Estacionario: Cuando el ruido ocurre a una frecuencia específica, es mucho más fácil identificarlo y eliminarlo en el dominio de la frecuencia.
- ¿En qué se diferencia la correlación cruzada de la convolución?
  - Aunque matemáticamente son muy similares, su propósito y una diferencia técnica en el cálculo las distinguen:
    1. Propósito: La convolución busca determinar la respuesta de un sistema ante una entrada (filtrado) , mientras que la correlación funciona como una medida de similitud para encontrar qué tanto se parecen dos señales.
    2. Inversión de la señal: En la convolución manual, una de las señales se debe invertir o "voltear" en el tiempo ($h[n-k]$) antes de deslizarla. En la correlación cruzada, las señales se comparan directamente sin invertir ninguna para ver cómo se alinean sus formas originales.
## Referencias:
* <a name="ref-Data"></a> **Data Science Python Blog.** (s.f.). Correlación cruzada. Recuperado el 5 de marzo de 2026 de  
https://datasciencepythonblog.net/correlacion-cruzada/

* <a name="ref-universidad"></a> **Universidad Autónoma de Baja California.** (2020). Procesamiento digital de señales biofisiológicas.  
https://citecuvp.tij.uabc.mx/bio/wp-content/uploads/2020/07/11808-Procesamiento-Digital-de-Se%C3%B1ales-Biofisiol%C3%B3gicas.pdf

* <a name="ref-uni"></a> **Universidad Central del Ecuador.** (s.f.). Análisis de correlación cruzada en procesamiento de señales.  
https://www.dspace.uce.edu.ec/bitstreams/77295fb1-b3d8-4b02-a060-83439c01bd7e/download
