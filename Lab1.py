# Importar paquete wfdb para leer "rec" de physionet
import wfdb
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats

#Cargar la informacion (hay dque tener los archivos .dat y .hea)

signal = wfdb.rdrecord('023995BE-51ED-4D1B-A966-610925F79203')

#Obtenemos valores de Y de la señal
valores = signal.p_signal[:,0] #para que el vector empiece en 0
tamano = signal.sig_len #numero de muestras

plt.plot(valores, color='#ff33c1')
plt.title('Onda ECG')
plt.xlabel('Milisegundos (ms)')
plt.ylabel('Milivoltios (mV)')
plt.show()

media = np.mean(valores)
desviacion_estandar = np.std(valores)
coeficiente_Des=desviacion_estandar/media

#media
n = len(valores)  
suma = np.sum(valores)  
media_cal = suma / n

#desviacion
suma_cuadradas = np.sum((valores - media) ** 2  )
desviacionestandar_mat = np.sqrt(suma_cuadradas / (n - 1)) 

#coeficiente de desviación
coeficiente= desviacionestandar_mat/media_cal

#histograma
fig,ax = plt.subplots()
ax.hist(valores,color="pink", edgecolor='black')
plt.title('HISTOGRAMA')
plt.show()

 
#HISTOGRAMA CALCULADO
# rango de los datos
min_value = min(valores)
max_value = max(valores)
# Definir los bins
num_bins = 10
bin_width = (max_value - min_value) / num_bins
bins = [min_value + i * bin_width for i in range(num_bins + 1)]
# Contar los datos en cada bin
counts = [0] * num_bins
for value in valores:
    for i in range(num_bins):
        if bins[i] <= value < bins[i + 1]:
            counts[i] += 1
            break

plt.bar(bins[:-1], counts, width=bin_width, color='#ae11dc',edgecolor='black', label='Histograma')
plt.title('Señal con Ruido de Impulso')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()
        

#Función de probabilidad
pdf = stats.norm.pdf(valores, loc=np.mean(valores), scale=np.std(valores),)

plt.plot(valores, pdf,color='#33ffbe')
plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.title('FUNCIÓN DE PROBABILIDAD')
plt.show()



#ruido gaussiano

N= signal.sig_len   
N= signal.sig_len
x= np.random.randn(N)
Ruidonormalizado=(x*0.005)/max(valores)
plt.plot(Ruidonormalizado, '.-')


#Grafca
plt.plot(Ruidonormalizado,  linestyle='-.', color='blue')
plt.plot(valores, label='Señal Original', color='red')
plt.title('Señal Original y Ruido Gaussiano')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()

#Suma de señales
señal_con_ruido = valores + Ruidonormalizado
plt.plot(señal_con_ruido, '.-', label='Señal con Ruido', color='magenta')
plt.title('Señal con Ruido Gaussiano')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()

#Suma de señales neg
señal_ruido = valores + x
plt.plot(señal_ruido, '.-', label='Señal con Ruido', color='#33e3ff')
plt.title('Señal con Ruido Gaussiano Amplificado ')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()

#SNR Gaussiano
pot_val= ((np.sum(abs(valores)))**2)/n
pot_ruido = ((np.sum(abs(Ruidonormalizado)))**2)/N
pot_ruidoneg = ((np.sum(abs(x)))**2)/N

print("+ Potencia valores:", pot_val)
print("+ Potencia ruido:", pot_ruido)

SNR = 10* math.log10((pot_val/pot_ruido))
SNR_neg = 10* math.log10((pot_val/pot_ruidoneg))

#RUIDO DE IMPULSO 
num_impulsos = 50
amplitud_impulso = 0.3
posiciones = np.random.choice(N, num_impulsos, replace=False)
ruido_impulso = np.zeros(N)
ruido_impulso[posiciones] = amplitud_impulso

Ruido_max=(ruido_impulso*1)/max(valores)

plt.plot(ruido_impulso, label='Ruido de Impulso', color='#ca94e7',  linestyle='-.')
plt.plot(valores, label='Señal Original', color='#e948ce')
plt.title('Señal con Ruido de Impulso')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()

#Suma de señales
señal_con_impulso = valores + ruido_impulso
plt.plot(señal_con_impulso, '.-', color='#fa68a9')
plt.title('Señal con Ruido de impulso')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.show()

#Suma de señales neg
señal_con_impulso_neg= valores + Ruido_max
plt.plot(señal_con_impulso_neg, '.-', color='#83fbb4')
plt.title('Señal con Ruido de Impulso Amplificado')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.show()
#SNR Impulso

pot_ruido_imp= ((np.sum(abs(ruido_impulso)))**2)/N
pot_ruid_neg=  ((np.sum(abs(Ruido_max)))**2)/N
print("+ Potencia ruido impulso:", pot_ruido_imp)

SNR2 = 10* math.log10((pot_val/pot_ruido_imp))
SNR2_neg = 10* math.log10((pot_val/pot_ruid_neg))

#Senal de ruido artefacto
frecuencia_artefacto = 0.02
amplitud_onda = 0.03
t = np.arange(N)
artefacto_onda = amplitud_onda * np.sin(2 * np.pi * frecuencia_artefacto * t)
probabilidad_mostrar = 0.81
mask = np.random.rand(N) > probabilidad_mostrar
artefacto_intervalos = np.where(mask, artefacto_onda, 0)

ruido_art_max=(artefacto_intervalos*5)/max(valores)

plt.plot(artefacto_intervalos, label='Artefacto Periódico', color='#fa6875', linestyle='-.')
plt.plot(valores, label='Señal Original',color='#ab68fa')
plt.title('Señal Original y Señal con Artefacto')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()

# Suma señales
señal_con_artefacto = valores + artefacto_intervalos

plt.plot(señal_con_artefacto, label='Señal con Artefacto', color='#68a5fa')
plt.title('Señal con Ruido de Artefacto')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV')
plt.legend()
plt.show()

# Suma señales
señal_con_artefacto_neg = valores + ruido_art_max

plt.plot(señal_con_artefacto_neg, label='Señal con Artefacto', color='#68fad8')
plt.title('Señal con Ruido de Artefacto Amplificado')
plt.xlabel('Muestras (ms)')
plt.ylabel('Valor (mV)')
plt.legend()
plt.show()


#SNR Artefacto
pot_val = ((np.sum(abs(valores)))**2) / n
pot_artefacto = ((np.sum(abs(artefacto_intervalos)))**2) / n
pot_artefacto_neg = ((np.sum(abs(ruido_art_max)))**2) / n
print("+ Potencia Artefacto:",pot_artefacto)
SNR3 = 10 * math.log10(pot_val / pot_artefacto)
SNR3_neg = 10 * math.log10(pot_val / pot_artefacto_neg)

print(" - Media de la señal:", media_cal)
print(" - Desviación estándar de la señal:", desviacionestandar_mat)
print(" - Coeficiente De Desviación de la señal",coeficiente)

print(" * Media:", media)
print(" * Desviación estándar:", desviacion_estandar)
print(" * Coeficiente De Desviación",coeficiente_Des)

print("SNR Gaussiano (positivo):", SNR)
print("SNR Impulso (positivo):", SNR2)
print("SNR Artefacto (positivo):", SNR3)

print("SNR Gaussiano (negativo):", SNR_neg)
print("SNR Impulso (negativo):", SNR2_neg)
print("SNR Artefacto (negativo):", SNR3_neg)