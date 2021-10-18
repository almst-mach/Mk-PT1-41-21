number = {'one' : 1,'two' : 2,'three' : 3 , 'four' : 4,'five' : 5, 'six' : 6, 'seven' : 7 ,'eight' : 8 ,'nine' : 9,
          'ten' : 10 , 'eleven' : 11 , 'twelve' : 12, 'thirteen' : 13 , 'fourteen' : 14, 'fiveteen' : 15, 'sixteen' : 16,
          'seventeen' : 17, 'eighteen' : 18, 'nineteen' : 19, 'twenty' : 20 } 

a = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

list_number = sorted(list(set([number[i] for i in a.split(" ")])))
print(list_number)


list1 = []
for i in range(len(list_number)-1):
    if i%2==0:
        list1.append(list_number[i]*list_number[i+1])

    else:
        list1.append(list_number[i]+list_number[i+1])

print(list1)           


s = 0
for i in list_number:
    if i%2==1:
        s = s + i

print(s)