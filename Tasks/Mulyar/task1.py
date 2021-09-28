b=20000 # start amount
t=5*12 # date in months
a=0.15/12 # % per month
total_amount=b*((1+a)**t)
print('Итоговая сумма составит',round(total_amount, 2),'рублей.')