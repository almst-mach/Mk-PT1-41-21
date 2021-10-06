a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
dis = b**2 - 4*a*c
if dis < 0:
    print('Корней нет')
elif dis == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + dis ** 0.5) / (2 * a)
    x2 = (-b - dis ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
    
