def mult(x,y):
    return x*y

# BAD VERSION
# def mult(x,y):
#     return int(x)*int(y)

# ANOTHER BAD VERSION
def mult(x,y):
    if isinstance(x, int) and isinstance(y, int):
        return x*y

# def mult(x,y,z):
#     return x*y*z

def intersection(x, y):
    res = []
    for i in x:
        if i in y:
            res.append(i)
    return res

print(mult(1,2))

print(mult("test",2))

print(mult([1,3,5],2))

print(mult({1,2,3},2))

print(intersection("test", "nottest"))
print(intersection("t4st", [1,2,3,"4"]))