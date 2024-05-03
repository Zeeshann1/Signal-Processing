import numpy as np



print("===================Near HL Lab==========================")

a=[14,16]
y = np.array(a)
yhat = np.array([15.15,15.66])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)


print("Actual Position :", y)
print("Actual Position :", yhat)

print("RMSE Error:", rmse_f)

print("========================Staff Rooms=====================")


a=[25,5.5]
y = np.array(a)
yhat = np.array([25.05,6.72])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)


print("Actual Position :", y)
print("Actual Position :", yhat)

print("RMSE Error:", rmse_f)

print("=======================Corridor 1=====================")


a=[24.5,6.7]
y = np.array(a)
yhat = np.array([22.67,7.14])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)


print("Actual Position :", y)
print("Actual Position :", yhat)

print("RMSE Error:", rmse_f)


print("=======================Corridor 2=====================")


a=[12,16]
y = np.array(a)
yhat = np.array([14.67,15.66])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)


print("Actual Position :", y)
print("Actual Position :", yhat)

print("RMSE Error:", rmse_f)

print("=======================DEL=====================")


a=[27,12]
y = np.array(a)
yhat = np.array([25.84,11.22])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)


print("Actual Position :", y)
print("Actual Position :", yhat)

print("RMSE Error:", rmse_f)




print("======================Implementation of paper=====================")


from random import seed
from random import randint
import math

seed(1)
x1=25
print("x1 ", x1)
y1 = 2
print("y1 :", y1)
x2 = 12
print("x2 :", x2)
y2 = 7
print("y2 :", y2)
x3 = 29
print("x3 :", x3)
y3 = 11
print("y3 :", y3)
x = 14
print("x :", x)
y = 16
print("y :", y)



r1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
print("R1  :", r1)
r2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
print("R2  :",r2)
r3 = ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5
print("R3  :",r3)

Distances=[r1, r2, r3]
print ("DISTANCE : ", end="")
print(Distances)


RSSII=[]
listt=[]

for i in range(len(Distances)):
 k=Distances[i]
 listt.append(k)
 L = math.log(k, 10)
 rss = -20 * L + (-36)

 RSSII.append(rss)
print ("RSSI : ", end="")
print(RSSII)

RSSI= [-71,-65,-69]
print(RSSI)

#RSSI SMOOTHING

lst = []
smooth = []
import numpy as np
for i in range(len(RSSI)):

    a = RSSI[i]
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

#FINDING SNR MARGIN

listtt=[]
SNR_margin=[]
SNR=[]
for i in range(len(RSSI)):
 h= RSSI[i]
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


arr = improved_smooth
temp = 0;

for i in range(0, len(arr)):
    print(arr[i]),

# Sort the array in descending order
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] < arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

print();

for i in range(1):
    ARY=[arr[0], arr[1], arr[2]]
    print("High Signal Strength RSSI ")
    ARY.sort()
    print(ARY)

    # Finding Distance

    liist = []
    distance = []
    z = []
    for i in range(len(ARY)):
        n = 2
        A = -36  # A is a reference received signal strength in dBm
        h = ARY[i]
        liist.append(h)
        z = pow(10, (A - h) / (10 * n))
        distance.append(z)

    print("Distance at Improved_Smooth_RSSI ")
    print(distance)



r1=distance[0]
r3=distance[2]
r2=distance[1]

#r1=17
#r2=9.2
#r3=15.8

def trackPhone(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = r2 ** 2 - r3 ** 2 - x2 ** 2 + x3 ** 2 - y2 ** 2 + y3 ** 2
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)
    return x, y


# Apply trilateration algorithm to locate phone
x, y = trackPhone(x1, y1, r1, x2, y2, r2, x3, y3, r3)

# Output phone location / coordinates
print("Targeted Location:")
print(x, y)














print("=======================Conventional Trilateration Method=====================")

from random import seed
from random import randint
import math

seed(1)
x1=2
print("x1 ", x1)
y1 = 1
print("y1 :", y1)
x2 = 5
print("x2 :", x2)
y2 = 4
print("y2 :", y2)
x3 = 8
print("x3 :", x3)
y3 = 2
print("y3 :", y3)
x = 5
print("x :", x)
y = 3
print("y :", y)



r1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
print("R1  :", r1)
r2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
print("R2  :",r2)
r3 = ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5
print("R3  :",r3)

Distances=[r1, r2, r3]
print ("DISTANCE : ", end="")
print(Distances)


RSSII=[]
listt=[]

for i in range(len(Distances)):
 k=Distances[i]
 listt.append(k)
 L = math.log(k, 10)
 rss = -20 * L + (-18.5)

 RSSII.append(rss)
print ("RSSI : ", end="")
print(RSSII)

#RSSI= [-84, -48,-96, -81, -34,-45,-89, -84,-98, -33, -19, -67] #(4,5)

#RSSI= [-46, -79,-39, -36 , -59,-29, -34,-55, -79, - 40, -89, -35]     ## this data is for position (6,2)

#RSSI= [-34, -89,-42, -87 , -45,-89, -84,-98, -33, - 98, -49, -67]   #(2,7)

RSSI= [-18, -56,-74,-98, -33,-98, -34,-48,-96, -71 , -69,-32]  #(5,3)

#RSSI= [-57, -48,-96, -71 , -69,-32, -77,-22, -55, - 67, -67, -22]   # (4, 2)


#RSSI= [-34, -89,-42, -36 , -59,-29, -34,-55, -55, -71 , -69,-32] #(5,1)



arr = RSSI
temp = 0;

for i in range(0, len(arr)):
    print(arr[i]),

# Sort the array in descending order
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] < arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

print();

for i in range(1):
    ARY=[arr[0], arr[1], arr[2]]
    print("High Signal Strength RSSI ")
    ARY.sort()
    print(ARY)

    # Finding Distance

    liist = []
    distance = []
    z = []
    for i in range(len(ARY)):
        n = 2
        A = -18.5  # A is a reference received signal strength in dBm
        h = ARY[i]
        liist.append(h)
        z = pow(10, (A - h) / (10 * n))
        distance.append(z)

    print("Distance at Improved_Smooth_RSSI ")
    print(distance)


r1=distance[0]
r2=distance[1]
r3=distance[2]


def trackPhone(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = r2 ** 2 - r3 ** 2 - x2 ** 2 + x3 ** 2 - y2 ** 2 + y3 ** 2
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)
    return x, y


# Apply trilateration algorithm to locate phone
x, y = trackPhone(x1, y1, r1, x2, y2, r2, x3, y3, r3)

# Output phone location / coordinates
print("Targeted Location:")
print(x, y)

print("=======================RMSE Error of Conventional trilateration Method POSITIONING=====================")


a=[5,1 , 2,7 , 5,3 , 4,5 , 6,2 ,4,2]
y = np.array(a)
yhat = np.array([ 7.08964452 , 1.09271007, 18.38913596, 19.00932653, 7.63603724, -0.66993425, 8.29268173 , -1.07643012, 8.13858346, -0.60741341, 6.44323268, 2.91484902])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)
r2_f = 1-(sum(d**2)/sum((y-np.mean(y))**2))


print("Actual Position :", y)
print("Estimated position  :", yhat)

print("MAE:",mae_f)
print("MSE:", mse_f)
print("RMSE Error:", rmse_f)
print("R-Squared:", r2_f)

print("=======================RMSE Error in Distance in Conventional trilateration Method=====================")


a=[ 4, 5]
y = np.array(a)
yhat = np.array([3 , 2])   #
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)
r2_f = 1-(sum(d**2)/sum((y-np.mean(y))**2))


print("Actual Distance :", y)
print("Estimated Distance :", yhat)

print("MAE:",mae_f)
print("MSE:", mse_f)
print("RMSE Error:", rmse_f)
print("R-Squared:", r2_f)