numd = {"one":1, "two":2 , "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "twenty one":21}
mystr = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()
numd = dict((i, numd[i]) for i in mystr)
print(numd)
numd = dict(sorted(numd.items(), key =lambda item: item[1])).values()
mystr = list(numd)
print(mystr)

print(sum(mystr))

print(sum(num for num in mystr if num % 2))

for i in range(len(mystr)-1):
    if  i %2 == 0:
        print(mystr[i]*mystr[i+1])
        
    elif i %2 !=0:
        print(mystr[i]+mystr[i+1])
        
