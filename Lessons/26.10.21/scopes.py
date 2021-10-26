x = 10

def func():
    # global x
    # print(f"func - {x}")
    x = 20
    print(f"func - {x}")

    def inner_func():
        nonlocal x
        print(f"inner func - {x}")
        x = 30
        print(f"inner func - {x}")

    inner_func()
    print(f"func - {x}")

func()
print(x)