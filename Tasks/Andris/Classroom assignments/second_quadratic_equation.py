# Introduce the coefficients
a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - 4 * a * c    # Find the discriminant
x = ((-b) + D ** 0.5) / (2 * a) or ((-b) - D ** 0.5) / (2 * a)
x1 = ((-b) + D ** 0.5) / (2 * a)
x2 = ((-b) - D ** 0.5) / (2 * a)
print("No roots") if D < 0 else print("One root", '\n', x) if D == 0 else print("Two roots", '\n', x1, '\n', x2)
