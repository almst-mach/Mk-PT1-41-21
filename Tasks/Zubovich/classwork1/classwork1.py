# five thirteen two eleven seventeen two one thirteen ten four eight five nineteen

# 0<"">21


a = input("Введите числительные больше 0 и меньше 21 через пробел в строку: ").split(" ")
c = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
     "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
     "eighteen": 18, "nineteen": 19, "twenty": 20}

for i in a:
    s = c.get(i)
    m = a.index(i)
    a[m] = s
print(a)

d = []

for i in a:
    if i not in d:
        d.append(i)
print(d)

for i in range(len(d)):
    for j in range(i + 1, len(d)):
        if d[i] > d[j]:
            d[i], d[j] = d[j], d[i]

print(d)

h = []
for i in range(len(d)):
    if i % 2 == 0 and i != len(d) - 1:
        h.append(d[i] * d[i + 1])
    elif i != len(d) - 1:
        h.append(d[i] + d[i + 1])

print(h)

s = 0
for i in h:
    if i % 2 != 0:
        s += i
print(s)
