p = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen twenty'.split(' ')
k = {'five': '5', 'twenty': 20, 'thirteen': 13, 'two': 2, 'eleven': 11, 'seventeen': 17, 'ten':10, 'four': 4, 'eight': 8, 'five':5, 'nineteen': 19, 'one':1}
t = [k.get(p[x]) for x in range(len(p))]
t = list(set(t))
for i in range(len(t) - 1):
    for j in range(len(t) - 1 - i):
        if t[j] > t[j+1]:
            t[j],t[j+1] = t[j+1],t[j]
    if i % 2 == 0:
        print(t[i] * t[i + 1], end=' ')
    elif i % 2 !=0:
        print(t[i] + t[i + 1])
print(t)
total = 0
for i in t:
        if i % 2 == 1:
            total += i

print(total)