i = 0

# while True:
#     if i == 3 or i == 7:
#         i += 1
#         continue
#     if i == 10:
#         break
#     print(f"test {i}")
#     i += 1
# else:
#     print("hello from the else")

while i < 10:
    i += 1
    if i == 3 or i == 7:
        continue
    print(f"test {i}")
else:
    print("hello from the else\n\n\n")

x = [1,2.5,3,"4","test"]

for i in x:
    # if i == "4":
    #     break
    if i == 2.5:
        continue
    print(i)
else:
    print("hello from the else\n\n\n")

print(i)

d = {1: "one", 2: "two"}
for d_key, d_value in d.items():
    print(d_key, d_value)

print("\n\n\n")

for i in range(5, 12, 2):
    print(i)

print("\n\n\n")

for i, e in enumerate(x):
    print(i, e)

print("\n\n\n")

x = [[1,2,3], [4,5,6], [7,8,9]]

for k, i in enumerate(x):
    print(f"{k+1} row")
    for j in i:
        if j % 3 == 0:
            continue
        if j == 5:
            break
        print(j)
    print(f"end of {k+1} row")

if True:
    for i in [1,2,3,4]:
        print(i)