def loan_calculator(deposit,percent,month):
    x = deposit*(percent+percent/((1+percent)**months-1))
    total = x*months
    return total, x

deposit = int(input('Введите желаемую сумму депозита: '))      #Сумма депозита
percent = int(input('Введите процентную ставку: '))/100/12       #1/100 доля процентной ставки
months = int(input('Введите время кредитования (в годах): '))*12    #Количество месяцев
total, x = loan_calculator(deposit,percent,months)
print(' Сумма по кредиту в месяц равна:', round(x,1), 'BYN\n','Сумма всего платежа составит:', round(total,2) )
print(' Сумма переплат:', round(total - deposit,2))
