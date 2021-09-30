import math
print ("ax^2+bx+c=0")
a = int(input("a=", ))
b = int(input("b=", ))
c = int(input("c=", ))
D = ((b**2)-4*a*c) 
if D >= 0:
    print ("D=", D)
    print ("x1=", round((-b+math.sqrt(D))/(2*a), 2))
    print ("x2=", round((-b-math.sqrt(D))/(2*a), 2))
else:
	print ("нет корней")