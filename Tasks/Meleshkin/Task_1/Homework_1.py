from func import loan_calculator as calculator

     
total, x, deposit = calculator(int(input('Введите желаемую сумму депозита: ')),int(input('Введите процентную ставку: ')),int(input('Введите время кредитования (в годах): '))*12)
print(' Сумма по кредиту в месяц равна:', round(x,1), 'BYN\n','Сумма всего платежа составит:', round(total,2) )
print(' Сумма переплат:', round(total - deposit,2))


