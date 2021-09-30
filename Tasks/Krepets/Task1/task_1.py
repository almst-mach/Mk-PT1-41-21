def credit():
    start_sum = float(input('Enter start sum: '))
    term = int(input('Enter term(in months): '))
    percent = float(input('Enter annual percentage: '))
    end_sum = start_sum * ((1 + (percent / 100)/12)**term)
    print(f'Amount is {end_sum}')


credit()

x = 20000
y = 60
c = 15
sum_2 = x * ((1 + (c / 100)/12)**y)
print(sum_2)