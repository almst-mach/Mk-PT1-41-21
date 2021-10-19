
s = {'one' : 1, 'two' : 2, 'three' : 3, \
'four' : 4, 'five' : 5, 'six': 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, \
'ten' : 10, 'eleven' : 11, 'twelve' : 12, 'thirteen' : 13, 'fourteen' : 14, \
'fifteen' : 15, 'sixteen' : 16, 'seventeen' : 17, 'eightteen' : 18, 'nineteen' : 19, \
'twenty' : 20}
lst = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
ns = lst.split(' ')
print(ns)
numbers = []
for i in range(len(ns)):
    numbers.append(s.get(ns[i]))
    i =+ 1
print (numbers)
new_numbers = set(numbers)
print(new_numbers)
print (numbers)

if len(numbers)%4 == 0:
    for i in range(0, len(numbers), 4):
        print('Произвидение ', i+1, 'и ', i+2, '= ', numbers[i]*numbers[i+1])
        print('Сумма ', i+3, 'и ', i+4, '= ', numbers[i+2]+numbers[i+3])
elif len(numbers)%4 == 1:
    for i in range(0, len(numbers) - 1, 4):
        print('Произвидение ', i+1, 'и ', i+2, '= ', numbers[i]*numbers[i+1])
        print('Сумма ', i+3, 'и ', i+4, '= ', numbers[i+2]+numbers[i+3])
elif len(numbers)%4 == 2:
    for i in range(0, len(numbers) - 2, 4):
        print('Произвидение ', i+1, 'и ', i+2, '= ', numbers[i]*numbers[i+1])
        print('Сумма ', i+3, 'и ', i+4, '= ', numbers[i+2]+numbers[i+3])
elif len(numbers)%4 == 3:
    for i in range(0, len(numbers) - 3, 4):
        print('Произвидение ', i+1, 'и ', i+2, '= ', numbers[i]*numbers[i+1])
        print('Сумма ', i+3, 'и ', i+4, '= ', numbers[i+2]+numbers[i+3])    
sum = 0 
for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 1:
        sum += numbers[i]
print('Сумма нечётных чисел = ', sum)            


