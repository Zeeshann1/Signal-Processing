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
x = 4
print("x :", x)
y = 5
print("y :", y)



#k=math.log(distance0[0],10)
#rss= -20*k + (-50)
#print(rss)

#z= pow(10, ((-50)-rss)/(20))
#print(z)



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

RSSI= [-84, -48,-96, -81, -34,-45,-89, -84,-98, -33, -19, -67] #(4,5)

#RSSI= [-46, -79,-39, -36 , -59,-29, -34,-55, -79, - 40, -89, -35]     # (6,2)

#RSSI= [-34, -89,-42, -87 , -45,-89, -84,-98, -33, - 98, -49, -67]   #(2,7)

#RSSI= [-18, -56,-74,-98, -33,-98, -34,-48,-96, -71 , -69,-32]  #(5,3)

#RSSI= [-57, -48,-96, -71 , -69,-32, -77,-22, -55, - 67, -67, -22]   # (4, 2)

#RSSI= [-34, -89,-42, -36 , -59,-29, -34,-55, -55, -71 , -69,-32]   # (5,1)





liist = []
SignalQualityR = []
z = []
for i in range(len(RSSI)):

   h=RSSI[i]
   liist.append(h)
   z= 2*(h+100)
   SignalQualityR.append(z)
print(" Signal Quality Using Average RSSI: ", end="")
print( SignalQualityR)





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


liist = []
SignalQuality = []
z = []
for i in range(len(improved_smooth)):

   h=improved_smooth[i]
   liist.append(h)
   z= 2*(h+100)
   SignalQuality.append(z)
print(" Signal Quality Using improved smooth RSSI: ", end="")
print( SignalQuality)




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
        A = -18.5  # A is a reference received signal strength in dBm
        h = ARY[i]
        liist.append(h)
        z = pow(10, (A - h) / (10 * n))
        distance.append(z)

    print("Distance at Improved_Smooth_RSSI ")
    print(distance)


r3=distance[0]
r1=distance[1]
r2=distance[2]





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





#Plotting Signal Quality
x = list(range(len(RSSI)))
import matplotlib.pyplot as plt

#plt.scatter(x, distance, color="blue", label="Direct Distance")
plt.plot(x, SignalQualityR, color="blue", label=" Signal Quality(Before)")
plt.plot(x, SignalQuality, color="red", label=" Signal Quality (After)")
plt.xlabel('Data Index')
plt.ylabel('Signal Quality Graph')
plt.legend()
plt.show()



print("=======================RMSE Error of Proposed Positioning Method=====================")


a=[4,5]
y = np.array(a)
yhat = np.array([4.061338711534476, 5.45439145293209])
x = list(range(len(y)))

# calculate manually
d = y - yhat
mse_f = np.mean(d**2)
mae_f = np.mean(abs(d))
rmse_f = np.sqrt(mse_f)
r2_f = 1-(sum(d**2)/sum((y-np.mean(y))**2))


print("Actual Position :", y)
print("Estimated position Position :", yhat)

print("MAE:",mae_f)
print("MSE:", mse_f)
print("RMSE Error:", rmse_f)
print("R-Squared:", r2_f)

print("=======================RMSE Error in Distance of Proposed Method=====================")


a=[4.47213595499958, 1.4142135623730951, 5.0]
y = np.array(a)
yhat = np.array([5.0991759757487, 4.758827909888168, 1.2458178394657857])
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
