with open('text.txt', 'r') as f:
    text = f.read()

length = int(input('Количество символов в строке: '))
list_lines = []
lower_bound = 0
upper_bound = 0
last_space_position = text.rindex(' ')

while upper_bound < len(text):
    upper_bound = text.rindex(' ', lower_bound, lower_bound + length)
    if upper_bound == last_space_position:
        upper_bound = len(text)
    else:
        list_lines.append(text[lower_bound:upper_bound].strip())
        lower_bound = upper_bound
list_lines.append(text[-length:].strip())

for i in list_lines:
    i.strip()
    lines_elem = [' ' if j == '\n' else j for j in i]
    while len(lines_elem) < length:
        try:
            space_index = i.rindex(' ')
            lines_elem.insert(space_index, ' ')
            i = i[:space_index]
        except ValueError:
            i = ''.join(lines_elem)
    print(''.join(lines_elem), len(lines_elem))
