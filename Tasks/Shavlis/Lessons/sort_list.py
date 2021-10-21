import random

l = [4,3,6,5,7,9,2]

def sorting(l):
    return l == sorted(l)

def random_item(lenght):
    x = random.randint(0, lenght-1)
    y = random.randint(0, lenght-1)
    while x == y:
        y = random.randint(0, lenght-1)
    return x, y

def sort(l):
    counter = 0
    while not sorting(l):
        counter += 1
        x, y = random_item(len(l))
        l[x], l[y] = l[y], l[x]
    print(l)
    return counter

print(sort(l))