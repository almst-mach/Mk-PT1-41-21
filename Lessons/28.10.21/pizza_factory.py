def prepare():
    print("MAKING NEW PIZZA")
    print("preparing base, baking it")
    print("select sauce")

def bake():
    print("baking.......")

def slice():
    print("вжух!")

def add_pepperoni():
    print("adding pepperoni")

def add_cheese():
    print("adding cheese")

# def make_pepperoni():
#     prepare()
#     add_pepperoni()
#     bake()
#     slice()

# def four_chesses():
#     prepare()
#     add_cheese()
#     bake()
#     slice()

def pizza_factory(actions):
    def making():
        prepare()
        for action in actions:
            action()
        bake()
        slice()
    return making

four_chesses = pizza_factory([add_cheese]*4)
make_pepperoni = pizza_factory([add_cheese, add_pepperoni])

four_chesses()
make_pepperoni()