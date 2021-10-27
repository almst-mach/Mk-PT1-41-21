b = int(input('Максимально количество символов в строке (больше 35): '))
while True:
    if b > 35:
        break
    elif b <= 35:
        b = int(input('Максимально количество символов в строке (больше 35): '))

with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\text.txt', 'r', encoding='utf-8') as t:  
    with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\formatted text.txt', 'w', encoding = 'UTF-8') as f:
        for line in t:
            t = line.split()
            p = ''
            for i in range(len(t)):
                p += t[i] + ' '
                
                if len(p) - 1 == b:
                    p = p.rstrip()
                    f.write(p + '\n')
                    p = ''
                
                if i == (len(t) - 1):
                    p = p.rstrip()
                    f.write(p + '\n')
                    p = ''
                    break
                
                if len(p) + len(t[i+1]) > b:
                    p = p.rstrip()
                    while len(p) < b:
                        p = p.replace(p.split()[0], p.split()[0] + ' ')
                    if len(p) > b:
                        p = p.replace(' ', '')    
                    f.write(p + '\n')
                    p = ''
print('Отформатированный текст находится в файле formatted text.txt')
                
                
                
                
                
                # if len(p) + len(t[i+1]) > b:
                #     p = p.rstrip()
                #     d = p.split()
                #     c = b - len(p)
                #     for i in range(len(d)-1):
                #         if len(p) == b:
                #             break
                #         for j in range(len(d)-1): 
                #             p = p.replace(d[j], d[j] + ' ')
                #             if len(p) < b:
                #                 continue
                #             else:
                #                 break   
                #     f.write(p + '\n')
                #     print(len(p))
                #     p = ''