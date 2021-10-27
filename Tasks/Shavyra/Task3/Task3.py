with open("text.txt", 'r', encoding="utf-8") as in_file:
    file = in_file.readlines()

new_file = []
number = int(input("Введите число символов в строке (не менее 35): "))

for line in file:
    num = number
    while True:
        if len(line) > num:
            if line[num] != ' ':
                num -= 1
            else:
                new_file.append(line[:num])
                line = line.replace(line[:num + 1], '')
                num = number
        else:
            new_file.append(line.rstrip())
            break
len_str = []
for line in new_file:
    z = line
    i = 0
    for i in range(len(z)):
        if number > len(line):
            if line[i] == ' ':
                line = line[:i] + ' ' + line[i:]
            else:
                if i == int(len(z)):
                    len_str.append(line)
        else:
            len_str.append(line)
            break

with open("text_2_0.txt", 'w+', encoding = "utf-8") as out_file:
    for txt in len_str:
        out_file.write(txt + '\n')
    out_file.seek(0)
    empty = out_file.readlines()
    if empty != '':
        print("Ваш файл отредактирован и записан как text_2_0.txt ")
    else:
        print("Ваш файл не удалось отредактировать")
