

#-*-coding: utf-8-*-

#1 pixel equivale a 1/119 metros
#1 frame  equivale a 1/24 seg
import re
import numpy as np
import matplotlib.pyplot as plt

g_estimadas = []

"""

for i in range(6):

    trajectory = "trajectory"+str(i+1)+".dat"
    f_1 = open(trajectory, "r")
    list_time_1 = []
    list_position_1 = []
    for line in f_1:
	    line = re.findall('\w+', line)
	    if(int(line[1])<=400):
		    list_time_1.append(float(line[0])*(1/24))
		    list_position_1.append(2.353-(float(line[2])*(1/119)))


    coeficientes_1 = np.polyfit(list_time_1, list_position_1, 2)

    g_1 = 2.*coeficientes_1[0]
    g_estimadas.append(g_1)
    f_1.close()

print(g_estimadas)

"""
trajectory = "trajectory1.dat"
f_1 = open(trajectory, "r")
list_time_1 = []
list_position_1 = []
for line in f_1:
    line = re.findall('\w+', line)
    if(int(line[1])<350):
	    list_time_1.append(float(line[0])*(1/24))
	    list_position_1.append(2.353-(float(line[2])*(1/119)))


coeficientes_1 = np.polyfit(list_time_1, list_position_1, 2)
print(coeficientes_1)
g_1 = 2.*coeficientes_1[0]
g_estimadas.append(g_1)
f_1.close()

y1=[coeficientes_1[0]*(i**2)+coeficientes_1[1]*i+coeficientes_1[2] for i in list_time_1]



x =list_time_1
y=list_position_1
plt.figure()
plt.xlabel(r"$Time(s)$", fontsize = 24, color = 'black')
plt.ylabel(r"$Position(m)$", fontsize = 24, color = 'black')

plt.plot(x, y, 'm-', linewidth = 2, label = 'G calculada')
plt.plot(x, y1, 'c-', linewidth = 2, label = 'G estándar')
plt.legend(loc = 4)
plt.show()


