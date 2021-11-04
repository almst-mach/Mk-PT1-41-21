numerals = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
numerals = numerals.split(' ')
number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
               'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
               'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}

numerals = list(set(number_dict[m] for m in numerals))
print(numerals)

multiplication_and_sum = []
for i in range(len(numerals)):
    if i % 2 == 0 and i != len(numerals):
        multiplication_and_sum.append(numerals[i] * numerals[i + 1])
    elif i != len(numerals) - 1:
        multiplication_and_sum.append(numerals[i] + numerals[i + 1])
print(multiplication_and_sum)

sum_of_all_odd_numbers = 0
for s in numerals:
    if s % 2 != 0:
        sum_of_all_odd_numbers += s
print('The sum of all odd numbers is: ', sum_of_all_odd_numbers)
