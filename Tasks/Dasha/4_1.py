def tire(lis):
    list_x = []
    try:
        for i in range(len(lis)):
            if lis[i] + 1 == lis[i + 1] and lis[i] - 1 == lis[i - 1]:
                continue
            if lis[i] + 1 == lis[i + 1] and lis[i] - 1 != lis[i - 1]:
                list_x.append(lis[i])
                list_x.append('-')
            else:
                list_x.append(lis[i])
    except IndexError:
        list_x.append(lis[i])
    return list_x


def kon(lisr):
    list_x = []
    try:
        for i in range(len(lisr)):
            if lisr[i] == '-':
                skl = str(lisr[i - 1]) + lisr[i] + str(lisr[i + 1])
                list_x.append(skl)
            elif lisr[i - 1] == '-' or lisr[i + 1] == '-':
                continue
            else:
                list_x.append(str(lisr[i]))
    except IndexError:
        list_x.append(str(lisr[i]))
    return (','.join(list_x))


def svern_spisok(my_spisok):
    res = kon(tire(my_spisok))
    return res


print(svern_spisok([int(i) for i in input('Введите числа отсортированные по возрастанию:').split(',')]))
