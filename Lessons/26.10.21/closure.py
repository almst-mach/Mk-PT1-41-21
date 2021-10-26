def maker(n):
    def action(x):
        return x ** n
    return action

f = maker(2)
g = maker(3)
l = maker(4)

print(maker(10)(2))

print(f(2), g(3), l(10))

for func in [f, g, l]:
    print(func(10))