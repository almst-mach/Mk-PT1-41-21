l='five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
l=l.split(' ')
b=[]
d={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fiveteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
for i in l:
    b.append(d[i])

c=[]
for i in b:
    if not i in c:
        c.append(i)   #без дубликатов

# c=sorted(c)      #сортировка
# print(c) 

for w in range(len(c)-1):                  #сортировка
    for i in range((len(c)-1)-w):
        if c[i]>c[i+1]:
            c[i],c[i+1]=c[i+1],c[i]
print(c)        

s=0
for i in c:
    if i%2!=0:
        s=s+i
print(s)        #сумма нечетных

for i in range(len(c)-1):
    if i%2==0:
        print(c[i]*c[i+1]) #произведения
    else:
        print(c[i]+c[i+1]) #суммы