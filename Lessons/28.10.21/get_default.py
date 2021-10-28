def get_value_or_default(default):
    def get_value(l, i):
        # if i>=len(l):
        #     return default
        # else:
        #     return l[i]
        assert i>0, "The index must be positive or zero"

        if l is None or len(l) == 0:
            raise RuntimeError("The collection is empty")

        try:
            try:
                print("test")
                raise TabError
            except:
                print("something went wrong")
            return l[i]
        except IndexError:
            return default
    return get_value

get_zer0 = get_value_or_default(0)

l = [1,2,3,4,5,6]
# print(get_zer0(l, 1))
# print(get_zer0(l, 10))
# print(get_zer0(l, -10))
try:
    get_zer0([], -10)
except RuntimeError as error:
    print(error)
except AssertionError as error:
    print(error)