def get_value_or_default(default):
    def get_value(l, i):
        if i>=len(l):
            return default
        else:
            return l[i]
    return get_value

get_zer0 = get_value_or_default(0)

l = [1,2,3,4,5,6]
print(get_zer0(l, 1))
print(get_zer0(l, 10))
print(get_zer0(l, -10))