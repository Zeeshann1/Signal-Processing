import xlrd as x
import matplotlib.pyplot as plt
#Exporting RSSI

loc_file = ("D:\LearningPython\AverageRSSI.xlsx")
wb = x.open_workbook(loc_file)
sheet = wb.sheet_by_index(0)


AverageRSSI=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print ("Average RSSI : ", end="")
print(AverageRSSI)
print ("Length of Data : ", end="")
print(len(AverageRSSI))


#Exporting Signal Quality

loc_file = ("D:\LearningPython\AverageSignalQuality.xlsx")
wb = x.open_workbook(loc_file)
sheet = wb.sheet_by_index(0)

AverageSignalQuality=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print ("Average Signal Quality : ", end="")
print(AverageSignalQuality)


liist = []
SignalQuality = []
z = []
for i in range(len(AverageRSSI)):

   h=AverageRSSI[i]
   liist.append(h)
   z= 2*(h+100)
   SignalQuality.append(z)
print(" Signal Quality Using Average RSSI: ", end="")
print( SignalQuality)

#Plotting Signal Quality
x = list(range(len(SignalQuality)))
import matplotlib.pyplot as plt

#plt.scatter(x, distance, color="blue", label="Direct Distance")
plt.plot(x, AverageSignalQuality, color="blue", label="Direct Average Signal Quality")
plt.plot(x, SignalQuality, color="red", label="Average Signal Quality Using Average RSSI")
plt.xlabel('Data Index')
plt.ylabel('Average Signal Quality VS Average RSSI')
plt.legend()
plt.show()

#Improving and Smoothing RSSI

#FINDING NOISE POWER

import math
noise_power = -174 + 10*math.log10(2400000000)
print ("Noise Power : ", end="")
print (noise_power)

#FINDING SNR MARGIN

listtt=[]
SNR_margin=[]
SNR=[]
for i in range(len(AverageRSSI)):
 h= AverageRSSI[i]
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


#IMPROVED RSSI

Improved_RSSI=[]
liist=[]

for i in range(len(SNR_margin10)):
  j=SNR_margin10[i]
  liist.append(j)
  AverageRSSI= j+noise_power
  Improved_RSSI.append(AverageRSSI)

print ("Improved RSSI Using Signal Quality Parameter SNR margin : ", end="")
print(Improved_RSSI)



#Smothing RSSI

lst = []
smooth = []

import numpy as np
for i in range(len(Improved_RSSI)):

    a = Improved_RSSI[i]
    lst.append(a)
    avg = np.mean(lst)
    RSSIsmooth = 0.75 * (a) + (1 - 0.75) * (avg)
    smooth.append(RSSIsmooth)
print(" Improved and Smooth RSSI: ", end="")
print(smooth)



#plt.plot(x, AverageRSSI, color="green", label=" Direct Average RSSI")
plt.plot(x, Improved_RSSI, color="blue", label=" Improved RSSI")
plt.plot(x, smooth, color="red", label="Improved and Smooth RSSI")
plt.xlabel('Data Index')
plt.ylabel('RSSI Smoothing and Improving')
plt.legend()
plt.show()




liist = []
SmoothSignalQuality = []
z = []
for i in range(len(smooth)):

   h=smooth[i]
   liist.append(h)
   z= 2*(h+100)
   SmoothSignalQuality.append(z)
print(" Signal Quality With Improved and Smooth RSSI: ", end="")
print( SmoothSignalQuality)


#Plotting with RSSI smooth
x = list(range(len(smooth)))
import matplotlib.pyplot as plt

plt.plot(x, AverageSignalQuality, color="blue", label=" Direct Average Signal Quality")
plt.plot(x, SmoothSignalQuality, color="red", label=" Signal Quality Using Proposed Method ")
plt.xlabel('Data Index')
plt.ylabel('  Signal Quality ')
plt.legend()
plt.show()


plt.plot(x, SignalQuality, color="blue", label=" Signal Quality Using Average RSSI")
plt.plot(x, SmoothSignalQuality, color="red", label=" Signal Quality Using Improved and Smooth RSSI")
plt.xlabel('Data Index')
plt.ylabel(' Signal Quality ')
plt.legend()
plt.show()



plt.plot(x, AverageRSSI, color="blue", label="Direct RSSI")
plt.plot(x, Improved_RSSI, color="red", label="Improved RSSI")
plt.xlabel('Data Index')
plt.ylabel('RSSI')
plt.legend()
plt.show()

