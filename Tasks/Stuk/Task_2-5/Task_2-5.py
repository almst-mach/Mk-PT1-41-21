import timeit

str_1 = "1112"
str_2 = "11"


def check_identity(str_1: str, str_2: str) -> bool:
    len_str_1 = len(str_1)
    len_str_2 = len(str_2)

    if len_str_1 != len_str_2:
        return False

    for i, element in enumerate(str_1):
        if element != str_2[i]:
            return False
    return True


def check_nested_str(str_1: str, str_2: str) -> bool:
    len_str_1 = len(str_1)
    len_str_2 = len(str_2)

    if len_str_1 < len_str_2:
        return False
    
    if not len_str_2:
        return True

    count_iteration = len_str_1 - len_str_2 + 1
    for itr in range(count_iteration):
        finish_substr = itr + len_str_2
        for i, element in enumerate(str_1[itr:finish_substr]):
            if element != str_2[i]:
                break
        else:
            return True
    return False


def check_palindrom(str_1: str) -> bool:
    len_str_1 = len(str_1)

    for i, element in enumerate(str_1):
        if element != str_1[-i-1]:
            return False
    return True


print("Результаты моих функций: ")
print("Строки идентичны!" if check_identity(str_1, str_2) else "Строки разные!")
print("Строка str_2 является подстрокой srt_1!" if check_nested_str(str_1, str_2) else "Строка str_2 не является подстрокой srt_1!")
print("Строка str_1 является палиндромом!" if check_palindrom(str_1) else "Строка str_1 не является палиндромом!")

print("\nРезультаты штатных методов Python: ")
print("Строки идентичны!" if str_1 == str_2 else "Строки разные!")
print("Строка str_2 является подстрокой srt_1!" if (str_2 in str_1) else "Строка str_2 не является подстрокой srt_1!")
print("Строка str_1 является палиндромом!" if str_1 == str_1[::-1] else "Строка str_1 не является палиндромом!")




# def check_identity_1(str_1: str, str_2: str) -> bool:
#     len_str_1 = len(str_1)
#     len_str_2 = len(str_2)

#     if len_str_1 != len_str_2:
#         return False

#     iter_str_2 = iter(str_2)
#     for element in str_1:
#         if element != next(iter_str_2):
#             return False
#     return True


# s = """
# import random
# arr = ['a', 'b', 'c', 'd', 'e', '1', '2', '3']
# str_1 = ''
# for i in range(100000):
#     str_1 += random.choice(arr)
# str_2 = str_1
# len_str_1 = len(str_1)
# len_str_2 = len(str_2)

# if len_str_1 != len_str_2:
#     print("NO")
# """

# def_1 = """
# for i in range(len_str_1):
#     if str_1[i] != str_2[i]:
#         break
# """

# def_2 = """
# iter_str_2 = iter(str_2)
# for element in str_1:
#     if element != next(iter_str_2):
#         break
# """

# def_3 = """
# for i, element in enumerate(str_1):
#     if element != str_2[i]:
#         break
# """

# t1 = timeit.Timer(stmt=def_1, setup=s)
# print(t1.timeit(number=100))

# t2 = timeit.Timer(stmt=def_2, setup=s)
# print(t2.timeit(number=100))

# t3 = timeit.Timer(stmt=def_3, setup=s)
# print(t3.timeit(number=100))

