money = 20000
deposit_months = 5 * 12   # месяцев в году
rate_in_year = 15         # процентная ставка годовых 

for i in range(1, deposit_months + 1):
    cash = money * (rate_in_year / 100 / 12)   # узнаем чему равна сумма по процентам за один месяц.
    money = money + cash                       # наш депозит плюс процент по вкладу за месяц
    i += 1
print(int(money))    # число получилось float, поэтому приоброзовал в int.