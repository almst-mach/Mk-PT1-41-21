n = int(input('Введите сумму счета(целое число): '))
dic = input('Введите имена участников и соответствующие суммы в формате(1:150,2:120,3:200 и т.д): ')
dic = dict((k, int(v)) for k, v in (e.split(':') for e in dic.split(',')))
midle = n/len(dic)
for k in dic:
    dic[k] -= midle

def dic_p(stats):
    try:
        max_key = max(stats, key=lambda k: stats[k])
        min_key = min(stats, key=lambda k: stats[k])

        if stats[max_key] > 0 and abs(stats[max_key]) > abs(stats[min_key]):
            res = stats[max_key] + stats[min_key]
            print(f'{min_key} должен {max_key}: {abs(stats[min_key])}')
            stats[max_key] = res
            del stats[min_key]
            dic_p(stats)

        elif stats[max_key] > 0 and abs(stats[max_key]) < abs(stats[min_key]):
            res = stats[max_key] + stats[min_key]
            stats[min_key] = res
            print(f'{min_key} должен {max_key}: {abs(stats[max_key])}')
            del stats[max_key]
            dic_p(stats)

        elif stats[max_key] > 0 and abs(stats[max_key]) == abs(stats[min_key]):

            print(f'{min_key} должен {max_key}: {abs(stats[max_key])}')
            del stats[max_key]
            del stats[min_key]
            dic_p(stats)

    except ValueError:
        print("Надеюсь все поняли, кто кому сколько должен!")


dic_p(dic)




