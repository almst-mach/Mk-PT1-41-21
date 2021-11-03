
list_old = [1,2,5,6,7,8,9,12,14,15]

def get_ranges(interval):
    
    list_new = []

    try:
        start_number = interval[0]
        last_number = interval[0]
        for i in interval[1:]:
            step = i - last_number
            if step == 1: last_number = i
            elif not (step == 0):
                list_new.append((start_number, last_number))
                start_number = last_number = i
        else: list_new.append((start_number, last_number))
    except IndexError:
        pass

    return ' , '.join("%d" % start_number if start_number==last_number else "%d-%d" % (start_number, last_number)
            for start_number,last_number in list_new)


print(get_ranges(list_old))

