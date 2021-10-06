import decimal
import datetime
import calendar

# Чтобы максимально избавится от дробных величин, переводим размер депозита в монеты
deposit_amount = decimal.Decimal('20000') * 100
rate_interest = decimal.Decimal('15')
deposit_time = 5
capitalization = 12 # количество капитализаций в год

# 1 вариант (по формуле "в лоб").
total_payout = round(deposit_amount * (1 + rate_interest/(capitalization * 100)) \
                **(deposit_time*capitalization))

result = (f'Общая сумма выплаты (ФОРМУЛА v.1) : '
          f'{total_payout//100} рублей и {total_payout%100} копеек. '
          f'Доходонсть: {(total_payout - deposit_amount)//100} рублей и '
          f'{(total_payout - deposit_amount)%100} копеек.')
print(result)

# 2 вариант (более реалистичный вариант)
total_payout_1 = deposit_amount
capitalization_number = capitalization * deposit_time

for i in range(capitalization_number):
    total_payout_1 += round((total_payout_1 * rate_interest) / (capitalization * 100))

result_1 = (f'Общая сумма выплаты (Формула v.2): '
               f'{total_payout_1//100} рублей и {total_payout_1%100} копеек.'
               f'Доходонсть: {(total_payout_1 - deposit_amount)//100} рублей и '
               f'{(total_payout_1 - deposit_amount)%100} копеек.')
print(result_1)

# 3 вариант (как в банке)
total_payout_bank = deposit_amount

date_today = datetime.date.today()
check_day = date_today.day

capitalization_date = date_today
for i in range(capitalization_number):
    # вычисление кол-ва дней в году
    if (i % 12) == 0:
        try:
            days_in_year = datetime.date(capitalization_date.year + 1, capitalization_date.month, check_day) - capitalization_date
            days_in_year = days_in_year.days
        except ValueError:
            days_in_year = datetime.date(capitalization_date.year + 1, capitalization_date.month, check_day - 1) - capitalization_date
            days_in_year = days_in_year.days

    days_in_month_now = calendar.monthrange(capitalization_date.year, capitalization_date.month)[1]
    days_in_month_future = calendar.monthrange(capitalization_date.year + (capitalization_date.month) // 12, (capitalization_date.month)%12 + 1)[1]

    # вычисление дату следующей капитализации и кол-во дней в отчётном месяце
    if check_day > days_in_month_future:
        days_in_month_deposit = days_in_month_now - (check_day - days_in_month_future)
        capitalization_date += datetime.timedelta(days=days_in_month_deposit)
    else:
        capitalization_date_old = capitalization_date
        capitalization_date = capitalization_date.replace(year=capitalization_date.year + (capitalization_date.month) // 12, 
                                                          month=(capitalization_date.month)%12 + 1, 
                                                          day=check_day)
        days_in_month_deposit = (capitalization_date.toordinal() - capitalization_date_old.toordinal())

    total_payout_bank += round((total_payout_bank * rate_interest * days_in_month_deposit) / (days_in_year * 100))
    
result_bank = (f'Общая сумма выплаты (БАНК): '
            f'{total_payout_bank//100} рублей и {total_payout_bank%100} копеек.'
            f'Доходонсть: {(total_payout_bank - deposit_amount)//100} рублей и '
            f'{(total_payout_bank - deposit_amount)%100} копеек.')
print(result_bank)





