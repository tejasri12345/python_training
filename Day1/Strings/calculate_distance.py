import math
x1=int(input("enter x1 value: "))
x2=int(input("enter x2 value: "))
y1=int(input("enter y1 value: "))
y2=int(input("enter y2 value: "))
dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
distance = "{:.2f}".format(dist)
print(distance)