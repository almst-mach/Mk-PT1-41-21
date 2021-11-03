# Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34


def deep_iter(lst: list, res=0):
    """
    :return sum of list elements
    """
    for i in lst:
        if isinstance(i, list):
            res += deep_iter(i)
        else:
            res += i
    return res


deep_iter([1, 2, [2, 4, [[7, 8], 4, 6]]])


# Написать функцию для вычисления n первых чисел Фибоначчи.

def fibonacci(n: int):
    """
    :return fibonacci list using cycle while
    """
    fib = [0, 1]
    fib1 = 0
    fib2 = 1
    n -= 2
    while n > 0:
        fib.append(fib2 + fib1)
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib


fibonacci(10)

fib = [0, 1]


def fibonacci_rec(n, fib1=0, fib2=1):
    """
    :return fibonacci list using recursion
    """
    if n == len(fib):
        print(fib)
    else:
        fib.append(fib2 + fib1)
        fibonacci_rec(n, fib2=fib1 + fib2, fib1=fib2)


fibonacci_rec(10)
