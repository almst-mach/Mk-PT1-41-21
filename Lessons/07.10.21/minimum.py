from random import shuffle

x = [0,2,3,4,5,6,7,8,9,1]
shuffle(x)

print(x)

# print(min(x)) dead and gone
# print(sorted(x))

result = x[0]
for i in x[1:]:
    if i<result:
        result = i

print(result)


for i in range(len(x)):
    for j in range(len(x)):
        if j == len(x)-1:
            continue
        if x[j]>x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]

print(x)