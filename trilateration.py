
from random import seed
import math
from random import randint
seed(1)
# generate some integers

for _ in range(1):
  x1 = randint(-150, -80)
  print("x1 ",x1)
  y1 = randint(-150, 150)
  print("y1 :", y1)
  x2 = randint(80, 150)
  print("x2 :", x2)
  y2 = randint(20, 150)
  print("y2 :", y2)
  x3 = randint(80, 150)
  print("x3 :", x3)
  y3 = randint(-150, -20)
  print("y3 :", y3)
  x = randint(-60, 60)
  print("x :", x)
  y = randint(-60, 60)
  print("y :", y)

#where r is the radius of the circle. Since
#the diameter is twice the radius, r=d/2
#basically diameter = 2*r

  r1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
  print("R1 :",r1)
  r2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
  print("R2 :", r2)
  r3 = ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5
  print("R3 :", r3)

Distances=[r1, r2, r3]
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


#L=math.log(r1,10)
#rss= -20*k + (-50)
#print(rss)

z= pow(10, ((-18.5)-RSSII[0])/(20))
print(z)





#A function to apply trilateration formulas to return
# the (x,y) intersection point of three circles
def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x,y


#Apply trilateration algorithm to locate phone
x,y = trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3)

#Output phone location / coordinates
print("Cell Phone Location:")
print(x,y)
