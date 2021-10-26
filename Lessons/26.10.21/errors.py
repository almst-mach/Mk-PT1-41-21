from typing import final


l = [1]

try:
    l[0]
    raise NameError
except NameError:
    l = []
except IndexError:
    print("index error")
finally:
    del l

# with open("test.txt") as f:
#     f.read()

# try:
#     f = open("test.txt")
#     f.read()
# finally:
#     f.close()

print(l)
print("continuing")