# 2. Написать программу для вычисления суммы долга при расчёте в ресторане. Например, счёт в 150$ делится на троих, 
# участник №1 внёс 100$, двое остальных (№2 и №3) - 15$ и 35$ соответственно. 
# Программа должна оповестить пользователя о том, что участник №2 должен участнику №1 ещё 35$, а участник №3 - ещё 15$.

# Пользователь вводит сумму счёта, количество участников, их суммы. 

try:
    x = float(input('Введите сумму счета: '))
except ValueError:
    print('Это не числовое значение!')
    x = float(input('Введите сумму счета заново: '))

try:
    y = int(input('Введите количество участников: '))
except ValueError:
    print('Это не числовое значение!')
    y = int(input('Введите количество участников: '))

try:
    c = [float(i) for i in input('Введите суммы, внесенные каждым участником (через пробел): ').split()]
    if y == len(c):
        print('Вы ввели все верно. Поздравляем :)')
    else:
        print('Количество участников не соответствует количеству внесенных сумм.')
        c = [float(i) for i in input('Введите суммы, внесенные каждым участником (через пробел): ').split()]
except ValueError:
    print('Что-то пошло не так. Не все введенные значения являются числами!')
    c = [float(i) for i in input('Введите суммы, внесенные каждым участником (через пробел): ').split()]

every = round(x/y, 2)
print(f'Каждый участник должен внести по {every}:')

count = 0
b = []

for i in range(len(c)):
    count += 1
    if c[i] == every:
        print(f'Участник {count} ничего не должен.')
        b.append(0)
    elif c[i] > every:
        b.append(round(c[i] - every, 2))
    elif c[i] < every:
        b.append(round(c[i] - every, 2))
 
print(f'Список недоплат / переплат участниками {b}')
print(f'Погрешность {sum(b)}')

count1 = 0
f = []

for j in range(len(b)):
    q = max(b)
    q1 = min(b)
    if b[j] == 0:
        count1 += 1
        f.append(0)
    elif b[j] < 0: 
        if b.index(b[j]) == b.index(b[-1]) and b[j] == q:          
            count1 += 1
            print(f'Участник {count1} должен участнику {b.index(q) + 1} {abs(b[j])} ')

        elif q >= abs(b[j]):
            count1 += 1
            print(f'Участник {count1} должен участнику {b.index(q) + 1} {abs(b[j])} ')
            f.append(0)
            b.insert(b.index(q), round((q + b[j]), 2))
            b.pop(b.index(q))
            b.insert(b.index(b[j]), 0)
            b.pop(b.index(b[j + 1]))

        elif q <= abs(b[j]):
            count1 += 1
            print(f'Участник {count1} должен участнику {b.index(q) + 1} {q}')
            f.append(b[j] + q)
            b.insert(b.index(q), 0)
            b.pop(b.index(q))
            b.insert(b.index(b[j]), round((q + b[j]), 2))
            b.pop(b.index(b[j + 1]))

    elif b[j] > 0:
        if abs(q1) >= b[j]:
            count1 += 1
            print(f'Участник {b.index(q1) + 1} должен участнику {count1} {b[j]}')
            f.append(0)
            b.insert(b.index(q1), round((q1 + b[j]), 2))
            b.pop(b.index(q1))
            b.insert(b.index(b[j]), 0)
            b.pop(b.index(b[j + 1]))
        
        elif abs(q1) < b[j]:
            count1 += 1
            print(f'Участник {b.index(q1) + 1} должен участнику {count1} {abs(q1)}')
            f.append(0)
            b.insert(b.index(q1), round((b[j] + q1), 2))
            b.pop(b.index(q1))
            b.insert(b.index(b[j]), 0)
            b.pop(b.index(b[j + 1]))

print(f'Финальный список недоплат / переплат участниками {b}')