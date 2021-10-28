def sum(x, y):
    return x + y

def sum(x=0, y=10):
    return x+y

print(sum())

def sum(x,y,z=0):
    return x+y+z

print(sum(x=1,y=3))

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,0))
l = [1,2,3,4,5,6,7,8,9,0]
d = {1:"one", 2:"two"}
print(sum(*(1,2,3)))
print(sum(*d))
print(sum(*l))

def sum(**kwargs):
    res = 0
    for k, v in kwargs.items():
        res += v
    return res

d = {"one":1, "two":2}
print(sum(**d))

def pairs(**kwargs):
    for i in kwargs.items():
        print(i)

pairs(x=4, b=6, test="test")
pairs()

def my_print(x, y, z, *args, **kwargs):
    print(x, y, z, *args, sep=kwargs["sep"], end=kwargs["end"])

my_print('x', 'y', 'z', *l, sep='___', end=".")