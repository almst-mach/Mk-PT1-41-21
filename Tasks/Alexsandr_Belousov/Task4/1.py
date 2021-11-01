try:
    s=input('Input string:')
    s=s.split(',')
    for i in range(0,len(s)-1):
        int(s[i])
except ValueError:
    print("Преобразование прошло неудачно") 
    
counter=0 
h=False  

for i in range(0,len(s)-1):
    try:
        if h and not int(s[i+1])==int(s[i])+1:
            s[counter+1:i]='-'
            h=False
            i=counter-1
        elif not h and int(s[i+1])==int(s[i])+1:
            h=True
            counter=i
        if i==len(s)-2:
            if h:
                s[counter+1:i+1]='-'
    except IndexError as error:
        print(error)
        
x=''
for i in range(0,len(s)):
    if not s[i]=='-' and not s[i-1]=='-' and not x=='':
        x=x+','+s[i]
    else:
        x=x+s[i]
        
print(x)