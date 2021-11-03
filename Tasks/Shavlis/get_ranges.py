# 1. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, отсортированных по возрастанию, которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


while True:
    try:
        l = sorted(set([int(i) for i in input('Введите числа через запятую: ').split(',')]))
        break  
    except:
        print('Данные введены неккоректно')
        continue

def get_ranges(a):
    s = ''
    b = 0
    if len(a) == 1:
        s += f'{a[0]}'
    for i in range(1, len(a)):
        b += 1
        if a[i-1] < a[i] - 1:
            if b == 1 and i == len(a) - 1:
                s += f'{a[i-1]}, {a[i]}'
            elif b == 1:
                s += f'{a[i-1]}, '
            elif b > 1 and i == len(a) - 1:
                s += f'{a[i-b]}-{a[i-1]}, {a[i]}'
            elif b > 1:
                s += f'{a[i-b]}-{a[i-1]}, '
            b = 0
        elif i == len(a) - 1:
            s += f'{a[i-b]}-{a[i]}'
    return s
    
print('Свернутый список:', get_ranges(l))