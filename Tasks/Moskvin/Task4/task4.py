def get_ranges(lst):
    res = []
    try:
        for elem in lst:
            if len(lst) >= 1 and elem + 1 != lst[lst.index(elem) + 1]:
                res.append([lst[0], lst[lst.index(elem)]])
                lst = lst[lst.index(elem) + 1:]
    except IndexError:
        res.append([lst[0], lst[-1]])

    result = []
    for res_el in res:
        if res_el[0] == res_el[-1]:
            res_el.pop()
        result.append('-'.join(str(v) for v in res_el))

    return ', '.join(result)


get_ranges([4, 7, 10])
get_ranges([1, 2, 3, 5, 7, 9, 10, 11])
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([2, 3, 8, 9])
get_ranges([1, 4, 6, 9, 10, 11])
