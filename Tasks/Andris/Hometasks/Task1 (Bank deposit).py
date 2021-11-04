a = 20000    # Initial amount
t = 5    # Term
p = 15    # Annual percentage

T = a * (1 + (p / 100) / 12) ** (12 * t)   # Total income amount for 5 years. Общая сумма дохода за 5 лет.

print("Total income amount for 5 years:", round(T, 2), "BYN")