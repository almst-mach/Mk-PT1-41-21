def chechRem(number, div):
    return number%div == 0

# for i in range(1, 101):
#     if chechRem(i, 3) and chechRem(i, 5):
#         print("fizz buzz")
#     elif chechRem(i, 3):
#         print("fizz")
#     elif chechRem(i, 5):
#         print("buzz")
#     else:
#         print(i)

for i in range(1, 101):
    fizz = ""
    buzz = ""
    if chechRem(i, 3):
        fizz = "fizz"
    if chechRem(i, 5):
        buzz = "buzz"
    print(f"{fizz}{buzz}" or i)