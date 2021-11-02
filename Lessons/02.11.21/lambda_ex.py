import functools

func = lambda x: x*2
# f = lambda x: [i for i in x]

# def f(x):
#     return x*2

def modify_arg(x, f):
    return f(x)

print(modify_arg(5, lambda x: x*2))

print((lambda x: x*2)(2))

print(func(3))

f = lambda x,y,z=0: x+y+z
print(f(3,4,5))

s = "Abc test aaa"
print(sorted(s.split(), key=str.lower))

d = {1:2, 3:4, 5:0}
print(sorted(d.items(), key=lambda x: x[1]))

l = [[1,2],[3,4],[5,3]]
print(sorted(l, key=lambda x: x[1]))

l = [1,2,3,4,5]
# print(list(map(lambda x: x+1, l)))
print([x for x in map(func, l)])

def filter_check(x):
    return x<=3

print(list(filter(lambda x: x<=3, l)))

print(functools.reduce(lambda x,y: f"{x},{y}", ["test1", "test2"]))

print(functools.reduce(lambda x,y: x if x<y else y, l))
