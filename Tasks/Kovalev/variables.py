a, b, c, d = "test"
print(a)
print(b)
print(c)
print(d)
def line():
    print('____end____')
line()
x,y = 3,4
print(x,y)
line()
# дано
a = 1
b = 2
# задача: присвоить переменной a значение переменной b "2", а переменной b - значение переменной a "1".
temp = a
a = b
b = temp
print(a, b)   # >>> 2, 1
line()
