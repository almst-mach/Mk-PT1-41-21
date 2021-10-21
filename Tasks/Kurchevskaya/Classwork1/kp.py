st = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
st1 =st.split()
print("Создаём список")
print(st1)
dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5, 'six':6,'seven':7,'eight':8, 'nine':9,'ten':10,'eleven':11,'thirteen':13,'seventeen':17,'nineteen':19,'twenty one':21}

out_list = [dict[elem] for elem in st1]
print("Преобразование в числа:")
print(out_list)

#исключить дубликаты
print("Исключаем дубликаты set:")
st2=set(out_list)
print(st2)
print("Исключаем дубликаты генератором:")
st3 = {x for x in out_list}
print(st3)

#отсортировать по возрастанию
print("Сортируем список:")
new_list=sorted(st2)
print(new_list)

#выводим сумму всех нечётных чисел
#count = 0
#for elem in new_list:
#    if elem % 2 != 0:
#        count=count+elem
#print("Сумма всех нечетных элементов:",count)

s=sum([elem for elem in new_list if  elem % 2 != 0])
print("Сумма с помощью генератора:\n",s)

#проозведение первого и второго, сумму второго и третьего, произведение третьего и четвёртого и т.д.

print("Произведение и сумма элементов:")     
new_l1 = []
for index in range(len(new_list)-1):
    if  index %2 == 0:
        fin = new_list[index]*new_list[index+1]
        new_l1.append(fin)
    elif index %2 != 0:
        fin2 = new_list[index]+new_list[index+1]
        new_l1.append(fin2)
print(new_l1)    
