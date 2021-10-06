import math
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")

a = int(input('введите число a = '))
b = int(input('введите число b =  '))
c = int(input('введите число c = '))
print()

d = b ** 2 - 4 * a * c
print("Дискриминант D = " + str(d))

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else: 
    print('нет корней')