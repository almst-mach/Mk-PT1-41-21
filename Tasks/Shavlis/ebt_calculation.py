# 2. Написать программу для вычисления суммы долга при расчёте в ресторане. Например, счёт в 150$ делится на троих, участник №1 внёс 100$, двое остальных (№2 и №3) - 15$ и 35$ соответственно. 
# Программа должна оповестить пользователя о том, что участник №2 должен участнику №1 ещё 35$, а участник №3 - ещё 15$.

# Пользователь вводит сумму счёта, количество участников, их суммы.


# total_bill=int(input('введите сумму общего счета===>>>'))
# amount_of_participants=int(input('введите количество участников (от 2)===>>>')) 
# sums=[]
# for i in range(amount_of_participants):
#     a=int(input(f'введите сумму {i+1} участника ===>>>'))
#     sums.append(a)

# def calculation_dept(arg1l, arg2, arg3):
#     average_bill=arg1l/arg2
#     for i in range(arg2):
#         if average_bill-arg3[i]>=0:
#             print(f'участник {i+1} должен {average_bill-arg3[i]}' )
# calculation_dept(total_bill, amount_of_participants, sums)

<<<<<<< Updated upstream
def input_sum_of_check():
    while True:
        try:
            sum_of_check = int(input('Enter sum of check: '))
            assert sum_of_check > 0, 'Sum must be more than zero!'
            return sum_of_check
        except:
            print('Smth was wrong, try ahain: ')
            continue

print(input_sum_of_check())
=======
# def input_sum_of_check():
#     while True:
#         try:
#             sum_of_check = int(input('Enter sum of check: '))
#             assert sum_of_check > 0, 'Sum must be more than zero!'
#             return sum_of_check
#         except:
#             print('Smth was wrong, try ahain: ')
#             continue

# print(input_sum_of_check())
>>>>>>> Stashed changes
