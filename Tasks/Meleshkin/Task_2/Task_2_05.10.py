from datetime import datetime

current_time = str(datetime.now().strftime('%I-%M'))    #Получаем время в строковом типе в 12-ти часовом формате
minutes, hours = current_time[3:], current_time[:2]     #Выделил две переменные минуты и часы          
print(str(datetime.now().strftime('%H:%M')))    #Сделал вывод текущего времени                               
hours_dict = {'00':'первого','01':'второго','02':'третьего','03':'четвертого','04':'пятого','05':'шестого','06':'седьмого','07':'восьмого','08':'девятого','09':'десятого','10':'одинадцатого','11':'двенадцатого','12':'первого'}
minutes_dict_case_one = {'00':'ноль','01':'одна','02':'две','03':'три','04':'четыре','05':'пять','06':'шесть','07':'семь','08':'восемь','09':'девять','10':'десять','11':'одинадцать','12':'двенадцать','13':'тринадцать','14':'четырнадцать','15':'пятнадцать','16':'шестнадцать','17':'семнадцать','18':'восемнадцать','19':'девятнадцать','20':'двадцать','21':'двадцать одна','22':'двадцать две','23':'двадцать три','24':'двадцать четыре','25':'двадцать пять','26':'двадцать шесть','27':'двадцать семь','28':'двадцать восемь','29':'двадцать девять',}
minutes_dict_case_two = {'31':'тридцать одна','32':'тридцать две','33':'тридцать три','34':'тридцать четыре','35':'тридцать пять','36':'тридцать шесть','37':'тридцать семь','38':'тридцать восемь','39':'тридцать девять','40':'сорок','41':'сорок одна','42':'сорок две','43':'сорок три','44':'сорок четыре'}
minutes_dict_case_three = {'45':'пятнадцати','46':'четырнадцати','47':'тринадцати','48':'двенадцати','49':'одинадцати','50':'десяти','51':'девяти','52':'девяти','53':'семи','54':'шести','55':'пяти','56':'четырех','57':'трех','58':'двух','59':'одной',}
if 0 <= int(minutes) < 30:
    if int(minutes) == 2 or int(minutes) == 3 or int(minutes) == 4 or int(minutes) == 22 or int(minutes) == 23 or int(minutes) == 24:
        print(f"{minutes_dict_case_one[minutes]} минуты {hours_dict[hours]}") #Хотел сделать через or и остаток от 
    elif int(minutes) == 1 or int(minutes) == 21:                                                   #деления,но 12,13,14 будут портить вывод
        print(f"{minutes_dict_case_one[minutes]} минута {hours_dict[hours]}")
    else:  
        print(f"{minutes_dict_case_one[minutes]} минут {hours_dict[hours]}")
elif int(minutes) == 30:
    print(f"половина {hours_dict[hours]}")
elif 30 < int(minutes) < 45:
    if int(minutes) == 42 or int(minutes) == 43 or int(minutes) == 44 or int(minutes) == 32 or int(minutes) == 33 or int(minutes) == 34:
        print(f"{minutes_dict_case_two[minutes]} минуты {hours_dict[hours]}")
    elif int(minutes)%10 == 1:
        print(f"{minutes_dict_case_two[minutes]} минута {hours_dict[hours]}")
    else:
        print(f"{minutes_dict_case_two[minutes]} минут {hours_dict[hours]}")
else:
    if int(minutes) == 1:
        print(f"Без {minutes_dict_case_three[minutes]} минуты {hours_dict[hours]}")
    else:
        print(f"Без {minutes_dict_case_three[minutes]} минут {hours_dict[hours]}")
