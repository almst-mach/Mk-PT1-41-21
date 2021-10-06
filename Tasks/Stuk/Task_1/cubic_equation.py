import math

def sgn(x: float) -> int:
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def input_parameter(name_parametr: str) -> float:
    """Ввод и проверка коэффициентов уравнения на корректность

    Args:
        name_parametr (str): название коэффициента, которое будет отображаться в 'input'

    Returns:
        float: значение коэффициента
    """
    while True:
        x = input(f"Введите коэф-т '{name_parametr}':")
        try:
            x = float(x)
            break
        except:
            print("Введите число!")
    return x


a = input_parameter(name_parametr = "a")
b = input_parameter(name_parametr = "b")
c = input_parameter(name_parametr = "c")
d = input_parameter(name_parametr = "d")

param_a = b / a
param_b = c / a
param_c = d / a

param_Q = (param_a**2 - 3*param_b) / 9
param_R = (2 * param_a**3 - 9 * param_a * param_b + 27 * param_c) / 54
param_S = param_Q**3 - param_R**2

if param_S > 0:
    param_fi = math.acos(param_R / math.sqrt(param_Q**3)) / 3
    x_1 = -2 * math.sqrt(param_Q) * math.cos(param_fi) - (param_a / 3)
    x_2 = -2 * math.sqrt(param_Q) * math.cos(param_fi + 2*math.pi/3) - (param_a / 3)
    x_3 = -2 * math.sqrt(param_Q) * math.cos(param_fi - 2*math.pi/3) - (param_a / 3)
    print(f"Корни уравнения:\nx_1 = {round(x_1, 3)}\nx_2 = {round(x_2, 3)}\nx_3 = {round(x_3, 3)}")
elif param_S < 0:
    if param_Q > 0:
        param_fi = math.acosh(abs(param_R) / math.sqrt(param_Q**3)) / 3
        x_1 = -2 * sgn(param_R) * math.sqrt(param_Q) * math.cosh(param_fi) - (param_a / 3)
        x_2 = complex(round(sgn(param_R) * math.sqrt(param_Q) * math.cosh(param_fi) - (param_a / 3), 3), 
                      round(math.sqrt(3) * math.sqrt(param_Q) * math.sinh(param_fi), 3))
        x_3 = complex(round(sgn(param_R) * math.sqrt(param_Q) * math.cosh(param_fi) - (param_a / 3), 3), 
                      round(-math.sqrt(3) * math.sqrt(param_Q) * math.sinh(param_fi), 3))
        print(f"Корни уравнения:\nx_1 = {round(x_1, 3)}\nx_2 = {x_2}\nx_3 = {x_3}")
    elif param_Q < 0:
        param_fi = math.asinh(abs(param_R) / math.sqrt(abs(param_Q)**3)) / 3
        x_1 = -2 * sgn(param_R) * math.sqrt(abs(param_Q)) * math.sinh(param_fi) - (param_a / 3)
        x_2 = complex(round(sgn(param_R) * math.sqrt(abs(param_Q)) * math.sinh(param_fi) - (param_a / 3), 3), 
                      round(math.sqrt(3) * math.sqrt(abs(param_Q)) * math.cosh(param_fi), 3))
        x_3 = complex(round(sgn(param_R) * math.sqrt(abs(param_Q)) * math.sinh(param_fi) - (param_a / 3), 3), 
                      round(-math.sqrt(3) * math.sqrt(abs(param_Q)) * math.cosh(param_fi), 3))
        print(f"Корни уравнения:\nx_1 = {round(x_1, 3)}\nx_2 = {x_2}\nx_3 = {x_3}")
    else:
        x_1 = -(param_c - (param_a**3 / 27))**(1/3) - (param_a / 3)
        x_2 = complex(round(-(param_a + x_1) / 2, 3),
                      round(math.sqrt(abs((param_a - 3*x_1) * (param_a + x_1) - 4*param_b)) / 2, 3))
        x_3 = complex(round(-(param_a + x_1) / 2, 3),
                      round(-math.sqrt(abs((param_a - 3*x_1) * (param_a + x_1) - 4*param_b)) / 2, 3))
        print(f"Корни уравнения:\nx_1 = {round(x_1, 3)}\nx_2 = {x_2}\nx_3 = {x_3}")
else:
    x_1 = -2 * param_R**(1/3) - (param_a / 3)
    x_2 = param_R**(1/3) - (param_a / 3)
    if x_1 == x_2:
        print(f"Корни уравнения:\nx_1 = {round(x_1, 3)}")
    else:
        print(f"Корни уравнения:\nx_1 = {round(x_1, 3)}\nx_2 = {round(x_2, 3)}")