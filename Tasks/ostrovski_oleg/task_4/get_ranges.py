def validation():
    while True:  
        list = input("введите список чисел через пробел, пример 1 3 6 7 14 15 76 : ").split() 
        print()

        try: 
            [int(x) for x in list]
            if len(list) == 0:
                raise RuntimeError('произошла ошибка, будьте внимательны при вводе')
            return [int(x) for x in list]
        except ValueError:
            print('произошла ошибка, повторите ввод')
            print()
        except RuntimeError as error:
            print(error)
            print()
            continue


def get_ranges(list):
    list.sort()
    range = [[list[0], list[0]]]
    for i in list: 
        ran = range[-1]
        if i == ran[1] + 1:
            ran[1] = i
        elif i > ran[1] + 1:
            range.append([i, i])
    print(",".join(["-".join([str(a) for a in b]) if b[0] != b[1] else str(b[0]) for b in range]))

  
get_ranges(validation())
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])
