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
print(l)

def get_ranges(arg):
    str_result = ''
    first_number = 0
    if len(arg) == 1:
        str_result += f'{arg[0]}'
    for i in range(1, len(arg)):
        first_number += 1
        if arg[i-1] < arg[i] - 1:
            if first_number == 1 and i == len(arg) - 1:
                str_result += f'{arg[i-1]}, {arg[i]}'
            elif first_number == 1:
                str_result += f'{arg[i-1]}, '
            elif first_number > 1 and i == len(arg) - 1:
                str_result += f'{arg[i-first_number]}-{arg[i-1]}, {arg[i]}'
            elif first_number > 1:
                str_result += f'{arg[i-first_number]}-{arg[i-1]}, '
            first_number = 0
        elif i == len(arg) - 1:
            str_result += f'{arg[i-first_number]}-{arg[i]}'
    return str_result
    
print(get_ranges(l))