

#-*-coding: utf-8-*-

#1 pixel equivale a 1/119 metros
#1 frame  equivale a 1/24 seg
import re
import numpy as np
import matplotlib.pyplot as plt

g_estimadas = []



for i in range(6):

    trajectory = "trajectory"+str(i+1)+".dat"

    f = open(trajectory, "r")
    list_time_1 = []
    list_position_1 = []
    for line in f:
	    line = re.findall('\w+', line)
	    if(int(line[1])<=400):
             list_time_1.append(float(line[0])*(1/24))
             list_position_1.append(2.353-(float(line[2])*(1/240)))



    coeficientes_1 = np.polyfit(list_time_1, list_position_1, 2)

    g_1 = -2.*coeficientes_1[0]
    g_estimadas.append(g_1)
    f.close()
print("G calculadas\n")
print(g_estimadas)

#Media aritmetica
suma=0
for i in range(6):
    suma += g_estimadas[i]
media_arit = suma/6.
print("Promedio: "+str(media_arit)+("\n"))

#Ahora calculamos la desviacion estandar
aux_de =0
for i in g_estimadas:
    x=(i-media_arit)
    aux_de+= pow(x,2)
aux_de = aux_de/7
desviacion_estandar = pow(aux_de, 0.5)

print("Desviación estándar: "+str(desviacion_estandar)+"\n")


#Ahora compararemos el valor medido de g con: g= GM/R^2
#con M: masa de la tierra
#    G: constante gravitacional
#    R: radio de la tierra en el ecuador

M=5.972*pow(10,24)
G=6.67392*(pow(10,-11))
R=6378000
g_est = (M*G)/(pow(R,2))
print(g_est)

print("G promedio calculada: "+str(media_arit)+"\nG estimada: "+str(g_est))
#Grafica
###############################################
trajectory = "trajectory1.dat"
f_1 = open(trajectory, "r")
list_time = []
list_position = []
for line in f_1:
    line = re.findall('\w+', line)
    if(int(line[1])<400):
        if (2.353-(float(line[2])*(1/119))) not in list_position:
    	    list_time.append(float(line[0])*(1/24))
    	    list_position.append(2.353-(float(line[2])*(1/240)))


coeficientes = np.polyfit(list_time, list_position, 2)
#print(coeficientes_1)
#_1 = 2.*coeficientes_1[0]
#g_estimadas.append(g_1)
f_1.close()


y1=[coeficientes[0]*(i**2)+coeficientes[1]*i+coeficientes[2] for i in list_time]



x =list_time
y=list_position
plt.figure()
plt.xlabel(r"$Time(s)$", fontsize = 24, color = 'black')
plt.ylabel(r"$Position(m)$", fontsize = 24, color = 'black')

plt.plot(x, y, 'm-', linewidth = 2, label = 'G calculada')
plt.plot(x, y1, 'c-', linewidth = 2, label = 'G estándar')
plt.legend(loc = 4)
plt.show()
#################################################################
