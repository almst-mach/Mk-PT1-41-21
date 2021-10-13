l = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
sl = {'zero': 0, 'one': 1, 'two': 2 , 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen':14 , 'fiveteen': 15, 'sixteen': 16, 'seventeen': 17, 'eightteen': 18, 'nineteen': 19, 'twenty': 20, 'twenty-one': 21}
print([sl[x] for x in l.split()])
print(set([sl[x] for x in l.split()]))
l = list(set([sl[x] for x in l.split()]))
l = sorted(l)
print(l)

out = []
for i in range(len(l)):
    if i%2 == 0 and i != len(l) - 1:
        out.append(l[i]*l[i+1])
    elif i!= len(l) - 1:
        out.append(l[i]+l[i+1])
print(out)

odd = []
for i in l:
    if i % 2 != 0:
        odd.append(i)
print(odd)
