from datetime import datetime 
import sys
min_now = datetime.now().strftime('%M')
hour_now = datetime.now().strftime('%H')
a = input('Введите нужное вам время (часы от 00 до 23) ')
b = input('Введите нужное вам время (минуты от 00 до 59) ')
min_00 = {"01" : "Час ночи", "02" : "Два часа ночи", "03" : "Три часа ночи", "04" : "Четыре часа утра", "05" : "Пять часов утра", "06" : "Шесть часов утра", \
    "07" : "Семь часов утра", "08" : "Восемь часов утра", "09" : "Девять часов утра", "10" : "Десять часов утра", \
        "11" : "Одинадцать часов утра", "12" : "Полдень", "13" : "Час дня", "14" : "Два часа дня", "15" : "Три часа дня", \
            "16" : "Четыре часа дня", "17" : "Пять часов дня", "18" : "Шесть часов вечера", "19" : "Семь часов вечера", \
                "20" : "Восемь часов вечера", "21" : "Девять часов вечера", "22" : "Десять часов вечера", "23" : "Одинадцать часов вечера", \
                    "00" : "Полночь"}
min_1_30 = {"01" : "Одна минута ", "02" : "Две минуты ", "03" : "Три минуты ", "04" : "Четыре минуты ", "05" : "Пять минут ", "06" : "Шесть минут ", \
    "07" : "Семь минут ", "08" : "Восемь минут ", "09" : "Девять минут ", "10" : "Десять минут ", \
             "11" : "Одинадцать минут ", "12" : "Двенадцать минут ", "13" : "Тринадцать минут ", "14" : "Четырнадцать минут ", \
                 "15" : "Пятнадцать минут ", "16" : "Шестнадцать минут ", "17" : "Семнадцать минут ", "18" : "Восемандцать минут ", \
                     "19" : "Девятнадцать минут ", "20" : "Двадцать минут ", "21" : "Двадцать одна минута ", "22" : "Двадцать две минуты ", \
                         "23" : "Двадцать три минуты ", "24" : "Двадцать четыре минуты ", "25" : "Двадцать пять минут ", \
                             "26" : "Двадцать шесть минут ", "27" : "Двадцать семь минут ", "28" : "Двадцать восемь минут ", "29" : "Двадцать девять минут "}
min_30 = {"30" : "Половина "}
min_30_45 = {"31" : "Тридцать одна минута ", "32" : "Тридцать две минуты ", "33" : "Тридцать три минуты ", "34" : "Тридцать четыре минуты ", \
    "35" : "Тридцать пять минут ", "36" : "Тридцать шесть минут ", "37" : " Тридцать семь минут ", "38" : "Тридцать восемь минут ", \
        "39" : "Тридцать девять минут ", "40" : "Сорок минут ", "41" : "Сорок одна минута ", "42" : "Сорок две минуты ", "43" : "Сорок три минуты ", \
            "44" : "Сорок четыре минуты "}
min_45_59 = {"45" : "Без пятнадцати минут ", "46" : "Без четырнадцати минут ", "47" : "Без тринадцати минут ", \
    "48" : "Без двенадцати минут ", "49" : "Без одинадцати минут ", "50" : "Без десяти минут ", "51" : "Без девяти минут ", "52" : "Без восьми минут ", \
        "53" : "Без семи минут ", "54" : "Без шести минут ", "55" : "Без пяти минут ", "56" : "Без четырех минут ", "57" : "Без трех минут ", \
            "58" : "Без двух минут ", "59" : "Без одной минуты "}
hour = { "00" : "первого", "01" : "второго", "02" : "третьего", "03" : "четвертого", "04" : "пятого", "05" : "шестого", \
     "06" : "седьмого", "07" : "восьмого", "08" : "девятого", "09" : "десятого", "10" : "одинадцатого", "11" : "двенадцатого", \
         "12" : "первого", "13" : "второго", "14" : "третьего", "15" : "четвертого", "16" : "пятого", "17" : "шестого", "18" : "седьмого", \
             "19" : "восьмого", "20" : "девятого", "21" : "десятого", "22" : "одинадцатого", "23" : "двенадцатого"}
hour_45_59 = {"00" : "час", "01" : "два", "02" : "три", "03" : "четыре", "04" : "пять", "05" : "шесть", \
     "06" : "семь", "07" : "восемь", "08" : "девять", "09" : "десять", "10" : "одинадцать", "11" : "двенадцать", \
         "12" : "час", "13" : "два", "14" : "три", "15" : "четыре", "16" : "пять", "17" : "шесть", "18" : "семь", \
             "19" : "восемь", "20" : "девять", "21" : "десять", "22" : "одинадцать", "23" : "двенадцать"}
# Время в данный момент
if int(min_now) == 00 :
        print(min_00.get(hour_now))
elif int(min_now) < 30 :
        print(min_1_30.get(min_now) + hour.get(hour_now))
elif int(min_now) == 30 :
    print(min_30.get(min_now) + hour.get(hour_now))
elif int(min_now) > 30:
    if int(min_now) < 45:
        print(min_30_45.get(min_now) + hour.get(hour_now))
elif int(min_now) >= 45:
        print(min_45_59.get(min_now) + hour_45_59.get(hour_now))
# Введенное время           
if int(b) > 59:
    sys.exit('Неверный формат минут, попробуйте еще раз')
if int(a) > 23:
    sys.exit('Неверный формат часов, попробуйте еще раз')

if int(b) == 00 :
    print(min_00.get(a))
elif int(b) < 30 :
    print(min_1_30.get(b) + hour.get(a))
elif int(b) == 30 :
    print(min_30.get(b) + hour.get(a))
elif int(b) > 30:
    if int(b) < 45:
        print(min_30_45.get(b) + hour.get(a))
    elif int(b) > 45:
        print(min_45_59.get(b) + hour_45_59.get(a))    
