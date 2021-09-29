p=20000    # The amount of the initial deposit
i=15       # Interest rate
t=1825     # Number of deposit days
k=365      # Number of days per year
s=(((p*i)*t)/k)/100
acc=p+s    #Amount of savings
print(acc)