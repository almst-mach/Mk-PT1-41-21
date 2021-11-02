def data_input():
    while True:
        try:
            numbers = sorted(set([int(num) for num in input('Enter your sorted numbers separated by commas = \n').split(',')]))
            return numbers
        
        except (TypeError, ValueError):
            print('Incorrect input!!!')
            
            continue
        
# array_numbers = [0, 1, 2, 3, 4, 7, 8, 10, 11]

def get_ranges(array_numbers2):
    new_array =[]
    j = 0
    for i in range(len(array_numbers2)):                 
        if i == len(array_numbers2)-1:                          
            if int(array_numbers2[i]) - int(array_numbers2[i-1]) == 1:
                new_array.append(array_numbers2[j:i+1])  
            else:
                new_array.append(array_numbers2[-1:])              
        else:       
            if int(array_numbers2[i+1]) - int(array_numbers2[i]) != 1:
                new_array.append(array_numbers2[j:i+1])
                j = i+1
            else:
                int(array_numbers2[i+1]) - int(array_numbers2[i]) == 1
                continue

    s = []
    for i in range(len(new_array)):
        
        if len(new_array[i]) == 1:
            s.append(str(new_array[i][0]))
        else:
            s.append(str(new_array[i][0]) + '-' + str(new_array[i][-1]))

    return print(s)

get_ranges(data_input())

