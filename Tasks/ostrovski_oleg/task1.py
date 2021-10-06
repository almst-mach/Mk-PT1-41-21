money = 20000
deposit_years = 5
rate_in_year = 15               # процентная ставка годовых.

for i in range(1, deposit_years + 1):
    cash = money * (rate_in_year / 100)
    money = money + cash        #сумма за год по вкладу.
    i += 1
print(int(money))               # число получилосьfloat, поэтому приоброзовал в int.