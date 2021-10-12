l = [2,5,3,8,5,1,7]

for i in range(len(l)-1):
    k = i
    t = i+1
    while t < len(l):
        if l[k]>=l[t]:
            k = t
        t += 1
    l[i], l[k] = l[k], l[i]

print(l)