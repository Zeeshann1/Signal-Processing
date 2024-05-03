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




import matplotlib.pyplot as plt

plt.plot(smooth,distance,label = "RSSI SMOOTH")

plt.plot(data,distance,label = "DIRECT RSSI")

plt.title('RSSI VS DISTANCE where n=2')
plt.xlabel('Smooth RSSI')
plt.ylabel('Distance')
plt.legend()
plt.show()



