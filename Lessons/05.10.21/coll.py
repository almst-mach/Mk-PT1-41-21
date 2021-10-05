l = [[1,2,3],[4,5,6],[7,8,9]]
print(l[0][1])
l[0][1] = "two"
print(l)

t = (32, l)
print(t)
t[1][0][1] = 2
print(t)

d = {t: "test"}