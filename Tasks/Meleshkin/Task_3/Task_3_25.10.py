finish_text = []
text_x = []

def add_space():
    for text in text_x:
            s = [index for index, ch in enumerate(text) if ch == ' ']
            i = 0
            while True:
                if len(text) < width and len(s) > 0:
                    text = text[:s[i]] + ' ' + text[s[i]:]
                    s = s[:i] + [x + 1 for x in s[i:]]
                    i += 1
                    if i +1 > len(s):
                        i = 0
                else:
                    finish_text.append(text + '\n')
                    break

def change(Text):
    for line in Text:
        piece = width
        line = line.rstrip()
        while True:
            if len(line) > piece:
                if line[piece] != ' ':
                    piece -= 1
                else:
                    text_x.append(line[:piece])
                    line = line.replace(line[:piece +1], '')
                    piece = width
            else:
                text_x.append(line.rstrip() + ' ')
                break


start = True
width = int(input('Enter the number more 35: \n '))
while start:
    if width > 35:
        with open('text.txt', 'r', encoding='utf-8') as file:
            change(file.readlines())
            add_space()
        with open('Text_out.txt', 'w', encoding='utf-8') as file_2:
            for txt in finish_text:
                file_2.write(txt)
            print('Ready!')   
    else:
        print('Incorrect number ')
    width = int(input('Enter the number more 35: \nIf you want to exit enter any word or symbol: \n'))
    if width < 35:
        start = False