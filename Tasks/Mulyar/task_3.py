with open("text.txt", 'r',encoding="utf-8")as text:
    text=text.readlines()
list1=[]
readytext=[]
x=int(input("введите число > 35===>>>>> "))
if x<=35:
    while x<=35:
        x=int(input("введите число > 35===>>>>> "))
z=x
for l in text:
    while True:
        if len(l)>z:
            if l[z]!=' ':
                z -= 1
            else:
                list1.append(l[:z])
                l=l.replace(l[:z+1],'')
                z=x
        else:
            list1.append(l.rstrip())
            break
for l in list1:
    q=l
    c=0
    for c in range(len(q)):
        if x>len(l):
            if l[c]==' ':
                l=l[:c]+' '+l[c:]
            else:
                if c==len(q):
                    readytext.append(l)
        else:
            readytext.append(l)
            break
with open("readytext.txt",'w+',encoding="utf-8") as write_text:
    for i in readytext:
        write_text.writelines(i + '\n')

