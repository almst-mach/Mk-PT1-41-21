b = input('Количество символов ')

with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\text.txt', encoding = 'UTF-8') as f:
    a = f.read(int(b))
    
with open(r'C:\python\Mk-PT1-41-21\Tasks\Shavlis\text2.txt', 'w', encoding = 'UTF-8') as f:
    f.write(a)

print(f)     
