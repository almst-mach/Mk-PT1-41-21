def counter_global(i):
    def counter_local():
        nonlocal i
        i +=1
        return i
    return counter_local

f = counter_global(5)
print (f())