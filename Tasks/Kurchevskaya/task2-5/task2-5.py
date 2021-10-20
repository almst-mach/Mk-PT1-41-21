str5=input("Введите первую строку для сравнения:")
str6=input("Введите вторую строку для сравнения:")

if len(str5)==len(str6):
    for i in range(len(str5)):
        if str5[i]!=str6[i]:
            print("Строки не равны!")
            break
        if str5[i]==str6[i] and i==len(str5)-1:
            print("Строки равны!")
else:
    print("Строки не равны!")

str1=input("Введите первую строку для поиска подстроки:")
str2=input("Введите вторую строку для поиска подстроки:")  

i=0
if len(str1)<len(str2):
    print("Вторая строка не является подстрокой первой строки!")
else:
    for i in (range(len(str1))):
        if str1[i]==str2[0]:
            if str1[i:len(str2)+i]==str2:
                print("Вторая строка является подстрокой первой строки!")
                break
            elif i==len(str1)-1:
                print("Вторая строка не является подстрокой первой строки!")
                break
            elif str1[i:len(str2)+i]!=str2:
                continue
            
        elif str1[i]!=str2[0]:
            if i==len(str1)-1:
                print("Вторая строка не является подстрокой первой строки!")
        else:
            continue



str3=input("Введите строку на проверку палиндрома (например: Рвал дед лавр) :")
str3=str3.lower()
i=0
j=len(str3)-1
palindrom=True
while i<j:
    if str3[i] != str3[j]:
        palindrom=False
        print("Введённая строка не является палиндром !") 
        break        
    if str3[i] == str3[j]:
        i+=1
        j-=1
if palindrom:
    print("Введённая строка является палиндромом!")