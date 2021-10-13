from datetime import datetime

def clock_text(minut, hour):
    hour_dict = {1: "первого", 2: "второго", 3: "третьего", 4: "четвёртого", 5: "пятого", 6: "шестого", 7: "седьмого", 8: "восьмого", 9: "девятого", 10: "десятого", 11: "одинадцатого", 12: "двенадцатого", 13: "первого", 14: "второго", 15: "третьего", 16: "четвёртого", 17: "пятого", 18: "шестого", 19: "седьмого", 20: "восьмого", 21: "девятого", 22: "десятого", 23: "одинадцатого", 24: "двенадцатого"}
    hour_dict_2 = {1: "час", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "час", 14: "два", 15:"три", 16: "четыре", 17: "пять", 18: "шесть", 19: "семь", 20: "восемь", 21: "девять", 22: "десять", 23: "одинадцать", 24: "двенадцать"}
    minut_dict_1 = {2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят"}
    minut_dict_2 = {0: "ноль", 1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
    minut_dict_3 = {1: "одной", 2: "двух", 3: "трёх", 4: "четырёх", 5: "пяти", 6: "шести", 7: "семи", 8: "восьми", 9: "девяти", 10: "десяти", 11: "одинадцати", 12: "двенадцати", 13: "тринадцати", 14: "четырнадцати", 15: "пятнадцати"}
    
    if minut < 30 and minut != 0:
        if 0 < minut < 20:
            if 4 < minut < 20 or minut == 0: 
                print(f"{minut_dict_2[minut]} минут {hour_dict[hour+1]}")
            elif 1 < minut < 5:
                print(f"{minut_dict_2[minut]} минуты {hour_dict[hour + 1]}")
            else:
                print(f"{minut_dict_2[minut]} минута {hour_dict[hour + 1]}")
        else:
            if minut % 10 == 1:
                print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минута {hour_dict[hour + 1]}")
            elif 1 < minut % 10 < 5:
                print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минуты {hour_dict[hour + 1]}")
            elif minut % 10 == 0:
                print(f"{minut_dict_1[minut//10]} минут {hour_dict[hour + 1]}")
            else:
                print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минут {hour_dict[hour + 1]}")
                
    elif minut == 30:
        print(f"половина {hour_dict[hour]}")

    elif minut > 30 and minut < 45:
        if minut % 10 == 1:
            print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минута {hour_dict[hour + 1]}")
        elif 1 < minut % 10 < 5:
            print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минуты {hour_dict[hour + 1]}")
        elif minut % 10 == 0:
            print(f"{minut_dict_1[minut//10]} минут {hour_dict[hour + 1]}")
        else:
            print(f"{minut_dict_1[minut//10]} {minut_dict_2[minut%10]} минут {hour_dict[hour + 1]}")

    elif minut >= 45:
        print(f"без {minut_dict_3[60-minut]} {hour_dict_2[hour + 1]}")
    
    elif hour!= 0 and minut == 0:
        if hour == 13 or hour == 1:
            print(f"{hour_dict_2[hour]}")
        elif 1 < hour < 5 or 13 < hour < 17:
            print(f"{hour_dict_2[hour]} часа")
        else:
            print(f"{hour_dict_2[hour]} часов")

    elif minut == 0 and hour == 0:
        print("полночь")

t = str(datetime.now())
t = t.split(' ')
t = t[1].split('.')
t = t[0].split(':')
h, m = int(t[0]), int(t[1])
if 0 <= m < 10:
    print(f"Систeмное время: {h}:0{m}")
else:
    print(f"Системное время: {h}:{m}")
clock_text(m, h)

h, m = [int(i) for i in input("Введите время и минуты в формате hh:mm :\n").split(':')]
if 0 <= m < 60 and 0 <= h < 24:
    clock_text(m,h)
else:
    print("Введите корректное время.")