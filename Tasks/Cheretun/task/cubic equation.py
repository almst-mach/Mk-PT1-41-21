from math import *

a, b, c, d = [int(i) for i in input().split()]
R_1 = 0

Q = (a**2 - 3*b / 9)
R = ((2*a**3 - 9*a*b + 27*c) / 54)
S = (Q**3 - R**2)

if S > 0:
    f = ((1/3) * acos(R/sqrt(Q**2)))
    print(-2*sqrt(Q)*cos(f) - a/3)
    print(-2*sqrt(Q)*cos(f + (2/3)*pi) - a/3)
    print(-2*sqrt(Q)*cos(f - (2/3)*pi) - a/3)

if R > 0:
    R_1 = 1
elif R == 0:
    R_1 = 0
elif R < 0:
    R_1 = -1

cm_1 = complex(0,1)
cm_2 = complex(0,0.5)

if S < 0:
    if Q > 0:
        f = (1/3 * acosh(abs(R)/sqrt(Q**3)))
        print(-2*R_1*sqrt(Q)*cosh(f) - a/3)
        print(R_1*sqrt(Q)*cosh(f) - a/3 + cm_1*sqrt(3)*sqrt(Q)*sinh(f))
        print(R_1*sqrt(Q)*cosh(f) - a/3 - cm_1*sqrt(3)*sqrt(Q)*sinh(f))
    elif Q < 0:
        f = (1/3 * asinh(abs(R)/sqrt(abs(Q)**3)))
        print(-2*R_1*sqrt(abs(Q))*sinh(f) - a/3)
        print(R_1*sqrt(abs(Q))*sinh(f) - a/3 + cm_1*sqrt(3)*sqrt(abs(Q))*cosh(f))
        print(R_1*sqrt(abs(Q))*sinh(f) - a/3 - cm_1*sqrt(3)*sqrt(abs(Q))*cosh(f))
    elif Q == 0:
        x1 = -(c - (a**3/27)**(1/3)) - a/3
        print(x1)
        print(-(a+x1/2) + cm_2*(sqrt(abs((a-3*x1)*(a+x1)-4*b))))
        print(-(a+x1/2) - cm_2*(sqrt(abs((a-3*x1)*(a+x1)-4*b))))

if S == 0:
    print(-2*(R*(1/3)) - a/3)
    print(R*(1/3) - a/3)