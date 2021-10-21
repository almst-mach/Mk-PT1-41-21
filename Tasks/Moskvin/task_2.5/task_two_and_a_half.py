# равна ли строка1 строке2
def equal(str1, str2):
    lst = []
    for e, i in enumerate(str1):
        try:
            if i == str2[e]:
                lst.append(i)
        except IndexError:
            print('вводите строки одинаковой длинны')

    print("Строки равны" if len(lst) == len(str2) else "Строки не равны")


# является ли str2 подстракой str1
def substring(str1, str2):
    if str1.find(str2) >= 0:
        return True
    else:
        return False


# является ли str1 полиндромом

def polindrom(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False
