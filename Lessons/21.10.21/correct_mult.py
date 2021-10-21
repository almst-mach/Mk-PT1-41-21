def mult(x, y):
    res = 0
    if y < 0:
        y = abs(y)
        res = mult_cycle(False, y, x)
        return res
    else:
        res = mult_cycle(True, y, x)
        return res

def mult_cycle(sign, y, x):
    res = 0
    for i in range(y):
        if sign:
            res += x
        else:
            res -= x

    return res

def super_correct_mult(x, y):
    res = 0
    if y < 0:
        x = -x
        y = -y
    for i in range(y):
        res += x
    return res

print(super_correct_mult(2, 3))