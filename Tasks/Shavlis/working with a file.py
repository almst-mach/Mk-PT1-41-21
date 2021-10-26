b = int(input('Максимально количество символов в строке (больше 35): '))
while True:
    if b > 35:
        break
    elif b <= 35:
        b = int(input('Максимально количество символов в строке (больше 35): '))

with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\text.txt', 'r', encoding='utf-8') as t:  
    with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\formatted text.txt', 'a', encoding = 'UTF-8') as f:
        for line in t:
            t = line.split()
            p = ''
            for i in range(len(t)):
                p += t[i] + ' '
                if len(p) == b:
                    f.write(p[:-1] + '\n')
                    p = ''

                if i == (len(t) - 1):
                    f.write(p[:-1] + '\n')
                    p = ''
                    break
                
                if len(p)+1 + len(t[i+1]) > b:
                    
                    d = p.split()
                    c = b - len(p)
                    for i in range(len(p)-1):
                        if len(p) == b:
                            break
                        for j in range(len(d)-1): 
                            p = p.replace(d[j], d[j] + ' ')
                            if len(p) == b:
                                break   
                    f.write(p[:-1] + '\n')
                    p = ''
                
                # if len(p) + len(t[i+1]) > b:
                #     p = p.rstrip()
                #     d = p.split()
                #     c = b - len(p)
                #     for i in range(c):
                #         if len(p) == b:
                #             break
                #         for j in range(len(d)-1): 
                #             p = p.replace(' ', '  ')
                #             if len(p) == b:
                #                 break   
                #     f.write(p + '\n')
                #     p = ''


                    


# s = 'asfs fasf asd dfdsadfads dasas'
# b = 50
# d = s.split()
# c = b - len(s)
# for i in range(c):
#     if len(s) == b:
#         break
#     for j in range(len(d)-1): 
#         s = s.replace(d[j], d[j] + ' ')
#         if len(s) == b:
#             break
                            
                            
# print(s)
# print(len(s))

# s = 'asfs fasf asd dfdsadfads dasas'
# b = 35
# d = s.split()
# c = b - len(s)
# for i in range(c):
    
#     for j in range(len(d)-1): 
#         s = s.replace(' ',  ' ' * j)
        
                            
                            
#         print(s)
#         print(len(s))

