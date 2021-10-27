with open("text.txt", 'r', encoding="utf-8") as f:
    tekst = f.readlines()

my_tekst = []
digit = int(input("Введите число больше 35: "))

if digit > 35:
    for line in tekst:
        cut_digit = digit
        while True:
            if len(line) > cut_digit:
                if line[cut_digit] != ' ':
                    cut_digit -= 1
                else:
                    my_tekst.append(line[:cut_digit])
                    line = line.replace(line[:cut_digit + 1], '')
                    cut_digit = digit
            else:
                my_tekst.append(line.rstrip() + ' ')
                break

    w_tekst = []
    for text in my_tekst:
        probel = [index for index, char in enumerate(text) if char == ' ']
        i = 0
        while True:
            if len(text) < digit and len(probel) > 0:
                text = text[:probel[i]] + ' ' + text[probel[i]:]
                probel = probel[:i] + [x + 1 for x in probel[i:]]
                i += 1
                if i + 1 > len(probel):
                    i = 0
            else:
                w_tekst.append(text + '\n')
                break

    with open("w_tekst.txt", 'w+', encoding = "utf-8") as fw:
        for txt in w_tekst:
            fw.write(txt)
        fw.seek(0)
        empty_f = fw.readlines()
        if empty_f != '':
            print("Файл записан")
        else:
            print("Файл не записан")
else:
    print("Вы ввели неверное число!")