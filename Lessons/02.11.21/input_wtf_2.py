num = str(input("Input the list of numbers\n"))
def isnum(lst):    
    numbers = []
    for i in lst.split(","):
        numbers += i
        if i == int(i):
            return numbers

while True:
    try:
        isnum(num)
        break
    except ValueError:
        num = str(input("THE LIST OF NUMBERS LIKE:\n 1,2,3,4,5\n"))
        continue