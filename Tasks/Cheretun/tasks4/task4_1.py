def get_ranges(list_ranges):
    ranges = []
    for num in list_ranges:
        if ranges == []:
            ranges.append([num])
        elif num - previously_num == 1:
            ranges[-1].append(num)
        else:
            ranges.append([num])
        previously_num = num
    return print_ranges(ranges)

def print_ranges(ranges):
    out = []
    x = [out.append(f"{r[0]}-{r[-1]}") if len(r) > 1 else out.append(r[0]) for r in ranges]
    print(*out, sep = ', ')

while True:
    array = input("Input values with sep ','\n")
    try:
        if array.split(',') and array.count(',') > 0:
            if array[0].isdigit():
                get_ranges([int(i) for i in array.split(',')])
                break
            else:
                raise RuntimeError
        else:
            raise RuntimeError
    except ValueError:
        print("Input correct range")
    except RuntimeError:
        print("Input range with format integer digits 'n1,n2 .... '")
    
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])