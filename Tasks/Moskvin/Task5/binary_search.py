# def binary_search(lst: list, n: int):
#     low = 0
#     high = len(lst) - 1
#
#     while low <= high:
#         res = (low + high) // 2
#         if lst[res] == n:
#             return res
#         if lst[res] > n:
#             high = res - 1
#         else:
#             low = res + 1
#     return None

def binary_search(lst, n, high, low=0):
    if (high < low):
        return None
    else:
        res = low + ((high - low) // 2)
        if lst[res] > n:
            return binary_search(lst, n, res - 1, low)
        elif lst[res] < n:
            return binary_search(lst, n, high, res + 1)
        else:
            return res


print(binary_search([2, 3, 4, 5, 6, 7, 8, 9], high=8, n=8))
