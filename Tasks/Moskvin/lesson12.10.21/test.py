s = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'thirteen': 13,
    'seventeen': 17,
    'nineteen': 19
}
lst1 = []
l = s.split()
for i in l:
    if i in d.keys():
        lst1.append(d.get(i))
print(lst1)


lst2 = set(lst1)
print(lst2)


lst3 = sorted(lst2)
print(lst3)


lst4 = []
for i in range(len(lst3)-1):
    if i % 2 == 0:
        lst4.append(lst3[i] * lst3[1 + i])
    elif i % 2 != 0:
        lst4.append(lst3[i] + lst3[1 + i])
print(lst4)


lst5 = []
for i in lst4:
    if i % 2 != 0:
        lst5.append(i)
print(sum(lst5))
