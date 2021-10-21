# do_nothing()

def do_nothing():
    print("test")

do_nothing()

x = "test"

if x == "test":
    def my_test_func():
        print("this is actually test")
else:
    def my_test_func():
        print("this is not")

my_test_func()

def times_two(x, y):
    print("before return")
    z = "some result"
    return x*2, y*2
    print("after return")

res1, res2 = times_two(5, 0)
print(res1, res2)

def return_nothing():
    if x == "testvfcv":
        return "test"
    print("doing nothing")

res = return_nothing()
print(res)

def external_func(internal_func, arg):
    internal_func(arg)

external_func(print, "test")