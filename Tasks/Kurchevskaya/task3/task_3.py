n=int(input("ВВедите максимальное количество символов в строке (>35):"))

with open("text.txt", 'r', encoding="utf-8") as file:
    text = file.read()
      

    def spl(textt, maxlen):
        text1 = ''
        c = 0 
        for i in text.split(' '):

            c += len(i)
            if c >= n:
                text1 += '\n'
                c = len(i)
            elif text1 != ' ':
                text1 +=' '
                c += 1
            text1 += i
        
        return text1

with open("textn.txt", "w", encoding="utf-8") as f:
    f.writelines(spl(text,n))

def space(line , number):
        raz = n-(len(line)-1)
        if not ' ' in line:
            return line
        else:     
            while raz!=0:
                for i in range(0,len(line)):
                    if line[i]==' ' and line[i-1]!=' ':
                        line = f'{line[:i]} {line[i:]}'
                        raz-=1
                    if raz==0:
                         break
                       
            return line
with open("textn.txt", "r", encoding="utf-8") as f , open("textnew.txt", "w",encoding="utf-8") as filenew:
    for line in f:
        linespace =space(line, n)
        print (linespace, end="")
        filenew.write(linespace)