str1 = input('Cтрока 1: ')
str2 = input('Cтрока 2: ')

x = []
for i in str1 + str2:
    if i not in str1 or i not in str2:
        x.append(i)
if not x:
    print('Строка 1 равна строке 2')
else:
    print('Строка 1 не равна строке 2')


if str1[0].find(str2[0]) > -1:
    print('Строка 1 содержит строку 2')
else:
    print('Строка 1 не содержит строку 2')


if str1 == str1[::-1]:
    print('Строка 1 является полиндромом') 
else:
    print('Строка 1 не является полиндромом')