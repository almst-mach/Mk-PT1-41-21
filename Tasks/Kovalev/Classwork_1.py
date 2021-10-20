stroka = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
stroka = stroka.split(' ')
dic = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
spis = []
for i in stroka:
    for j in dic:
        x = dic.get(i)
    spis.append(x) # преобразовали в числа (список)
print(f'Исходная строка, преобразованная в числа: {spis}') 
spis = list(set(spis)) # исключили дубликаты и отсортировали по возрастанию, выдали в виде списка
print(f'Исходная строка без дубликатов, отсортированная по возрастанию: {spis}')
new_spis = []
for i in range(len(spis)-1):
    if i%2 == 0:
        res = spis[i] * spis[i+1] #произведение элемента с четным индексом на следующий элемент, т.е. первый элемент списка имеет индекс 0 - четный.
        new_spis.append(res) 
    elif i%2 != 0:
        res2 = spis[i] + spis[i+1] # тоже самое но для сложения и для нечетных элементов, т.е. втопрой элемент имеет индекс 1 - нечетный 
        new_spis.append(res2) 
print(f'Произведения и суммы чисел: {new_spis}')
odd = []
for x in spis:
    if x % 2 !=0:
        odd.append(x) # создает список только нечетных чсисел 
print(f'Сумма всех нечетных чисел: {sum(odd)}') # выводит суииу списка нечетных чисел