from itertools import zip_longest

x = input("Enter your words: ").split()

a = {'zero': 0, 'one': 1, 'two': 2, 'tree': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
'eightteen': 18, 'nineteen': 19, 'twenty': 20, 'twenty one': 21}

# вывод списка преобразованного в числа
b = []                     
for word in x:
    if word in a:
        b.append(a[word])
print(b)

# исключение дубликатов и сортировка по возрастанию 
b1 = list(set(b))            
print(b1)

# вывод полной суммы всех нечетных чисел 
c = [int(item) for item in b]     
summa = 0
for i in c:
    if i % 2 != 0:
        summa += i
print(f"Sum of all odd numbers: {summa}")

# вывод произведения первого и второго чисел, сумму второго и третьего, произведение третьего и четвертого и т.д. 
index = 0
d = []              # создаем два списка согласно четным и нечетным индексам 
e = []
for item in b:
    if index % 2 == 0:
        d.append(item)
    if index % 2 != 0:
        e.append(item)
    index += 1

w1 = [t*y for t, y in zip_longest(d, e, fillvalue = 1)] # умножаем 
d.pop(0)     # удаляем первый элемент из списка для удобного сложения  
w2 = [t+y for t, y in zip_longest(d, e, fillvalue = 0)] # суммируем 
w3 = list(zip_longest(w1, w2, fillvalue=' '))   # создаем список [произведение, сумма, произведение, сумма и т. д.]
w4 = [item for sub in w3 for item in sub]      # преобразуем список 

print(w4)

# Наверное, громоздко получилось немного и, уверен, можно сделать проще, но пока мои знания не настолько заточены на оптимизацию  :)
# Как все это сделать с использованием только одной переменной не знаю :))) 

# для проверки five thirteen two eleven seventeen two one thirteen ten four eight five nineteen fifteen 
