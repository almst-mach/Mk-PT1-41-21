# 2. Написать программу для вычисления суммы долга при расчёте в ресторане. Например, счёт в 150$ делится на троих, участник №1 внёс 100$, двое остальных (№2 и №3) - 15$ и 35$ соответственно. 
# Программа должна оповестить пользователя о том, что участник №2 должен участнику №1 ещё 35$, а участник №3 - ещё 15$.

# Пользователь вводит сумму счёта, количество участников, их суммы.

def check():
    while True:
        try:
            full_sum = int(input('Введите сумму чека: '))
            assert full_sum > 0
            return full_sum
        except:
            print('Данные введены неккоректно.')
            continue

def participants():
    register = {}
    while True:
        try: 
            key = input('Введите имя участника (для окончания внесения нажмите ввод): ')
            if key =='':
                break
            value = int(input('Введите его внесенную сумму: '))
            assert value > 0
            register[key] = value
        except:
            print('Данные введены неккоректно.')
            continue
    return register

def calculation_of_debts():
    a = check()
    b = participants()
    c = {}
    d = {}
    t = a / len(b) 
    for k, v in b.items():
        if b[k] == t:
            print(f'Участник {k} ничего не должен')
        if b[k] > t:
            d[k] = b[k] - t
        if b[k] < t:
            c[k] = t - b[k]
    for i, j in d.items(): 
        for m, n in c.items():
            if j >= n:  
                j = j - n 
                print(f'Участник {m} должен участнику {i} {int(n)}')
            elif j < n:
                n = n - j
                c[m] = n 
                print(f'Участник {m} должен участнику {i} {int(j)}')    
                break

calculation_of_debts()