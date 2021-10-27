len_str = int(input('Введите максимальное количество символов в строке (минимальное значение: 35): '))


def space(words, length): 
    len_words = 0
    for i in range(len(words)):
        len_words += len(words[i])
    spaces = length - len_words 
               
    while spaces > 0:
        for i in range(len(words)-1):
            words[i] += ' '
            spaces -= 1
            if spaces == 0:
                break
                
    new_line = ''.join(words)
    return(new_line)


new_text = ''
def write_lines(new_line):
    global new_text
    new_text += new_line + '\n'

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

      

count = 0
while count in range(len(text)):

    if (count + len_str) > len(text):
        line = text[count : len(text)]
    else:
        line = text[count : count + len_str]

    if line.find('\n') != -1:

        if line.endswith('\n'):
            write_lines(line)
            count += len_str
        else:    
            words = line.split('\n')
            last_word = len(words[-1])
            words = words[0].split(' ')
            
            if len(words) == 1:
                new_line = str(words[0])
                write_lines(new_line)
                count += (len(new_line)+1)
            else:
                new_line = space(words, len_str)   
                write_lines(new_line)
                count += (len_str - last_word)

    elif line.endswith(' '):
        words = line.strip().split(' ')
        new_line = space(words, len_str)   
        write_lines(new_line)
        count += len_str
    
    else:
        words = line.split(' ')
        last_word = len(words[-1]) 
        
        if len(words) == 1:
                new_line = words[0]
                write_lines(new_line)
                count += len(new_line)
        else:
            
            if (count + len_str) < len(text):
                words.pop()
            else:
                pass 
            
            new_line = space(words, len_str)   
            write_lines(new_line)
            count += (len_str - last_word)

with open('new_text.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)