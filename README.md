###ANÁLISIS ESTADÍSTICO DE LA SEÑAL
En el primer laboratorio de procesamiento de señales digitales se busca describir una señal biomédica a partir de variables estadísticas.
Para la primera parte del codigo, se seleccionado libremente en la plataforma PhysioNet una señal, específicamente de la base de datos ECGDMMLD. Esta base de datos incluye datos de un ensayo clínico aleatorizado, realizado en 5 períodos, con 22 sujetos sanos de ambos sexos, con edades entre 18 y 35 años. El objetivo del estudio es comparar la respuesta electrofisiológica de los fármacos bloqueadores de los canales de potasio, tanto con o sin la adición de fármacos bloqueadores tardíos de los canales de sodio o calcio. Para el laboratorio, se utilizaron los datos del primer paciente del estudio.

La señal seleccionada fue importada y graficada en Python utilizando el compilador Spyder. Para la elaboración del código, fue necesario importar cinco librerías:

######•	wfdb: Útil para trabajar con bases de datos de señales fisiológicas.
###### •	numpy: Una biblioteca fundamental para la computación matemática, que proporciona soporte para arreglos y matrices.
###### •	math: Útil para realizar una amplia variedad de operaciones matemáticas.
###### •	matplotlib.pyplot: Utilizada para crear gráficos y visualizaciones de datos.
###### •	scipy.stats: Parte del paquete SciPy, proporciona una amplia variedad de funciones y herramientas para realizar análisis estadísticos en Python.


![](https://imgur.com/h7IKREL.png)
> Señal ECG.

Posteriormente en el codigo, se calcularon los estadísticos descriptivos de dos maneras: utilizando comandos y librerías de Python, y aplicando fórmulas manualmente.
En primer lugar, se calculó la** media**, que es una medida de tendencia central que representa el valor promedio de un conjunto de datos.
Así mismo, se determinó la **desviación estándar**, una medida estadística que cuantifica la variabilidad o dispersión de los datos respecto a su media.
El **coeficiente de variación (CV)** es otra medida estadística que expresa la desviación estándar en relación con la media del conjunto de datos, y se emplea para comparar la variabilidad entre diferentes conjuntos de datos.
Además, se utilizó un **histograma** como herramienta gráfica para representar la distribución de los datos. El histograma muestra la frecuencia de los datos dentro de intervalos o rangos específicos, proporcionando una visualización clara de la distribución de los valores en el conjunto de datos.
![](https://imgur.com/UaovcLA.png)


 
La **función de probabilidad **es una función matemática que tiene como objetivo describir la probabilidad de que una variable aleatoria tome un valor específico o se encuentre dentro de un intervalo de valores
![](https://imgur.com/wzJz8V4.png)
>Función de probabilidad con una curva desplazada hacia la izquierda

Para la segunda parte del codigo tenemos los ruidos añadidos a la señal, tambien se calculo el SNR (Signal-to-Noise Ratio), tanto de la señal con un ruido “normal” tanto como con un ruido amplificado. Este fue calculado mediante el logaritmo en base 10 de la potencia de la señal sobre la protencia del ruido multimplicado por 10
SNR= 10 log10(P_señal/P_Ruido)

**RUIDO GAUSSIANO**
Es un ruido con una distribución normal o gaussiana. El cual se caracteriza por su forma de campana y se distribuye de manera simétrica al rededor de la media.
Como observamos a continuacion, tenemos 2 graficas, en la que se evidencia el ruido sumado a la señal y en la tercera el ruido amplificado, donde este es mas grande que la señal, a partir de estos ruidos se calculo la relacion señal-ruido (SNR) donde, en la primera se puuede observar que al ser el SNR positivo la señal está clara, pero el ruido gaussiano afecta la calidad de la señal, mientras que, el SNR negativo del ruido gaussiano es el más bajo (segunda imagen). Esto indica que la señal está extremadamente afectada por el ruido gaussiano en esta condición negativa, con la señal apenas perceptible sobre el ruido.
![](https://imgur.com/UFPN4qf.png)
  
**RUIDO DE IMPULSO**
Este ruido se caracteriza por la presencia de picos de gran amplitud o impulsos que se introducen de manera espontanea en la señal.
Como se puede observar, el SNR de Impulso positivo es mucho más alto que el SNR de Impulso negativo. Esto muestra que el impacto del ruido de impulso es mucho menor en condiciones positivas comparado con las negativas, sin embargo aun se distorciona la señal original. En condiciones negativas, el ruido impulsivo aún afecta la señal de manera significativa, pero la señal es relativamente más clara en comparación con el ruido gaussiano en condiciones negativas, ya que en el ruido los impulsos son mas positivos mientras que en el gausiano tiene parte negativa, la cual puede dirtorcionar aun mas la señal.
  ![](https://imgur.com/N7cYTFY.png)

**RUIDO DE ARTEFACTO**
Este se refiere a distorsiones no deseadas en los datos que pueden ser causadas por errores en el equipo o interferencias.
En la primera imagen podemos observar el ruido de artefacto el cual tiene un SNR positivo cercano a los 17,3 dB, lo cual indica que el ruido artefacto tiene el menor impacto en la señal, por lo cual a señal es mas clara con respecto a este ruido, mientras que en la segunda imagen el ruido es mayor a la señal, por lo cua esta se distorciona mucho mas y es mas dificil reconocer la señal original 

  ![](https://imgur.com/EO3OQgo.png)
   
### INSTRUCCIONES 
El codigo se realizo descargando una señal desde la pagina de physionet, se descargaron los archivos .dat y .hea
En caso de descargar otra señal, cambiar el nombre de la señal:
>	 signal = wfdb.rdrecord( '______' )

