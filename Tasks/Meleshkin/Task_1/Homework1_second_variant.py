def loan_calculator(deposit,percent,month):
    total = deposit*(1+(percent/100)/12)**(months)
    x = total/months
    return total, x

deposit = int(input('Введите желаемую сумму депозита: '))      #Сумма депозита
percent = int(input('Введите процентную ставку: '))       #1/100 доля процентной ставки
months = int(input('Введите время кредитования (в годах): '))*12    #Количество месяцев
total, x = loan_calculator(deposit,percent,months)
print(' Сумма по кредиту в месяц равна:', round(x,1), 'BYN\n','Сумма всего платежа составит:', round(total,2) )
print(' Сумма переплат:', round(total - deposit,2))