# --------------------- Task 1 -----------------------------

def input_list():
    while True:
        try:
            numbers = ([int(numbers) for numbers in input('Enter int numbers of the list without repetitions, comma separated: ').strip(' ').split(',')])
            return numbers
        except:
            print('Smth was wrong, please try again!')
            continue
        

def get_ranges():
    l = input_list()
    l = list(set(l))
    l = sorted(l)
    print(l)   
    rolled_list = []
    for i in range(len(l)):
        if i == len(l) - 1:
            rolled_list.append(l[i])
        elif l[i + 1] == l[i] + 1 and l[i] - 1 != l[i - 1]:
            rolled_list.append(l[i])
            rolled_list.append('-')
        elif l[i] + 1 == l[i + 1] and l[i - 1] == l[i] - 1:
            continue
        else:
            rolled_list.append(l[i])
    final_list = []
    for i in range(len(rolled_list)):
        if i == len(rolled_list) - 1 and rolled_list[i-1] != '-' :
            final_list.append(str(rolled_list[i]))
        elif rolled_list[i - 1] == '-' or rolled_list[i + 1] == '-':
            continue
        elif rolled_list[i] == '-':
            final_list.append(str(rolled_list[i - 1]) + rolled_list[i] + str(rolled_list[i + 1]))
        else:
            final_list.append(str(rolled_list[i]))
    return ','.join(final_list)
    
    


print(get_ranges())



# --------------------- Task 2 -----------------------------

def input_sum_of_check():
    while True:
        try:
            sum_of_check = int(input('Enter sum of check: '))
            assert sum_of_check > 0, 'Sum must be more than zero!'
            return sum_of_check
        except:
            print('Smth was wrong, try ahain: ')
            continue

def input_participant_and_sums():
    participant_and_sums = {}
    while True:
        try: 
            key = input('Enter name of the participant(if it is the last, just enter): ')
            if key =='':
                break
            value = int(input('Enter the amount this participant has entered: '))
            participant_and_sums[key] = value
        except:
            print('Smth was wrong, try again')
            continue
    return participant_and_sums
    

def amount_of_debt():
    check = input_sum_of_check()
    sums = input_participant_and_sums()
    underpay = {}
    overpay = {}
    t = check / len(sums) 
    for k, v in sums.items():
        if sums[k] == t:
            print(f'The participant {k} mustn\'t give anything')
        if sums[k] > t:
            overpay[k] = sums[k] - t
        if sums[k] < t:
            underpay[k] = t - sums[k]
    for overpay_key, overpay_value in overpay.items(): 
        for underpay_key, underpay_value in underpay.items():
            if overpay_value >= underpay_value:  
                overpay_value = overpay_value - underpay_value 
                print(f'The participant {underpay_key} must give {overpay_key} {underpay_value}')
            elif overpay_value < underpay_value:
                underpay_value = underpay_value - overpay_value
                underpay[underpay_key] = underpay_value 
                print(f'The participant {underpay_key} must give {overpay_key} {overpay_value}')    
                break

amount_of_debt()


