from decimal import *
i_deposit = input("ВВедите размер начального депозита:")
i_deposit= Decimal(i_deposit)
percent = input("Введите размер процента годовой:")
percent = Decimal(percent)/100
t=input("Введите срок депозита в годах:")
t=Decimal(t)*12

income = Decimal(str(i_deposit*(1+percent/12)**t))
rounded = income.quantize(Decimal('0.01'), rounding = ROUND_UP)
print(rounded)