s = "five thirteen two eleven two"

s = [{"five":5, "thirteen":13, "two":2, "eleven": 11}[s] for s in s.split()]

s = sorted(list(set(s)))

print(s)

s += ["stop", 0, 0]

print(s)

while True:

    print(s[s[-1]])

    if s[s[-1]] %2 != 0:
        s[-2] += s[s[-1]]

    if s[s[-1]+1] == "stop":
        break

    s[-1] += 1

print(s)