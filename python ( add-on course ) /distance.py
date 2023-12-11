#find distance between 2 points
import math
x1=float(input("Enter x1 value:"))
x2=float(input("Enter x2 value:"))
y1=float(input("Enter y1 value:"))
y2=float(input("Enter y2 value:"))
dis=math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )
print("distance " ,format(dis,".2f"))
