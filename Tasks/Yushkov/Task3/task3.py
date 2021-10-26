with open("text.txt", 'r', encoding="utf-8") as in_file:
    file = in_file.readlines()

new_file = []
user_number = int(input("Please, enter your number of character (more than 35): "))

for line in file:
    numb = user_number
    while True:
        if len(line) > numb:
            if line[numb] != ' ':
                numb -= 1
            else:
                new_file.append(line[:numb])
                line = line.replace(line[:numb + 1], '')
                numb = user_number
        else:
            new_file.append(line.rstrip())
            break


with open("format_text.txt", 'w+', encoding = "utf-8") as out_file:
    for txt in new_file:
        out_file.write(txt + '\n')
    out_file.seek(0)
    empty = out_file.readlines()
    if empty != '':
        print("Your file was written")
    else:
        print("Your file was not written")
