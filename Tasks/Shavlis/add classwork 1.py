l = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
l = l.split(' ')
a = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
b = []
for i in l:
    b.append(a[i])
print('Преобразование в числа:', b)

c = []
for i in b:
    if not i in c:
        c.append(i)
print('Исключение дубликатов:', c)

for i in range(len(c)-1):
    k = i
    t = i+1
    while t < len(c):
        if c[k]>=c[t]:
            k=t
        t+=1
    c[i],c[k]=c[k],c[i]
print('Сортировка по возрастанию:', c)

z = []
for i in range(len(c)-1):
    if i%2==0:
        z.append(c[i]*c[i+1]) 
    else:
        z.append(c[i]+c[i+1])
print('Вывод произведения и суммы:', z)

s = 0
for i in z:
    if i%2!=0:
        s = s + i
print('Сумма нечетных чисел: ', s)

