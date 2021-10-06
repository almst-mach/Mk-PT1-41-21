import math
print('a0*x**3+a1*x**2+a2*x+a3==0')
a0=int(input('a0='))
a1=int(input('a1='))
a2=int(input('a2='))
a3=int(input('a3='))
b1=a1/a0
b2=a2/a0
b3=a3/a0
p=-1*((b1**2)/3)+b2
q=(((2*(b1**3))/27)-((b1*b2)/3))+b3
print(p)
print(q)
z=((q**2)/4+(p**3)/27)**(1/2)
x=(((-1*(q/2))+z)**(1/3)-((-1*(q/2))-z)**(1/3))-(b1/3)
print(x)