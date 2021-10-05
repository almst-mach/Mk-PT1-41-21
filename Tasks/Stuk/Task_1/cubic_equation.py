import math

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
param_R = (2 * param_a**3 - 9 * param_a * param_b + 27 * param_c)
param_S = param_Q**3 - param_R**2

if S > 0:
    # param_fi = 

