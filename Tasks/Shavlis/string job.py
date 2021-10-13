l = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
l = l.split(' ')
a = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
b = []
for i in l:
    b.append(a[i])
print(b)

c = []
for i in range(len(b)):
    for j in range(len(b)):
        if j == len(b)-1:
            continue
        if l[j]>l[j+1] or l[j]<l[j+1]:
            c.append(b[j])
print(c)