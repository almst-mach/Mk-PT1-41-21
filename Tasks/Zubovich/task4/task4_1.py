def valid():
    while True:
        try:
            lst = sorted(set([int(i) for i in
                              input(
                                  'Введите непустой список целых чисел через запятую:\n').strip(
                                  ' ').split(',')]))

            return lst
        except (TypeError, ValueError):
            print('Данные введены некорректно, попробуйте еще раз!')
            continue


def get_ranges(lst):
    new_list = []
    x1 = x2 = lst[0]

    for x in lst[1:]:
        if x == x2 + 1:
            x2 = x
        else:
            new_list.append(f'{x1}' if x1 == x2 else f'{str(x1)}-{str(x2)}')
            x1 = x2 = x
    new_list.append(
        f'{x1}' if x1 == x2 else f'{str(x1)}-{str(x2)}')
    return ', '.join(new_list)


print(get_ranges(valid()))

# 0, 1, 2, 3, 4, 7, 8, 10
# 4,7,10
# 2, 3, 8, 9
