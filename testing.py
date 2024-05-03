import xlrd as x

loc_file = ("D:\LearningPython\AverageRSSIUpdated.xlsx")
wb = x.open_workbook(loc_file)
sheet = wb.sheet_by_index(0)


#for i in range(sheet.nrows):
   #print(sheet.cell_value(i, 2))

data=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print(data)


lst = []
smooth = []
import numpy as np
for i in range(len(data)):

    a = data[i]
    lst.append(a)
    avg = np.mean(lst)
    RSSIsmooth = 0.75 * (a) + (1 - 0.75) * (avg)
    smooth.append(RSSIsmooth)

print(smooth)

liist = []
distance = []
z = []

for i in range(len(smooth)):

   n = 2    #n is the signal propagation constant or exponent
   A = -36  #A is a reference received signal strength in dBm
   h=smooth[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n))
   distance.append(z)

print(distance)



liist2 = []
distance2 = []
z2 = []

for i in range(len(data)):

   n2 = 2    #n is the signal propagation constant or exponent
   A2 = -36  #A is a reference received signal strength in dBm
   h2=data[i]
   liist2.append(h2)
   z2= pow(10, (A2-h2)/(10*n2))
   distance2.append(z2)

print(distance2)




import matplotlib.pyplot as plt



plt.scatter(data,distance2, label= "Direct RSSI", color= "red",
          marker= "*", s=50)

plt.scatter(smooth,distance, label= "Smooth RSSI", color= "green",
            marker= "*", s=50)

#plt.plot(data,distance2, label= "Direct RSSI")
#plt.plot(smooth,distance, label= "Smooth RSSI")


plt.title('RSSI VS DISTANCE')
plt.xlabel('RSSI')
plt.ylabel('Distance')
plt.legend()
plt.show()

