sums=[]
try:
    total_bill=int(input('введите сумму общего счета===>>>'))
except ValueError:
    print('введите целое число')   
    total_bill=int(input('повторите ввод суммы общего счета===>>>'))
try:       
    amount_of_participants=int(input('введите количество участников (от 2)===>>>'))
except ValueError:
    print('введите целое число')
    amount_of_participants=int(input('заново введите количество участников (от 2)===>>>'))
try:   
    for i in range(amount_of_participants):
            a=int(input(f'введите сумму {i+1} участника ===>>>'))
            if a==int(a):
                sums.append(a)
except ValueError:
        for j in range(i):
            print('введите целое число')
            a=int(input(f'введите сумму {i+1} участника еще раз ===>>>'))
            sums.append(a)
def calculation_dept(arg1l, arg2, arg3):
    average_bill=arg1l/arg2
    for i in range(arg2):
        if average_bill-arg3[i]>=0:
            print(f'участник {i+1} должен {average_bill-arg3[i]}' )
calculation_dept(total_bill, amount_of_participants, sums)