from decimal import Decimal

def is_int(owe):
    try:
        int(owe)
        return True
    except ValueError:
        return False

def not_debt():
    counter = 0
    for k, v in max_owes.items():
        if v == 0:
            counter += 1
    if counter == len(max_owes):
        print("Nobody is in debt")
    else:
        return True

def print_value(value, key, amount_debt):
    print(f"{value} people owe {key} people - {amount_debt} dollars")
    
while True:
    owe = input("Input owe:\n")
    try:
        if owe != '' :
            if is_int(owe):
                owe = int(owe)
                break
            else:
                owe = float(owe)
                break
        else:
            raise RuntimeError
    except (RuntimeError, ValueError):
        print("Input correct value")

while True:
    count = input("Input amount people\n")
    try:
        if count != '':
            if is_int(count):
                count = int(count)
                break
            else:
                raise ValueError 
        else:
            raise RuntimeError
    except RuntimeError:
        print("Input coorect value")
    except ValueError:
        print("Input integer value")

amount = []
while True:
    for num, i in enumerate(range(count),1):
        while True:
            x  = input(f"How much money {num} people pay?\n")
            try:
                if x != '':
                    if is_int(x):
                        x = int(x)
                        amount.append(x)
                        break
                    else:
                        x = float(x)
                        amount.append(x)
                        break
                else:
                    raise RuntimeError
            except (RuntimeError, ValueError):
                print("Input correct value")
    if sum(amount) > owe:
        print("You pay more than yours bill")
    elif sum(amount) < owe:
        print("You pay less than yours bill")
    else:
        break

average = round(owe / count, 2)
max_owes = {c : x - average for c, x in enumerate(amount, 1) if x >= average }
min_owes = [str(c) + str(round(average - x, 2)) for c, x in enumerate(amount, 1) if x < average]

if not_debt():
    j = 0
    for key, value in max_owes.items():
        amount_debt = 0
        value = Decimal(value)
        while True:
            try :
                if round(Decimal(min_owes[j][1:]), 2) == 0 :
                    print_value(min_owes[j][0], key, amount_debt)
                    amount_debt = 0
                    j += 1
                    if round(Decimal(value), 2) == 0:
                        break

                elif round(Decimal(value), 2) == 0  :
                    print_value(min_owes[j][0], key, amount_debt)
                    break

                else:
                    min_owes[j] = (min_owes[j][0] + str(round(Decimal(min_owes[j][1:]) - Decimal(0.01), 2)))
                    value = round(value - Decimal(0.01), 2)
                    amount_debt = round(amount_debt + Decimal(0.01), 2)
            except IndexError:
                break