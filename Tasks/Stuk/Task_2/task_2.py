import datetime


minutes = {
    1: "одна",
    2: "две",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восьемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тренадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестандцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    21: "двадцать одна",
    22: "двадцать две",
    23: "двадцать три",
    24: "двадцать четыре",
    25: "двадцать пять",
    26: "двадцать шесть",
    27: "двадцать семь",
    28: "двадцать восемь ",
    29: "двадцать девять",
    30: "половина",
    31: "тридцать одна",
    32: "тридцать две",
    33: "тридцать три",
    34: "тридцать четыре",
    35: "тридцать пять",
    36: "тридцать шесть",
    37: "тридцать семь",
    38: "тридцать восемь",
    39: "тридцать девять",
    40: "сорок",
    41: "сорок одна",
    42: "сорок две",
    43: "сорок три",
    44: "сорок четыре",
    45: "пятнадцати",
    46: "четырнадцати",
    47: "тренадцати",
    48: "двенадцати",
    49: "одинадцати",
    50: "десяти",
    51: "девяти",
    52: "восьми",
    53: "семи",
    54: "шести",
    55: "пяти",
    56: "четырех",
    57: "трех",
    58: "двух",
    59: "одной"
}

hours = {
    1: ("первого", "час"),
    2: ("второго", "два"),
    3: ("третьего", "три"),
    4: ("четвертого", "четыре"),
    5: ("пятого", "пять"),
    6: ("шестого", "шесть"),
    7: ("седьмого", "семь"),
    8: ("восьмого", "восемь"),
    9: ("девятого", "девять"),
    10: ("десятого", "десять"),
    11: ("одиннадцатого", "одиннадцать"),
    12: ("двенадцатого", "двенадцать")
}


def print_time(hour: int, minute: int): 
    """Отрисовка времени в текстовом виде

    Args:
        hour (int): кол-во часов
        minute (int): кол-во минут
    """
    if minute > 0 and minute < 45:
        text_hour = hours[hour%12+1][0]
        text_minute = minutes[minute]
        text = "".join((text_minute, print_word_minute(minute), text_hour))
        print(text.capitalize())
    elif minute >= 45 and minute < 60:
        text_hour = hours[hour%12+1][1]
        text_minute = minutes[minute]
        text = " ".join(("без", text_minute, text_hour))
        print(text.capitalize())
    else:
        if hour == 0:
            print("Полночь")
        elif hour == 12: 
            print("Полдень")
        else:
            text_hour = hours[hour%12][1]
            text = "".join((text_hour, print_word_hour(hour), print_time_of_day(hour)))
            print(text.capitalize())


def print_time_of_day(hour: int) -> str:
    """Определение времени суток

    Args:
        hour (int): кол-во часов

    Returns:
        str: время суток
    """
    if hour >= 0 and hour < 6:
        return "ночи"
    elif hour >= 6 and hour < 12:
        return "утра"
    elif hour >= 12 and hour < 18:
        return "дня"
    else:
        return "вечера"


def print_word_minute(minute: int) -> str:
    """Корректная запись слова "минута" в зависимости от кол-ва минут

    Args:
        minute (int): кол-во минут

    Returns:
        str: слово "минута" в зависимости от числа
    """
    last_digit = minute%10
    if last_digit == 1 and minute != 11:
        return " минута "
    elif last_digit in (2, 3, 4) and minute not in (12, 13, 14):
        return " минуты "
    elif minute == 30:
        return " "
    else:
        return " минут "


def print_word_hour(hour: int) -> str:
    """Корректная запись слова "час" в зависимости от кол-ва часов

    Args:
        hour (int): кол-во часов

    Returns:
        str: слово "час" в зависимости от числа
    """
    noraml_hour = hour%12
    if noraml_hour == 1:
        return " "
    elif noraml_hour in (2, 3, 4):
        return " часа "
    else:
        return " часов "


# текущая дата и время
datetime_now = datetime.datetime.today()

hour_now = datetime_now.hour
minute_now = datetime_now.minute

# отрисовка времени
print(datetime_now.strftime("%H:%M"))
print_time(hour=hour_now, minute=minute_now)

# ручной ввод времени
while True:
    time_check = input("Введите время в формате '23:02' или '0', чтобы завершить работу: ")
    if time_check == "0":
        break

    try:
        hour_check, minute_check = time_check.split(":")
        hour_check = int(hour_check)
        minute_check = int(minute_check)
    except ValueError:
        print("Некорректно ведено время! Попробуйте ещё раз.")
        continue

    if hour_check < 0 or hour_check > 23 or minute_check < 0 or minute_check > 59:
        print("Некорректно ведено время! Попробуйте ещё раз.")
        continue
    
    print_time(hour=hour_check, minute=minute_check)
