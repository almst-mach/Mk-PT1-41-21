
def cycle(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    i += 1
    cycle(l, f, i)

l = [1,2,3,4,5]
# cycle(l)
# cycle("test string")
cycle((1,2,3,4,5), lambda x: print(x))