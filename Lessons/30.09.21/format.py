"the current time is 21:00"

x = "the current time is "
y = "21:00"
x + y

c = "cat"
d = "dog"
m = "mouse"

#"a cat, a dog, a mouse"

p = "a {}, a {}, a {}"
print(p)

print(p.format(c, d, m))

print("a {1}, a {0}, a {2}".format(c, d, m))
print("a {a}, a {b}, a {t}".format(a="cat", b="dog", t="mouse"))

#print("a {1}, a {0}, a {2}".format(c, d))

print(f"a {12+42}, a {d}, a {m}")