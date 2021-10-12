str="five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
listed_str=str.split()
print(listed_str)


listed_str=list(set(listed_str)) 
print(listed_str)


chisla={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19, "twenty":20, "twenty one":21}

chisla_v_chislax=[]

for x in listed_str:
    print(chisla.get(x))
    chisla_v_chislax.append(chisla.get(x))
print("\n\n\n")
print(chisla_v_chislax)
print("\n\n\n")

for i in range(len(chisla_v_chislax)-1):
    k = i
    t = i+1
    while t < len(chisla_v_chislax):
        if chisla_v_chislax[k]>=chisla_v_chislax[t]:
            k = t
        t += 1
    chisla_v_chislax[i], chisla_v_chislax[k] = chisla_v_chislax[k], chisla_v_chislax[i]

print(chisla_v_chislax)
print("\n\n\n")

result_oper_with_chisla=[]
op=0
for i in range(len(chisla_v_chislax)-1):
   
    if op%2==0:
        result_oper_with_chisla.append(chisla_v_chislax[i]+chisla_v_chislax[i+1])
        op+=1
    elif op%2!=0:   
        result_oper_with_chisla.append(chisla_v_chislax[i]*chisla_v_chislax[i+1]) 
        op+=1
    
print(result_oper_with_chisla)
print("\n\n\n")

result_oper_with_nechet_chisla=0
for i in range(len(chisla_v_chislax)-1):
   if chisla_v_chislax[i]%2==1:
        result_oper_with_nechet_chisla=result_oper_with_nechet_chisla+chisla_v_chislax[i]
    
    
print(result_oper_with_nechet_chisla)
print("\n\n\n")