# к сожалению, я так и не добилась правильного результата, иногда считает правильно, иногда нет. Сбрасываю что хоть есть
#работала с целыми числами, начала с decimal, но что-то пошло не так(
while True:
    total = int(input('Введите счёт в ресторане:'))
    n = int(input('Введите кол-во участников:'))
    try:
        total = int(total)
        n = int(n)
        assert total > 0, "Сумма в чеке не может быть отрицательной!"
        
        assert n > 2,     "Если участников встречи меньше двух, то и делить счёт не с кем!"
        break
    except AssertionError as error:
        print(error)
        continue
    except (TypeError, ValueError):
        print('Некорректно введены данные, попробуйте ещё раз!!!')
        continue


while True:
    amount = []

    for num  in range(1,n+1):
        amount.append(int(input(f"Сколько внес {num} участник ? ")))
    
    try:
        #здесь я хотела обработать исключения элементов списке при вводе пользователем, но так и  не нашла способа
        assert sum(amount) == total, "Cумма, внесённая всеми участниками не должна отличаться от суммы в счёте! "
        break
    except AssertionError as error:
        print(error)
        continue   
    except RuntimeError as error:
        print(error)
        continue
    except (TypeError, ValueError):
        print('Некорректно введены данные, попробуйте ещё раз!')
        continue

avg = total/n

#словарь для тех, кто не доплатил, в словаре сумма, которую они должны доплатить
print("должники должны доплатить:")
dict1 = {i+1: avg-amount[i] for i in range(0, len(amount)) if amount[i]<avg }
print(dict1)
print()
#Словарь для тех кто переплатил, в словаре сумма, которую им должны
print("Этим участникам должны доплатить такие суммы:")
dict2 = {i+1: amount[i]-avg for i in range(0, len(amount)) if amount[i]>=avg }
print(dict2)

h=0
for k1, v1 in dict1.items():
    for k2, v2 in dict2.items():
        while dict1[k1]!=0 :
            #   while dict[k2]!=0:
            if  dict2[k2]==0:
                break
            if  v1 == v2:
                print ("должник №" ,k1," отдал №", k2,"-", v1)
                dict1[k1]=v1-v1
                dict2[k2]=v2-v1 
                     
            elif v1>=v2:
                h=v1-v2
                print ("должник №" ,k1," отдал №", k2,"-", v2)
                dict1[k1]=v1-v2
                dict2[k2]=v2-v2
                        
            elif v1<=v2:
                print ("должник №" ,k1," отдал №", k2,"-", v1)
                dict2[k2]=v2-v1
                dict1[k1]=v1-v1
            
