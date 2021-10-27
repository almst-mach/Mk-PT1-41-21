#Text file was written with count = 50
with open("text.txt", 'r', encoding="utf-8") as f:
    data = f.readlines()

data_upd = []
count = int(input("Input number more than 35: "))

if count > 35:
    for line in data:
        cut = count
        while True:
            if len(line) > cut:
                if line[cut] != ' ':
                    cut -= 1
                else:
                    data_upd.append(line[:cut])
                    line = line.replace(line[:cut + 1], '')
                    cut = count
            else:
                data_upd.append(line.rstrip() + ' ')
                break

    output = []
    for text in data_upd:
        space_index = [index for index, char in enumerate(text) if char == ' ']
        i = 0
        while True:
            if len(text) < count and len(space_index) > 0:
                text = text[:space_index[i]] + ' ' + text[space_index[i]:]
                space_index = space_index[:i] + [x + 1 for x in space_index[i:]]
                i += 1
                if i + 1 > len(space_index):
                    i = 0
            else:
                output.append(text + '\n')
                break

    with open("output.txt", 'w+', encoding = "utf-8") as file_out:
        for txt in output:
            file_out.write(txt)
        file_out.seek(0)
        is_empty = file_out.readlines()
        if is_empty != '':
            print("File successfully was written")
        else:
            print("File was not written")
else:
    print("Input correct number")