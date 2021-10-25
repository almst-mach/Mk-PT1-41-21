running = True
Text_u = []
Text_out = []
width = int(input('введите число больше 35: \n'))
 
def lener():
    for line in Text:
        chunks = width
        line = line.rstrip()
        while True:
            if len(line) > chunks:
                if line[chunks] != ' ':
                    chunks -= 1
                else:
                    Text_u.append(line[:chunks])
                    line = line.replace(line[:chunks +1], '')
                    chunks = width
            else:
                Text_u.append(line.rstrip() + ' ')
                break

def space():
    for text in Text_u:
            s = [index for index, char in enumerate(text) if char == ' ']
            i = 0
            while True:
                if len(text) < width and len(s) > 0:
                    text = text[:s[i]] + ' ' + text[s[i]:]
                    s = s[:i] + [x + 1 for x in s[i:]]
                    i += 1
                    if i +1 > len(s):
                        i = 0
                else:
                    Text_out.append(text + '\n')
                    break

while running:
    if width > 35:
        with open('text.txt', 'r', encoding='utf-8') as f:
            Text= f.readlines()
        lener()
        space()
        with open('Text_out.txt', 'w', encoding='utf-8') as f2:
            for txt in Text_out:
                f2.write(txt)
            print('записано')   
    else:
        print('неверно ввели число ')
    answer = input("Would you like to run again? (y/N)")
    width = int(input('введите число больше 35: \n'))
    if answer != 'y':
        running = False