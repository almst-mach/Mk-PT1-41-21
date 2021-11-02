def do_something(x: int, y: str) -> str:
    """
    Function do_something does something

    Params:
    x(int) - number that will be dealed with
    y(str) - string that will be dealed with
    """
    return x*y

do_something(3,5)
print(help(do_something))