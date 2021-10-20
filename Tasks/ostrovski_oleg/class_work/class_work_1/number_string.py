test_input = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split(" ")

numbers_case = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 
                'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 
                'eighteen': 18, 'nineteen': 19, 'twenty': 20}

numbers = list(set([numbers_case[i] for i in test_input]))           # sorted() не использовал, так как set() все отсортировал.

odd_numbers_sum = sum([i for i in numbers if i % 2 != 0])


plus = []
multiply = []

for i in range(len(numbers) - 1):
    if i % 2 == 0:
        plus.append(numbers[i] + numbers[i + 1])
    elif i % 2 != 0:
        multiply.append(numbers[i] * numbers[i + 1])