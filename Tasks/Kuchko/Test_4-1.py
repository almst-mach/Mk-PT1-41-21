# 1. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10" 
# get_ranges([4, 7, 10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


a = [0, 1, 2, 3, 5, 7, 8, 10, 12, 78, 88]

def get_ranges(): 

    i = 0
    count = 0
    count1 = 0

    for i in range(len(a) - 1):

        if a[i] == a[i + 1] - 1:
            count += 1

            if a.index(a[i + 1]) == a.index(a[-1]) and count != 0:                 
                print(f'{a[i]} - {a[-1]}')
        
        if a[i] != a[i + 1] - 1:
            count1 += 1

            if count1 == 1 and a.index(a[i]) == a.index(a[0]):
                print(a[i])
            
            elif a[i - 1] != a[i] - 1:
                if a.index(a[i + 1]) == a.index(a[-1]) and count == 0:
                    print(a[i])
                    print(a[-1])
                
                elif count1 >= 2:
                    print(a[i])
            
            elif a.index(a[i + 1]) != a.index(a[-1]):
                print(f'{a[i - count]} - {a[i]}')
                count = 0

            elif count != 0 and a.index(a[i + 1]) == a.index(a[-1]):
                print(f'{a[i - count]} - {a[i]}')
                count = 0
                
                if a.index(a[i + 1]) == a.index(a[-1]) and count == 0:
                    print(a[-1])
        
        i += 1

get_ranges()
