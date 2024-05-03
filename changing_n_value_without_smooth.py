import xlrd as x

loc_file = ("D:\LearningPython\AverageRSSIUpdated.xlsx")
wb = x.open_workbook(loc_file)
sheet = wb.sheet_by_index(0)


#for i in range(sheet.nrows):
   #print(sheet.cell_value(i, 2))

data=[sheet.cell_value(i, 2) for i in range(sheet.nrows)]
print(data)



#when n = 1.7

liist = []
distance0 = []
z = []
for i in range(len(data)):

   n0=1.7
   A = -36  #A is a reference received signal strength in dBm
   h=data[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n0))
   distance0.append(z)
print("When n= 1.7: ")
print(distance0)



#when n = 1.8

liist = []
distance1 = []
z = []
for i in range(len(data)):

   n1=1.8
   A = -36  #A is a reference received signal strength in dBm
   h=data[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n1))
   distance1.append(z)

print("When n= 1.8: ")
print(distance1)


#when n = 1.9

liist = []
distance2 = []
z = []
for i in range(len(data)):

   n2=1.9
   A = -36  #A is a reference received signal strength in dBm
   h=data[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n2))
   distance2.append(z)

print("When n= 1.9: ")
print(distance2)



#when n = 2

liist = []
distance3 = []
z = []
for i in range(len(data)):

   n3=2
   A = -36  #A is a reference received signal strength in dBm
   h=data[i]
   liist.append(h)
   z= pow(10, (A-h)/(10*n3))
   distance3.append(z)

print("When n= 2: ")
print(distance3)




import matplotlib.pyplot as plt



plt.scatter(data,distance0, label= "Direct RSSI: n=1.7", color= "green",
            marker= "*", s=50)

plt.scatter(data,distance1, label= "Direct RSSI: n=1.8", color= "red",
            marker= "*", s=50)


plt.scatter(data,distance2, label= "Direct RSSI: n=1.9", color= "blue",
            marker= "*", s=30)

plt.scatter(data,distance3, label= "Direct RSSI: n=2", color= "yellow",
            marker= "*", s=10)


#plt.plot(data,distance2, label= "Direct RSSI")
#plt.plot(smooth,distance, label= "Smooth RSSI")


plt.title('RSSI VS DISTANCE')
plt.xlabel('RSSI')
plt.ylabel('Distance')
plt.legend()
plt.show()


