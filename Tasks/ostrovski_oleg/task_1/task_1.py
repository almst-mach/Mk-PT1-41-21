money = int(input('введите сумму депозита: '))
deposit_months = int(input('введите срок вклада (в годах): ')) * 12   # месяцев в году
rate_in_year = int(input('введите процентную ставку в год: '))    # процентная ставка годовых 

for i in range(1, deposit_months + 1):
    cash = money * (rate_in_year / 100 / 12)   # узнаем чему равна сумма по процентам за один месяц.
    money = money + cash                       # наш депозит плюс процент по вкладу за месяц
    i += 1

print('сумма к выплате: %.2f' % money)