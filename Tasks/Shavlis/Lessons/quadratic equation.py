import math
print ("ax^2+bx+c=0")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
D = ((b**2)-4*a*c) 
X1 = (-b+math.sqrt(D))/(2*a)
X2 = (-b-math.sqrt(D))/(2*a)
if D > 0:
    print ("D =", D)
    print ("x1 =", round(X1, 2))
    print ("x2 =", round(X2, 2))
elif D == 0:
    print ("D =", D)
    print ("x1,x2 =", round(X1, 2))
else:
    print ("нет корней")