def entry_bool(text: str) -> bool:
    """Ввод целого числа 

    Args:
        text (str): текст сообщения перед вводом данных

    Raises:
        RuntimeError: ошибка если вводимое число не равно 1 или 2

    Returns:
        bool: выходное значение типа bool 
    """
    while True:
        value = input(f"{text}:\n")
        
        try:
            value = int(value)
            if value not in (1,2):
                raise RuntimeError(f"Введенное число не равно ни 1, ни 2. Повторите попытку.")
            break
        except ValueError:
            print("Входные данные не являются целым число. Повторите попытку.")
        except RuntimeError as error:
            print(error)
    return True if value == 1 else False


def entry_number_int(min_value: int, text: str) -> int:
    """Ввод целого числа 

    Args:
        min_value (int): минимальное значение целого числа
        text (str): текст сообщения перед вводом данных

    Raises:
        RuntimeError: ошибка если вводимое число меньше минимального значения

    Returns:
        int: вводимое целое число
    """
    while True:
        value = input(f"{text} (целое число):\n")
        
        try:
            value = int(value)
            if value < min_value:
                raise RuntimeError(f"Введенное число меньше минимально допустимого значения: {min_value}. Повторите попытку.")
            break
        except ValueError:
            print("Входные данные не являются целым число. Повторите попытку.")
        except RuntimeError as error:
            print(error)
    return value


def entry_number_float(min_value: float, text: str) -> float:
    """Ввод числа

    Args:
        min_value (float): минимальное значение числа
        text (str): текст сообщения перед вводом данных

    Raises:
        RuntimeError: ошибка если вводимое число меньше минимального значения

    Returns:
        float: вводимое число
    """
    while True:
        value = input(f"{text}:\n")
        
        try:
            value = float(value)
            if value < min_value:
                raise RuntimeError(f"Введенное число меньше минимально допустимого значения: {min_value}. Повторите попытку.")
            break
        except ValueError:
            print("Входные данные не являются число. Повторите попытку.")
        except RuntimeError as error:
            print(error)
    return value


def add_non_debtor(
        payments: dict, debts: dict, underpayments: dict, overpayments: dict, 
        min_payment: int, max_payment: int, count_min_payment: int, count_max_payment: int):
    """Исключение из должников тех людей, которые заплатили свою долю. 
       Т.к. число не делится нацело, то кто-то заплатить должен на 1 копейку больше,
       а кто-то меньше. Поэтому возможна ситуация, когда кто-то должен будет 1 копейку
       или должен будет ее отдать.

    Args:
        payments (dict): кто и сколько заплатил 
        debts (dict): кто, кому и сколько должен
        underpayments (dict): кто заплатил меньше и на сколько
        overpayments (dict): кто заплатил больше и на сколько
        min_payment (int): минимальная сумма, которую нужно было заплатить по счёту одному человеку
        max_payment (int): максимальная сумма (на 1 копейку больше минимальной), 
                        которую нужно было заплатить по счёту одному человеку
        count_min_payment (int): кол-во людей, которые должны заплатить на 1 копейку меньше
        count_max_payment (int): кол-во людей, которые должны заплатить на 1 копейку больше

    Returns:
        dict: кто и сколько заплатил 
        dict: кто, кому и сколько должен
        dict: кто заплатил больше и на сколько
        dict: кто заплатил меньше и на сколько
        
    """
    for guest in list(payments.keys()):
        payment = payments[guest]
        if payment == min_payment:
            if count_min_payment:
                count_min_payment -= 1
                debts[(guest, guest)] = 0
            else:
                underpayments[guest] = 1
            del payments[guest]
        elif payment == max_payment:
            if count_max_payment:
                count_max_payment -= 1
                debts[(guest, guest)] = 0
            else:
                overpayments[guest] = 1
            del payments[guest]
    return payments, debts, underpayments, overpayments


def add_debtor(
        payments: dict, underpayments: dict, overpayments: dict, min_payment: int, 
        max_payment: int, count_min_payment: int, count_max_payment: int):
    """Формирование групп тех, кто заплатил больше и кто заплатил меньше

    Args:
        payments (dict): кто и сколько заплатил 
        underpayments (dict): кто заплатил меньше и на сколько
        overpayments (dict): кто заплатил больше и на сколько
        min_payment (int): минимальная сумма, которую нужно было заплатить по счёту одному человеку
        max_payment (int): максимальная сумма (на 1 копейку больше минимальной), 
                        которую нужно было заплатить по счёту одному человеку
        count_min_payment (int): кол-во людей, которые должны заплатить на 1 копейку меньше
        count_max_payment (int): кол-во людей, которые должны заплатить на 1 копейку больше

    Returns:
        dict: кто заплатил меньше и на сколько
        dict: кто заплатил больше и на сколько
    """
    for guest, payment in payments.items():
        if payment < min_payment:
            if count_min_payment:
                count_min_payment -= 1
                underpayments[guest] = min_payment - payment
            else:
                count_max_payment -= 1
                underpayments[guest] = max_payment - payment
        else:
            if count_min_payment:
                count_min_payment -= 1
                overpayments[guest] = payment - min_payment
            else:
                count_max_payment -= 1
                overpayments[guest] = payment - max_payment
    return underpayments, overpayments


def create_groups_debt_float(payments: dict, min_payment: int, count_max_payment: int, count_min_payment: int):
    """
        Разбиение на 3 группы гостей: 1) те, кто заплатил больше
                                      2) те, кто заплатил меньше
                                      3) кто заплатил свою долю
        Те, кто заплатил свою долю, записываем в словарь 'кто, кому и сколько должен',
        т.е. исключаем из должников, но не всех, а по наличию свободных мест. Кто-то может 
        остаться должен 1 копейку, и кому-то должны будут отдать 1 копейку.


    Args:
        payments (dict): кто и сколько заплатил
        min_payment (int): минимальная сумма, которую нужно было заплатить по счёту одному человеку
        count_max_payment (int): кол-во людей, которые должны заплатить на 1 копейку больше
        count_min_payment (int): кол-во людей, которые должны заплатить на 1 копейку меньше

    Returns:
        dict: кто заплатил больше и на сколько
        dict: кто заплатил меньше и на сколько
        dict: кто, кому и сколько должен
    """
    max_payment = min_payment + 1

    overpayments = {}
    underpayments = {}
    debts = {}
    payments_copy = payments.copy()

    payments_copy, debts, underpayments, overpayments = add_non_debtor(payments_copy, 
                                                                        debts, 
                                                                        underpayments, 
                                                                        overpayments, 
                                                                        min_payment, 
                                                                        max_payment, 
                                                                        count_min_payment, 
                                                                        count_max_payment)
    underpayments, overpayments = add_debtor(payments_copy, 
                                                underpayments, 
                                                overpayments, 
                                                min_payment, 
                                                max_payment, 
                                                count_min_payment, 
                                                count_max_payment)
    return overpayments, underpayments, debts


def create_groups_debt(payments: dict, average_payment: int):
    """
        Разбиение на 3 группы гостей: 1) те, кто заплатил больше
                                      2) те, кто заплатил меньше
                                      3) кто заплатил свою долю
        Те, кто заплатил свою долю, записываем в словарь 'кто, кому и сколько должен'

    Args:
        payments (dict): кто и сколько заплатил
        average_payment (int): сумма, которую нужно было заплатить по счёту одному человеку

    Returns:
        dict: кто заплатил больше и на сколько
        dict: кто заплатил меньше и на сколько
        dict: кто, кому и сколько должен
    """
    overpayments = {}
    underpayments = {}
    debts = {}

    for guest, payment in payments.items():
        if payment > average_payment:
            overpayments[guest] = payment - average_payment
        elif payment < average_payment:
            underpayments[guest] = average_payment - payment
        else:
            debts[(guest, guest)] = 0
    return overpayments, underpayments, debts


def recovery_debts(overpayments: dict, underpayments: dict, debts: dict) -> dict:
    """Распределение долгов между друзьями

    Args:
        overpayments (dict): кто заплатил больше и на сколько
        underpayments (dict): кто заплатил меньше и на сколько
        debts (dict): кто, кому и сколько должен

    Returns:
        dict: кто, кому и сколько должен
    """
    for guest_max, overpayment in overpayments.items():
        for guest_min in list(underpayments.keys()):
            underpayment = underpayments[guest_min]
            if underpayment > overpayment:
                underpayment -= overpayment
                debts[(guest_min, guest_max)] = underpayment
                underpayments[guest_min] = underpayment
                break
            elif underpayment < overpayment:
                overpayment -= underpayment
                debts[(guest_min, guest_max)] = underpayment
                del underpayments[guest_min]
            else:
                debts[(guest_min, guest_max)] = underpayment
                break
        else:
            debts[(guest_max, guest_max)] = overpayment
    return debts


def print_result(debts: dict):
    """Отрисовка результата

    Args:
        debts (dict): кто, кому и сколько должен
    """
    for guests, debt in debts.items():
        if guests[0] == guests[1]:
            if debt:
                print(f"Гость {guests[0]} переплатил - {debt//100},{debt%100:0=2} рублей.")
            else:
                print(f"Гость {guests[0]} ничего не должен.")
        else:
            print(f"Гость {guests[0]} должен гостю {guests[1]} - {debt//100},{debt%100:0=2} рублей.")


def check_bill_payment(restaurant_bill: int, guests_payment: int) -> bool:
    """Оплатили гости весь счет или нет

    Args:
        restaurant_bill (int): счёт в ресторане
        actual_guests_payment (int): сумма, которую заплатили клиенты

    Returns:
        bool: True, если оплатили весь счёт, Flase, если нехватает денег
    """
    if guests_payment >= restaurant_bill:
        return True
    return False


def input_guests_payment(count_guests: int, restaurant_bill: int):
    while True:
        guests_payment = {i+1: int(entry_number_float(min_value=0, text=f"Введите сумму внесенную {i+1} гостем (в рублях)") * 100) for i in range(count_guests)}
        sum_guests_payment = sum(guests_payment.values())
        if check_bill_payment(restaurant_bill, sum_guests_payment):
            break
        print(f"Ваша компания недоплатила {(restaurant_bill - sum_guests_payment)//100},{(restaurant_bill - sum_guests_payment)%100:0=2} рублей")
    return guests_payment


def main():
    # Переводим все суммы в монеты для точного счёта
    restaurant_bill = int(entry_number_float(min_value=0, text="Введите размер счёта в ресторане (В рублях)") * 100)
    count_guests = entry_number_int(min_value=1, text="Введите кол-во гостей в ресторане")
    actual_guests_payment = input_guests_payment(count_guests, restaurant_bill)

    tip_equally = entry_bool("Введите число:\n1 - если делим чаевые (если они есть) на всех поровну\n2 - платят те, кто больше заплатил")
    if tip_equally:
        sum_actual_guests_payment = sum(actual_guests_payment.values())
        average_payment = sum_actual_guests_payment // count_guests
        count_people_max_payment = sum_actual_guests_payment % count_guests
    else:
        average_payment = restaurant_bill // count_guests
        count_people_max_payment = restaurant_bill % count_guests

    if count_people_max_payment:
        overpayments, underpayments, debts = create_groups_debt_float(payments=actual_guests_payment, 
                                                                        min_payment=average_payment, 
                                                                        count_max_payment=count_people_max_payment, 
                                                                        count_min_payment=count_guests - count_people_max_payment)
    else:
        overpayments, underpayments, debts = create_groups_debt(payments=actual_guests_payment, 
                                                                average_payment=average_payment)
    debts = recovery_debts(overpayments, underpayments, debts)
    print_result(debts)


main()
