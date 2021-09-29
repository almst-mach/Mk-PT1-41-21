import decimal

print("Депозит: ")
print("ежемесячная капитализация")
initial_amount = decimal.Decimal(input("Введите начальную сумму в BYN - "))
interest_rate = decimal.Decimal(input("Введите годовую процентную ставку  - "))
term = decimal.Decimal(input("Введите срок размещения в месяцах - "))

amount_of_money = (initial_amount * ((1 + ((interest_rate / 100) / 12)) ** term))
interest_income = decimal.Decimal(amount_of_money - initial_amount)

print("Сумма вклада с процентами:", amount_of_money.quantize(decimal.Decimal("1.00")))
print("Процентный доход составит:", interest_income.quantize(decimal.Decimal("1.00")))
