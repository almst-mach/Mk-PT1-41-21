from datetime import datetime


def time_in_string_format(minutes, hours):
    """
    changes the numeric time value to text
    """

    if int(hours) in hour1.keys() and int(minutes) in minutes1.keys():  # if minutes < 30 and 30 < minutes < 45
        print(f'{minutes1.get(int(minutes))}{hour1.get(int(hours))}')

    elif int(hours) in hour2.keys() and int(minutes) in minutes2.keys():  # if minutes >= 45
        print(f'{minutes2.get(int(minutes))}{hour2.get((int(hours)))}')

    elif int(hours) == 00 and int(minutes) == 00:  # midnight
        print('Полночь')

    elif int(minutes) == 30:  # if minutes = 30
        print(f'Половина {hour1.get(int(hours))}')

    elif int(hours) in hour2.keys() and int(minutes) == 00:  # if minutes = 00
        print(f'{hour2.get((int(hours) - 1))} ровно')


hour1 = {
    0: 'первого ',
    1: 'второго ',
    2: 'третьего ',
    3: 'четвертого ',
    4: 'пятого ',
    5: 'шестого ',
    6: 'седьмого ',
    7: 'восьмого ',
    8: 'девятого ',
    9: 'десятого ',
    10: 'одинадцатого ',
    11: 'двенадцатого ',
    12: 'первого',
    13: 'второго',
    14: 'третьего ',
    15: 'четвертого ',
    16: 'пятого ',
    17: 'шестого ',
    18: 'седьмого ',
    19: 'восьмого ',
    20: 'девятого ',
    21: 'десятого ',
    22: 'одинадцатого ',
    23: 'двенадцатого ',
}

hour2 = {
    0: 'час ',
    1: 'два ',
    2: 'три ',
    3: 'четыре ',
    4: 'пять ',
    5: 'шесть ',
    6: 'семь ',
    7: 'восемь ',
    8: 'девять ',
    9: 'десять ',
    10: 'одинадцать ',
    11: 'двенадцать ',
    12: 'час',
    13: 'два',
    14: 'три ',
    15: 'четыре ',
    16: 'пять ',
    17: 'шесть ',
    18: 'семь ',
    19: 'восемь ',
    20: 'девять ',
    21: 'десять ',
    22: 'одинадцать ',
    23: 'двенадцать ',
}

minutes1 = {
    1: 'одна минута ',
    2: 'две минуты ',
    3: 'три минуты ',
    4: 'четыре минуты ',
    5: 'пять минут ',
    6: 'шесть минут ',
    7: 'семь минут ',
    8: 'восьемь минут ',
    9: 'девять минут ',
    10: 'десять минут ',
    11: 'одинадцать минут ',
    12: 'двенадцать минут ',
    13: 'тренадцать минут ',
    14: 'четырнадцать минут ',
    15: 'пятнадцать минут ',
    16: 'шестандцать минут ',
    17: 'семнадцать минут ',
    18: 'восемнадцать минут ',
    19: 'девятнадцать минут ',
    20: 'двадцать минут ',
    21: 'двадцать одна минута ',
    22: 'двадцать две минуты ',
    23: 'двадцать три минуты ',
    24: 'двадцать четыре минуты ',
    25: 'двадцать пять минут ',
    26: 'двадцать шесть минут ',
    27: 'двадцать семь минут ',
    28: 'двадцать восемь ',
    29: 'двадцать девять минут ',
    31: 'тридцать одна минута ',
    32: 'тридцать две минуты ',
    33: 'тридцать три минуты ',
    34: 'тридцать четыре минуты ',
    35: 'тридцать пять минут ',
    36: 'тридцать шесть минут ',
    37: 'тридцать семь минут ',
    38: 'тридцать восемь минут ',
    39: 'тридцать девять минут ',
    40: 'сорок минут ',
    41: 'сорок одна минута ',
    42: 'сорок две минуты ',
    43: 'сорок три минуты ',
    44: 'сорок четыре минуты ',
}

minutes2 = {
    45: 'без пятнадцати ',
    46: 'без четырнадцати ',
    47: 'без тренадцати ',
    48: 'без двенадцати ',
    49: 'без одинадцати ',
    50: 'без десяти ',
    51: 'без девяти ',
    52: 'без восьми ',
    53: 'без семи ',
    54: 'без шести ',
    55: 'без пяти ',
    56: 'без четырех ',
    57: 'без трех ',
    58: 'без двух ',
    59: 'без одной минуты ',
}

current_time = datetime.now().time().strftime('%H:%M')

minutes = current_time[3:5]
hours = current_time[0:2]
time_in_string_format(minutes, hours)

try:
    random_time = input('Введите время формата (hh:mm): \n')
    datetime.strptime(random_time, '%H:%M')
    minutes = random_time[3:5]
    hours = random_time[0:2]
    time_in_string_format(minutes, hours)

except ValueError:
    print('Incorrect Format')
