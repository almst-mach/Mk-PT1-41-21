str1='qwert'
str2='rewq'
x=[i for i in str1+str2 if i not in str1 or i not in str2]
print(x)
# x=[]
# for i in str1+str2:
#     if i not in str1 or i not in str2:
#         x.append(i)
# print(x)
if not x:
    print('str1 равно str2')
else:
    print('str1 не равно str2')


if str1[0].find(str2[0])>-1:
    print('str1 contains str2')
else:
    print('str1 doesnt contains str2')

if str1==str1[::-1]:
    print('явл полиндромом') 
else:
    print('не является полиндромом')   
# def reversed_string(str1):
#     return str1[::-1]
# if str1==reversed_string(str1):
#     print('явл полиндромом') 
# else:
#     print('не является полиндромом') 