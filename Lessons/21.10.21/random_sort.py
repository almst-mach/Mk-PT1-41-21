import random

l = [4,3,6,5,7,8,2,1,10,11,12,13]

def is_sorted(l):
    # for i in range(len(l)-1):
    #     if l[i]>l[i+1]:
    #         return False
    # return True
    return l == sorted(l)

def get_indexes(lenght):
    x = random.randint(0, lenght-1)
    y = random.randint(0, lenght-1)
    while x == y:
        y = random.randint(0, lenght-1)
    return x, y

def sort(l):
    counter = 0
    while not is_sorted(l):
        counter += 1
        x, y = get_indexes(len(l))
        l[x], l[y] = l[y], l[x]
    print(l)
    return counter
    
print(sort(l))