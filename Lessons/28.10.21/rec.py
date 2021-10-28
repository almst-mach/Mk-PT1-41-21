def print_10(text, counter=0):
    if counter == 10:
        return counter
    print(text)
    x = print_10(text, counter+1)
    print(x)
    return counter

# print_10("some text")

def factorial(x):
    if x == 0:
        return 1
    return x*factorial(x-1)

#10*factorial(9)
#10*9*factorial(8)
#factorial(10)*factorial(9)*factorial(8)
#factorial(10)*...*factorial(0)
#factorial(10)*factorial(9)*...*factorial(1)*1
#factorial(10)*factorial(9)*...*factorial(2)*1*1
#factorial(10)*factorial(9)*...*factorial(3)*2*1*1
#factorial(10)*factorial(9)*...*factorial(4)*3*2*1*1
#factorial(10)*factorial(9)*...*factorial(5)*4*3*2*1*1
#factorial(10)*factorial(9)*...*factorial(6)*5*4*3*2*1*1
#factorial(10)*factorial(9)*...*factorial(7)*6*5*4*3*2*1*1
#factorial(10)*factorial(9)*factorial(8)*7*6*5*4*3*2*1*1
#factorial(10)*factorial(9)*8*7*6*5*4*3*2*1*1
#factorial(10)*9*8*7*6*5*4*3*2*1*1
#10*9*8*7*6*5*4*3*2*1*1


x = factorial(10)
print(x)