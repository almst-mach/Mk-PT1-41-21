from decimal import *
i_deposit = input("ВВедите размер начального депозита:")
i_deposit= int(i_deposit)
percent = input("Введите размер процента годовой:")
percent = int(percent)/100
#percent = 15/100
#срок договора в месяцах
t=input("Введите срок депозита в годах:")
t=int(t)*12
#t = 12*5
#income = i_deposit*(1+percent/12)**t
income = Decimal(str(i_deposit*(1+percent/12)**t))
rounded = income.quantize(Decimal('0.01'), rounding = ROUND_UP)
print(rounded)