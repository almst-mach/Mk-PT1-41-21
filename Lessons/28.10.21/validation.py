

while True:
    x = input("Input value higher than 34\n")

    try:
        x = int(x)
        assert x >= 35, "The value is too low"
        # if x < 34:
        #     raise RuntimeError("The value is too low")
        break
    except ValueError:
        print("wrong input, please try again")
        continue
    except RuntimeError as error:
        print(error)
        continue
    except AssertionError as error:
        print(error)
        continue