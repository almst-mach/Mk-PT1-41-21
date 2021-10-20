str_1 = input('Enter first string: ')
str_2 = input('Enter second string: ')

x = [i for i in str_1 + str_2 if i not in str_1 or i not in str_2]

if not x and len(str_1) == len(str_2): 
    print('Strings are equal')
else:
    print('Strings are not equal')

if str_1.find(str_2) > -1:
    print('String 2 is substring of string 1')
else:
    print('String 2 is not substring of string 1')

if str_1 == str_1[::-1]:
    print("Palindrom")
else:
    print('Not palindrom')

# -------------------------------- Serialization -----------------------



import csv
import pickle
import json

with open('task.csv', 'w', newline = '') as x:
    writer = csv.writer(x)
    writer.writerow(['Model', 'Year', 'Horsepower', 'Engine size'])
    writer.writerow(['80 1.6 Specs', '1989', '69', '1595 cm3 (97.3 cu-in)'])
    writer.writerow(['80 1.6 Specs', '1993', '102', '1595 cm3 (97.3 cu-in)'])
    writer.writerow(['80 1.8 Specs', '1986', '75', '1781 cm3 (108.7 cu-in)'])
    

with open('task.csv', 'r') as x:
    reader = csv.DictReader(x)
    data = list(reader)

with open('task_2.json', 'w') as x:
    json.dump(data, x)

with open('task_2.json', 'r') as x:
    reader = json.load(x) 
    data = list(reader)

with open('task_3.pickle', 'wb') as x:
    pickle.dump(data, x)


# data = {
#     'Model': ['80 1.6 Specs', '80 1.6 Specs', '80 1.8 Specs'],
#     'Year': ['1989', '1993', '1986'],
#     'Horsepower': ['69', '102', '75'],
#     'Engine size': ['1595 cm3 (97.3 cu-in)', '1595 cm3 (97.3 cu-in)', '1781 cm3 (108.7 cu-in)']
# }

# with open('task_1.json', 'w') as x:
#     json.dump(data, x)


# with open('task_2.pickle', 'wb') as x:
#     pickle.dump(data, x)

