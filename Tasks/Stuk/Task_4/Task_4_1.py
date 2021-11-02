test_list_1 = [0, 1, 2, 3, 4, 7, 8, 10]
test_list_2 = [4,7,10]
test_list_3 = [2, 3, 8, 9]

def add_list_group(flag: bool, list_group: list, start: int, finish: int) -> list:
    if flag:
        list_group.append(f"{start}-{finish}")
    else:
        list_group.append(f"{start}")
    return list_group

def create_format_string(list_group):
    return ", ".join(list_group)
     

def get_ranges(list_numbers: list) -> str:
    list_group = []
    start = finish = list_numbers[0]
    flag = False
    for i in range(1, len(list_numbers)):
        if list_numbers[i] == list_numbers[i-1] + 1:
            flag = True
            finish = list_numbers[i]
        else:
            list_group = add_list_group(flag, list_group, start, finish)
            flag = False
            start = list_numbers[i]
    list_group = add_list_group(flag, list_group, start, finish)
    return create_format_string(list_group)


print(get_ranges(test_list_1))
print(get_ranges(test_list_2))
print(get_ranges(test_list_3))