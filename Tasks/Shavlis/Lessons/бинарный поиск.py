l = [3,4,5,6,7,8,9,10,11,12]

def bin(x, y):
    a = 0 
    b = len(x)-1
    mid = (a + b)//2

    if (y == x[mid]):
        return mid
   
    elif (y > x[mid]):
        return bin(x[mid+1:], y) + (mid + 1)
    else:
        return bin(x[:mid], y)

print(bin(l,9))