import decimal  

def input_data():  
    data_list = ['Enter restaurant bill = ', 'Number of person = ', 'Cash amount of each person = ']
    final_data = []  
    for i in range(len(data_list)):
        while True:
            try:
                [final_data.append(int(num)) for num in input(f'{data_list[i]}\n').strip(' ').split(',')]
                if i == 2 and final_data[0] != sum(final_data[2:]):  
                    final_data = final_data[0:2]  
                    raise RuntimeError('The amount of the check is not divided for all persons.')
                break
            except RuntimeError as Error:
                print(Error)
                continue
            except (TypeError, ValueError):
                print('Incorrect input')
                continue
    return final_data


def amount_of_debt(person_data):
    sum = []
    c = {}  
    d = {}


    sum_each = (decimal.Decimal(str(person_data[0])) / decimal.Decimal(str(person_data[1])))  
    pers = {f'Person {i - 1}': decimal.Decimal(str(person_data[i])) for i in range(2, len(person_data))}  
     
    for k, v in pers.items(): 
        if v > sum_each:  
            c[k] = decimal.Decimal(str(v)) - decimal.Decimal(str(sum_each))  
        elif v < sum_each:  
            d[k] = decimal.Decimal(str(sum_each)) - decimal.Decimal(str(v))
        
    count_1 = 0  
    for k, v in c.items():
        count_1 += 1
        count_2 = 0 
        
        while v != 0:  
            for k1, v1 in d.items():
                count_2 += 1
                if v1 == 0: 
                    continue
               
                if v >= v1: 
                    v = decimal.Decimal(str(v)) - decimal.Decimal(str(v1))
                    sum.append(f'{k1} have to pay {k} - {round(float(v1), 2):.2f}')
                    d[k1] = 0 
                     
                elif v < v1:  
                    v1 = decimal.Decimal(str(v1)) - decimal.Decimal(str(v))  
                    d[k1] = v1 
                    sum.append(f'{k1} have to pay {k} - {round(float(v), 2):.2f}')
                    v = 0
                    
                    break
    return sum


for i in amount_of_debt(input_data()):  
    print(i)