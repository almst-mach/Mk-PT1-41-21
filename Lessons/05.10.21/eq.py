eq = input("enter your eq:")
x = input("enter your x:")

right = eq.split('=')
coeff = right[1].split('x')
if coeff[0] == "":
    coeff[0] = 1
print(coeff[0], coeff[1])
res = int(coeff[0])*int(x) + int(coeff[1])
print(res)