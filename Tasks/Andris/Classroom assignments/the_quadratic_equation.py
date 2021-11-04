# Introduce the coefficients
a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - 4 * a * c  # Find the discriminant
if D < 0:
    print('No roots')

elif D == 0:
    x = ((-b) + D ** 0.5) / (2 * a) or ((-b) - D ** 0.5) / (2 * a)
    print('One root', '\n', x)

elif D > 0:
    x1 = ((-b) + D ** 0.5) / (2 * a)
    x2 = ((-b) - D ** 0.5) / (2 * a)
    print('Two roots:', '\n', x1, '\n', x2)
