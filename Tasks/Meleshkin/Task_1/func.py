def loan_calculator(deposit,percent,month):
    total = deposit*(1+(percent/100)/12)**(month)
    x = total/month
    return total, x, deposit
