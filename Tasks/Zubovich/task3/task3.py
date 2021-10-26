max_len = int(
    input("Введите максимальное количество символов в строке, который должен быть больше 35: "))

with open("text.txt", "r") as file:
    text = file.read()


def spl(textt, maxlen):
    text1 = ''
    a = 0
    for i in text.split():
        a += len(i)
        if a >= max_len:
            text1 += '\n'
            a = len(i)
        elif text1 != '':
            text1 += ' '
            a += 1
        text1 += i
    return text1


with open("text1.txt", "w+") as file1:
    file1.writelines(spl(text, max_len))


