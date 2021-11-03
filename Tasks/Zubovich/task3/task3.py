with open("text.txt", "r") as f:
    textt = f.read().split()
print(textt)
max_len = int(
    input("Введите максимальное количество символов в строке, который должен быть больше 35: "))


def on_the_lines():
    result = ''
    a = 0
    for i in textt:
        a += len(i)
        if a >= max_len:
            result += '\n'
            a = len(i)
        elif result != '':
            result += ' '
            a += 1
        result += i
    return result


result = on_the_lines()
print(result)
result = on_the_lines().splitlines()
print(result)


def width():
    b = []
    for text in result:
        space_index = [index for index, char in enumerate(text) if char == ' ']
        i = 0
        while True:
            if len(text) <= max_len and len(space_index) > 0:
                text = text[:space_index[i]] + ' ' + text[space_index[i]:]
                space_index = space_index[:i] + list(map(lambda x: x + 1, space_index[i:]))
                i += 1
                if i + 1 > len(space_index):
                    i = 0
            else:
                b.append(text + '\n')
                break
    return b


result2 = ("".join(width()))
print(result2)

with open("text1.txt", "w") as file1:
    file1.writelines(result2)

print('Отредактированный текст сохранен в файл text1.txt ')