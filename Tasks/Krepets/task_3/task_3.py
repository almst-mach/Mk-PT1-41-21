import os 

def symbols():
    s = int(input('Enter number of symbols in one string(more than 35): '))
    while True:
        if s > 35:
            break
        elif s <= 35:
            s = int(input('You entered number less than 35, try again: '))
    return s 

def write_text_in_file():
    k = os.stat('/Users/antonkrepec/Documents/GitHub/Mk-PT1-41-21/Tasks/Krepets/task_3/text_formatted.txt').st_size == 0
    if k is False:
        print('The text was successfully written to the file')
    else:
        print('The text was not recorded!')

def add_space(formatted_list, s):
    lines_list = []
    for line in formatted_list:
        space = [index for index, space in enumerate(line) if space == ' ']
        i = 0
        while True:
            if (len(line) - 1) < s and len(space) > 0:
                k = [x + 1 for x in space[i:]]
                line = line[:space[i]] + ' ' + line[space[i]:]
                space = space[:i] + k
                i += 1
                if i + 1 > len(space):
                    i = 0
            else:
                lines_list.append(line)
                break
    return lines_list
        

with open('/Users/antonkrepec/Documents/GitHub/Mk-PT1-41-21/Tasks/Krepets/task_3/text_formatted.txt', 'w') as f, open('/Users/antonkrepec/Documents/GitHub/Mk-PT1-41-21/Tasks/Krepets/task_3/text.txt', 'r') as x:
    data = x.read()
    s = symbols()
    formatted_list = []
    for line in data.split('\n'):
        count = 0
        string = []
        for elem in line.split(' '):
            if count + len(elem) + 1 <= s:
                string.append(elem)
                count += len(elem) + 1
            else:
                formatted_list.append((' ').join(string) + '\n')
                string = [elem]
                count = len(elem)
        formatted_list.append((' ').join(string) + '\n')
    list_with_spaces = add_space(formatted_list, s)
    f.write(''.join(list_with_spaces))
    write_text_in_file()

