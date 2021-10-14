numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
test_str = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

# отсортированный список без дубликатов
list_numbers = sorted(list(set([numbers[i] for i in test_str.split(" ")])))
print(list_numbers)

# сумма нечётных чисел списка
odd_number = 0
for i in list_numbers:
    if i%2 == 1:
        odd_number += i
print(odd_number)

# списки попарного перемножения и попарной суммы чисел списка
# по принципу: 1 эл-т * 2 эл-т, 2 эл-т + 3 эл-т, 3 эл-т * 4 эл-т и тд.
mult_list = []
sum_list = []

for i, element in enumerate(list_numbers[1:]):
    if i%2 == 0:
        mult_list.append(element * list_numbers[i])
    else:
        sum_list.append(element + list_numbers[i])

print(mult_list)
print(sum_list)

print("\n--------------------------------------------------------\n")

# реализация с одной переменной
a = sorted(list(set([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[i] for i in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" ")])))
print(a)

print(sum([a for a in a if a%2 !=0]))

a = sorted(list(set([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[i] for i in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" ")])))
a = list(zip(a, a[1:]))
print([a[0]*a[1] for a in a[::2]])

a = sorted(list(set([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[i] for i in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" ")])))
a = list(zip(a, a[1:]))
print([a[0]+a[1] for a in a[1::2]])
