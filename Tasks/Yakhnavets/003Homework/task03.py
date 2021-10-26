number = int(input("Input the number of symbols more than 35\n"))

def spacer(line = str, max_lenth = int):
        
        spaces = max_lenth - len(line)
        #print(spaces)
        words_coll = line.strip().split(" ")
        #print(words_coll)
        i = 0
        while spaces >-1:      #-1 просто потому что оно пропускает один пробел непонятно почему, Объясните почему_)))
            if i == len(words_coll)-1:
                i = 0

            else:
                words_coll[i]+=" "
                i+=1
                spaces -= 1

        text = " ".join(map(str,words_coll))

        return text


def chek_input(num):
    if num<35:
        number = int(input("MORE THAN 35\n"))
        chek_input(number)
chek_input(number)

with open("/Users/developer/Documents/DEVELOPMENT/PYTHON/Yakhnavets/test.py/csv_json/home/text.txt", "r") as orig_file:
    orig_text = orig_file.read().replace("\n", " ")
    #print(orig_text)
    row_collection = []
    row_couter = 0
    final_text = ""
    words_list  = orig_text.split(" ")
    #print(words_list)
    
    for word in words_list:

        if len(row_collection) < row_couter+1:
            row_collection.append("") #нулевое добавили
        
        if len(row_collection[row_couter]+word) <= number:
            row_collection[row_couter]+=word+" "
        
        else: 

            row_collection[row_couter] = spacer(row_collection[row_couter],number)  

            #print(row_collection[row_couter])
            row_couter+=1
            row_collection.append(word+" ")

    with open("new_text.txt","w")as new_file:
        print("\n".join(row_collection),file=new_file)

print("Ваш новый текст в файле new_text.txt")



