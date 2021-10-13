from random import shuffle

x=[1,2,3,4,5,6,7,8,9,0,-1,-2]
shuffle(x)

print(x)

result=x[0]

for i in x[1:]:
    if i<result:
        result=i
  
       
print(result)
    
    