import cmath
        
print('Решим уравнение вида a*x^3+b*x^2+c*x+d=0')

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
d = float(input('Введите значение d: '))
        
if a == 0 and b == 0 and c == 0 and d == 0:
    print('Ошибка')
    exit()
p = (3 * a * c - b ** 2) / (3 * a ** 2)
q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
Q = (p / 3) ** 3 + (q / 2) ** 2


if q == 0:
    F = cmath.pi/2
if q < 0:
    F = cmath.atan(-2 * cmath.sqrt(-Q) / q)
if q > 0:
    F = cmath.atan(-2 * cmath.sqrt(-Q) / q) + cmath.pi

if Q == 0:
    x1 = 2 * (-q / 2) ** (1 / 3) - b / (3 * a)
    x2 = (-q / 2) ** (-1 / 3) - b / (3 * a)
    x3 = (-q / 2) ** (-1 / 3) - b / (3 * a)
    print('x1 =', x1, '\n x2 =', x2, '\n x3 =', x3)        
elif Q > 0:
    alfa = (-q / 2 + Q ** 0.5) ** (1 / 3)
    beta = -abs((-q / 2 - Q ** 0.5) ** (1 / 3))
    y1 = alfa + beta
    y2 = complex(-((alfa + beta) / 2), (alfa - beta) / 2 * 3 ** 0.5)
    y3 = complex(-((alfa + beta) / 2), -(alfa - beta) / 2 * 3 ** 0.5)
    x1 = y1 - b / (3 * a)
    x1 = round(x1.real, 5)
    x2 = y2 - b / (3 * a)
    x2 = round(x2.real, 5) + round(x2.imag, 5) * 1j
    x3 = y3 - b / (3 * a)
    x3 = round(x3.real, 5) + round(x3.imag, 5) * 1j
    print('x1 =', x1, '\n x2 =', x2, '\n x3 =', x3)
elif Q < 0:
    x1 = 2 * (-p / 3)**0.5 * cmath.cos(F / 3) - b / (3 * a)
    x1 = round(x1.real, 5) 
    x2 = 2 * (-p / 3)**0.5 * cmath.cos((F / 3) + 2 * cmath.pi / 3) - b / (3 * a)
    x2 = round(x2.real, 5)
    x3 = 2 * (-p / 3)**0.5 * cmath.cos((F / 3) + 4 * cmath.pi / 3) - b / (3 * a)
    x3 = round(x3.real, 5) 
    print('x1 =', x1, '\n x2 =', x2, '\n x3 =', x3)

