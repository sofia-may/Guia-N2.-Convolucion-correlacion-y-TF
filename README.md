# Guia-N2.-Convolucion-correlacion-y-TF
## Parte A

### A MANO

### EN PYTHON
<img width="1935" height="1330" alt="parte_A_convolucion" src="https://github.com/user-attachments/assets/91bf9325-8e2c-4ea9-934d-e1a188fa690a" />
en la imagen se muestra la grafica de h[n], la grafica de x[n] y la grafica de la convolucion entre ellas.

### Conclucion

## PARTE B

## SOFI ACA TOCA INVESTIGA SOBRE LA CORRELACION CRUZADA Y COLOCARLO ANTES DE LA PARTE A, COMO UN MARCO TEORICO

#### correlacion cruzada

calculamos los componentes de las dos señales y aplicamos la correlacion cruzada entre las dos.

<img width="635" height="276" alt="image" src="https://github.com/user-attachments/assets/5784c1c2-eb01-4b90-9505-a9d3e1ccbb76" />


<img width="310" height="326" alt="image" src="https://github.com/user-attachments/assets/02092b0e-2462-4b70-842f-7ae8f9853368" />

graficamos los datos optenidos:
<img width="1785" height="1330" alt="parte_B_correlacion" src="https://github.com/user-attachments/assets/c0aea5d0-edf4-42bd-ad1b-955d9cf2a268" />
segun el "lag" evidenciamos  que en 2 es donde mas se parecen las dos señales

#### Descripcion

La correlacion cruzada entre coseno y seno de la misma frecuencia produce una secuencia que refleja el desfase de 90° (π/2 rad) entre ambas señales. El valor maximo de |R X1 y X2| ocurren en el lag donde las señales tienen mayor similitud desplazada, y la secuencia es antisimetrica respecto al lag=0, lo cual es caracteristico de dos señales en cuadratura (desfasada 90°).

 #### ¿En que situaciones es util la correlacion cruzada?

 - Deteccion de retardo entre señales: permite identificar cuanto tiempo tarda una señal en llegar a otro sensor. Por Ejemplo: localizacion de fuentes sonoras o sismicas
   
 - Identificacion de similitud entre señales: util para comparar una señal de referencia con una señal ruidosa y determinar si contiene el patron buscado.
   
 - Procesamiento de señales biomedicas: por ejemplo, para detectar relaciones entre dos canales de EEG, o entre una señal de estimulacion y la respuesta fisiológica.
 
 - Radar y sonar: para estimar la distancia a un objeto correlacionando la señal emitida con el eco recibido.
 
 -   Comunicaciones: para sincronizacion y deteccion de señales en presencia de ruido e interferencias.
