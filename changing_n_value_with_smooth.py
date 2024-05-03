import xlrd as x

loc_file = ("D:\LearningPython\AverageRSSI.xlsx")
wb = x.open_workbook(loc_file)
sheet = wb.sheet_by_index(0)

avg_power=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print("Direct RSSI :")
print(avg_power)
print("Total Number of Received APs")
print(len(avg_power))

lst = []
smooth = []

import numpy as np
for i in range(len(avg_power)):

    a = avg_power[i]
    lst.append(a)
    avg = np.mean(lst)
    RSSIsmooth = 0.75 * (a) + (1 - 0.75) * (avg)
    smooth.append(RSSIsmooth)
print("Smooth RSSI :")
print(smooth)





#FINDING NOISE POWER

import math
noise_power = -174 + 10*math.log10(2400000000)
print ("Noise Power : ", end="")
print (noise_power)

#FINDING SINR

SINR=[]
listt=[]

for i in range(len(avg_power)):
 k=avg_power[i]
 listt.append(k)
 SINRR= k/noise_power
 SINR.append(SINRR)

print ("Given SINR : ", end="")
print(SINR)


#FINDING SNR MARGIN

listtt=[]
SNR_margin=[]
SNR=[]
for i in range(len(avg_power)):
 h= avg_power[i]
 listtt.append(h)
 SNR=h-noise_power
 SNR_margin.append(SNR)

print ("Given SNR MARGIN : ", end="")
print(SNR_margin)


#INCREASE SNR MARGIN BY 10

SNR_margin10=[]
liist=[]
for i in range(len(SNR_margin)):

 a=SNR_margin[i]
 liist.append(a)

 SNR_margin2= a+10
 SNR_margin10.append(SNR_margin2)

print ("Increase SNR MARGIN by 10  : ", end="")
print(SNR_margin10)


#IMPROVED SIGNAL STRENGTH

Improved_RSSI=[]
liist=[]

for i in range(len(SNR_margin10)):
  j=SNR_margin10[i]
  liist.append(j)
  avg_power= j+noise_power
  Improved_RSSI.append(avg_power)

print ("Improved Avg Power : ", end="")
print(Improved_RSSI)


#IMPROVED RSSI and Smoothing

lst = []
improved_smooth = []

import numpy as np
for i in range(len(Improved_RSSI)):

    a = Improved_RSSI[i]
    lst.append(a)
    avg = np.mean(lst)
    RSSIsmooth = 0.75 * (a) + (1 - 0.75) * (avg)
    improved_smooth.append(RSSIsmooth)
print("Improved Smooth RSSI :", end="")
print(improved_smooth)



#pathloss at Smooth RSSI

#when n = 1.7

liist = []
distance0 = []
z = []
for i in range(len(smooth)):

   n0=1.7
   A = -36  #A is a reference received signal strength in dBm
   h=smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n0))
   distance0.append(z)
print("Distance at n= 1.7: ")
print(distance0)

#when n = 1.8

liist = []
distance1 = []
z = []
for i in range(len(smooth)):

   n1=1.8
   A = -36  #A is a reference received signal strength in dBm
   h=smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n1))
   distance1.append(z)

print("Distance at n= 1.8: ")
print(distance1)

#when n = 1.9

liist = []
distance2 = []
z = []
for i in range(len(smooth)):

   n2=1.9
   A = -36  #A is a reference received signal strength in dBm
   h=smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n2))
   distance2.append(z)

print("Distance at n= 1.9: ")
print(distance2)

#when n = 2

liist = []
distance3 = []
z = []
for i in range(len(smooth)):

   n3=2
   A = -36  #A is a reference received signal strength in dBm
   h=smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n3))
   distance3.append(z)

print("Distance at n= 2: ")
print(distance3)


#Improving and smoothing RSSI

#FINDING NOISE POWER

import math
noise_power = -174 + 10*math.log10(2400000000)
print ("Noise Power : ", end="")
print (noise_power)



print ("Given Avg Power : ", end="")
avg_power=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print(avg_power)

#FINDING SNR MARGIN

listtt=[]
SNR_margin=[]
SNR=[]
for i in range(len(avg_power)):
 h= avg_power[i]
 listtt.append(h)
 SNR=h-noise_power
 SNR_margin.append(SNR)

print ("Given SNR MARGIN : ", end="")
print(SNR_margin)


#INCREASE SNR MARGIN BY 10

SNR_margin10=[]
liist=[]
for i in range(len(SNR_margin)):

 a=SNR_margin[i]
 liist.append(a)

 SNR_margin2= a+10
 SNR_margin10.append(SNR_margin2)

print ("Increase SNR MARGIN by 10  : ", end="")
print(SNR_margin10)


#IMPROVED SIGNAL STRENGTH

Improved_RSSI=[]
liist=[]

for i in range(len(SNR_margin10)):
  j=SNR_margin10[i]
  liist.append(j)
  avg_power= j+noise_power
  Improved_RSSI.append(avg_power)

print ("Improved Avg Power : ", end="")
print(Improved_RSSI)


#IMPROVED RSSI and Smoothing

lst = []
improved_smooth = []

import numpy as np
for i in range(len(Improved_RSSI)):

    a = Improved_RSSI[i]
    lst.append(a)
    avg = np.mean(lst)
    RSSIsmooth = 0.75 * (a) + (1 - 0.75) * (avg)
    improved_smooth.append(RSSIsmooth)
print("Improved Smooth RSSI :", end="")
print(improved_smooth)


#pathloss at Improved Smooth RSSI

#when n = 1.7

liist = []
distance00 = []
z = []
for i in range(len(improved_smooth)):

   n0=1.7
   A = -36  #A is a reference received signal strength in dBm
   h=improved_smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n0))
   distance00.append(z)
print("Distance at n= 1.7: ")
print(distance00)

#when n = 1.8

liist = []
distance11 = []
z = []
for i in range(len(improved_smooth)):

   n1=1.8
   A = -36  #A is a reference received signal strength in dBm
   h=improved_smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n1))
   distance11.append(z)

print("Distance at n= 1.8: ")
print(distance11)

#when n = 1.9

liist = []
distance22 = []
z = []
for i in range(len(improved_smooth)):

   n2=1.9
   A = -36  #A is a reference received signal strength in dBm
   h=improved_smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n2))
   distance22.append(z)

print("Distance at n= 1.9: ")
print(distance22)

#when n = 2

liist = []
distance33 = []
z = []
for i in range(len(improved_smooth)):

   n3=2
   A = -36  #A is a reference received signal strength in dBm
   h=improved_smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n3))
   distance33.append(z)

print("Distance at n= 2: ")
print(distance33)

#Ploting at Smooth RSSI

import matplotlib.pyplot as plt

print ("Given Avg Power : ", end="")
avg_power=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print(avg_power)

plt.scatter(avg_power,distance0, label= " RSSI: n=1.7", color= "green",
            marker= "*", s=50)

plt.scatter(avg_power,distance1, label= " RSSI: n=1.8", color= "red",
            marker= "*", s=50)


plt.scatter(avg_power,distance2, label= " RSSI: n=1.9", color= "blue",
            marker= "*", s=30)

plt.scatter(avg_power,distance3, label= " RSSI: n=2", color= "yellow",
            marker= "*", s=10)

#plt.plot(data,distance2, label= "Direct RSSI")
#plt.plot(smooth,distance, label= "Smooth RSSI")

plt.title('RSSI VS DISTANCE')
plt.xlabel('RSSI')
plt.ylabel('Distance')
plt.legend()
plt.show()




#Ploting at Improved Smooth RSSI

import matplotlib.pyplot as plt


plt.scatter(improved_smooth,distance00, label= "Smooth RSSI: n=1.7", color= "green",
            marker= "*", s=50)

plt.scatter(improved_smooth,distance11, label= "Smooth RSSI: n=1.8", color= "red",
            marker= "*", s=50)


plt.scatter(improved_smooth,distance22, label= "Smooth RSSI: n=1.9", color= "blue",
            marker= "*", s=30)

plt.scatter(improved_smooth,distance33, label= "Smooth RSSI: n=2", color= "yellow",
            marker= "*", s=10)

#plt.plot(data,distance2, label= "Direct RSSI")
#plt.plot(smooth,distance, label= "Smooth RSSI")

plt.title('RSSI VS DISTANCE')
plt.xlabel('Improved Smooth RSSI')
plt.ylabel('Distance')
plt.legend()
plt.show()
