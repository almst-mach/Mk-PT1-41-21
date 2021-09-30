x = -5

if x == 0:
    print("it's zero")
elif x == 1:
    print("it's one")
elif x == 2:
    print("it's two")
elif x == 3:
    print("it's three")
elif x == 4:
    print("it's four")
elif x > 0 and x < 10:
    print("it's under ten")
elif x == 11 or 12:
    print("it's either 11 or 12")
else:
    print("nope")

z = 4 if x > 0 else 0
print(4 if x > 0 else 0)

if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

print("positive") if x > 0 else print("zero") if x == 0 else print("negative")

if x >= 0:
    if x == 0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")

if x == 0:
    print("")



y = "good" if x > 0 else "bad"
print(y)

print("good" if x > 0 else "bad")
