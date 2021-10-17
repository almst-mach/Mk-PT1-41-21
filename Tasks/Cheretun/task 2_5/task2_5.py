str1, str2 = input(), input()

x = set(str1).difference(set(str2))
if len(x) == 0 and len(str1) == len(str2):
    print("Same strings")
else:
    print("Different strings")

if str1.find(str2) >= 0 :
    print("str2 is an substring str1")
else:
    print("str2 isn't substring str1")

if str1[::-1] == str1:
    print("str1 it's a palindrom")
else:
    print("str1 it isn't a palindrom")