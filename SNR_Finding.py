import xlrd as x

#Uploading WiFi DATA INTO PYTHON

loc_file = ("D:\LearningPython\AverageRSSIUpdated.xlsx")
wb = x.open_workbook(loc_file)
sheet = wb.sheet_by_index(0)

#EXTRACTING RSSI DATA FROM EXCEL

print ("Given Avg Power : ", end="")
avg_power=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print(avg_power)
print ("Length of Data : ", end="")
print(len(avg_power))

#RSSI SMOOTHING

lst = []
smooth = []

import numpy as np
for i in range(len(avg_power)):

    a = avg_power[i]
    lst.append(a)
    avg = np.mean(lst)
    RSSIsmooth = 0.75 * (a) + (1 - 0.75) * (avg)
    smooth.append(RSSIsmooth)
print("Smooth RSSI :", end="")
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




#IMPROVED SINR

improved_SINR=[]
liist=[]

for i in range(len(Improved_RSSI)):
 k=Improved_RSSI[i]
 liist.append(k)
 SINRR= k/noise_power
 improved_SINR.append(SINRR)

print ("Improved SINR : ", end="")
print(improved_SINR)



#Finding Distances



liist = []
distance1 = []
z = []
for i in range(len(Improved_RSSI)):

   n=2
   A = -36  #A is a reference received signal strength in dBm
   h=Improved_RSSI[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n))
   distance1.append(z)

print("Distance at Improved_RSSI ")
print(distance1)



print ("Given Avg Power : ", end="")
avg_power=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print(avg_power)


liist = []
distance = []
z = []
for i in range(len(avg_power)):

   n=2
   A = -36  #A is a reference received signal strength in dBm
   h=avg_power[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n))
   distance.append(z)

print("Distance at Direct_RSSI ")
print(distance)



from pandas import DataFrame

Results1 = {
             'SNR Margin': SNR_margin,
             'Improved SNR Margin': SNR_margin10,

             'Distance Direct': distance,
             'Distance Improved': distance1,

            }

df = DataFrame(Results1, columns= [ 'SNR Margin', 'Improved SNR Margin',
                                    'Distance Direct','Distance Improved'])
print (df)


Results = {
             'RSSI': avg_power,
             'Improved RSSI': Improved_RSSI,

             'SINR': SINR,
             'Improved SINR': improved_SINR,

            }

df = DataFrame(Results, columns= ['RSSI', 'Improved RSSI','SINR','Improved SINR'])

print (df)


#Calculating RMSE
import numpy as np

listOfStrings2 = [-50 for i in range(213)]
y = np.array(listOfStrings2)
yhat = np.array(avg_power)

# calculate accuracy for Direct RSSI
d = y-yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)

print("MAE:",mae_f)
print("MSE:", mse_f)
print("RMSE:", rmse_f)

# calculate accuracy for Improved RSSI
y = np.array(listOfStrings2)
yhat = np.array(Improved_RSSI)
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)

print("MAE:",mae_f)
print("MSE:", mse_f)
print("RMSE:", rmse_f)

#Plotting
x = list(range(len(distance)))
import matplotlib.pyplot as plt

#plt.scatter(x, distance, color="blue", label="Direct Distance")
plt.plot(x, distance, color="blue", label="Direct Distance")
plt.plot(x, distance1, color="red", label="Improved Distance")
plt.xlabel('Data Index')
plt.ylabel('Distance')
plt.legend()
plt.show()

plt.plot(x, avg_power, color="blue", label="Direct RSSI")
plt.plot(x, Improved_RSSI, color="red", label="Improved RSSI")
plt.xlabel('Data Index')
plt.ylabel('RSSI')
plt.legend()
plt.show()

plt.plot(x,SINR, color="blue", label="Direct SINR")
plt.plot(x, improved_SINR, color="red", label="Improved SINR")
plt.xlabel('Data Index')
plt.ylabel('SINR')
plt.legend()
plt.show()

plt.plot(x,SNR_margin, color="blue", label="Direct SIN Margin")
plt.plot(x, SNR_margin10, color="red", label="Improved SINR Margin")
plt.xlabel('Data Index')
plt.ylabel('SNR Margin')
plt.legend()
plt.show()

plt.plot(x,avg_power, color="blue", label="Direct RSSI")
plt.plot(x, smooth, color="red", label="Smooth RSSI")
plt.plot(x,Improved_RSSI, color="green", label="Improved RSSI")
plt.plot(x,improved_smooth, color="yellow", label="Proposed Method")
plt.xlabel('Data Index')
plt.ylabel('RSSI')
plt.legend()
plt.show()
