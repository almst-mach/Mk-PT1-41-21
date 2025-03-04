import datetime
timenow = datetime.datetime.now().strftime("%H:%M")

nativeMin = { 1:"Одна", 2:"Две", 3:"Три", 4:"Четыре", 5:"Пять", 6:"Шесть", 7:"Семь", 8:"Восемь", 9:"Девять", 10:"Десять", 11:"Одиннадцать", 12:"Двенадцать", 13:"Тринадцать", 14:"Четырнадцать", 15:"Пятнадцать", 16:"Шестнадцать", 17:"Семнадцать", 18:"Восемнадцать", 19:"Девятнадцать", 20:"Двадцать", 21:"Двадцать одна", 22:"Двадцать две", 23:"Двадцать три", 24:"Двадцать четыре", 25:"Двадцать четыре", 26:"Двадцать пять", 27:"Двадцать семь", 28:"Двадцать восемь", 29:"Двадцать девять", 30:"Половина", 31:"Тридцать одна", 32:"Тридцать две", 33:"Тридцать три", 34:"Тридцать четрые", 35:"Тридцать пять", 36:"Тридцать шесть", 37:"Тридцать семь", 38:"Тридцать восемь", 39:"Тридцать девять", 40:"Сорок", 41:"Сорок одна", 42:"Сорок две", 43:"Сорок три", 44:"Сорок четыре"}
genetMin = { 45:"пятнадцати", 46:"четырнадцати", 47:"тринадцати", 48:"двенадцати", 49:"одиннадцати", 50:"десяти", 51:"девяти", 52:"восьми", 53:"семи", 54:"шести", 55:"пяти", 56:"четырех", 57:"трех", 58:"двух", 59:"одной"}
genetHours = {1:"первого", 2:"второго", 3:"третьего", 4:"четвертого", 5:"пятого", 6:"шестого", 7:"седьмого", 8:"восьмого", 9:"девятого", 10:"десятого", 11:"одиннадцатого", 12:"двеннадцатого", 13:"первого", 14:"второго", 15:"третьего", 16:"четвертого", 17:"пятого", 18:"шестого", 19:"седьмого", 20:"восьмого", 21:"девятого", 22:"десятого", 23:"одиннадцатого", 24:"двеннадцатого"}
nativHours = {1:"час", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двеннадцать", 13:"час", 14:"два", 15:"три", 16:"четыре", 17:"пять", 18:"шесть", 19:"семь", 20:"восемь", 21:"девять", 22:"десять", 23:"одиннадцать", 24:"двеннадцать", 00:"двеннадцать" }

def recursiontimeprint(timenow):
    
    partition = timenow.split(':')
    hours =int(partition[0])
    min = int(partition[1])

    if min == 0 and hours != 0 and 0<hours<=4:
        print(f"Ровно {nativHours.get(hours)} ночи")
    
    elif min == 0 and hours != 0 and 4<hours<=10:
        print(f"Ровно {nativHours.get(hours)} утра")

    elif min == 0 and hours != 0 and 10<hours<=16:
        print(f"Ровно {nativHours.get(hours)} дня")

    elif min == 0 and hours != 0 and 16<hours<=23:
        print(f"Ровно {nativHours.get(hours)} вечера")

    elif min==0 and hours==0:
        print("Полночь")

    elif min==1 or min==21 or min==31 or min==41:
        print(f'{nativeMin.get(min)} минута {genetHours.get(hours+1)}')

    elif 1<min<=4 or 21<min<=24 or 31<min<=34 or 41<min<=44 :
        print(f'{nativeMin.get(min)} минуты {genetHours.get(hours+1)}')

    elif min == 30:
        print (f'{nativeMin.get(min)} {genetHours.get(hours+1)}')

    elif min >= 45:
        print(f'Без {genetMin.get(min)} {nativHours.get(hours+1)}')

    else:
        print(f'{nativeMin.get(min)} минут {genetHours.get(hours+1)}')

    timenow = input("Введите время в формате чч:мм\n")
    recursiontimeprint(timenow=timenow)
recursiontimeprint(timenow=timenow)