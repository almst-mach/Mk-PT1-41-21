x = []
p = {}
res = []

def greedy():
    global x,p,res
    h=True
    dic_1 = {}  
    dic_2 = {}  
    for k, v in p.items():
        if v > x[2]:
            dic_1[k] = v - x[2]
        elif v < x[2]:
            dic_2[k] = x[2] - v
    if dic_1 == {}:
        res = ['Никто никому не должен']
        return res
    counter_1 = 0
    for k, v in dic_1.items():
        counter_1 += 1
        counter_2 = 0
        while h:  
            for k1, v1 in dic_2.items():
                counter_2 += 1
                if v1 == 0:
                    continue
                if v >= v1:  
                    v = v - v1 
                    res.append(f'{k1} должен {k} - {v1}')
                    h=False 
                elif v < v1:
                    v1 = v1 - v
                    dic_2[k1] = v1 
                    res.append(f'{k1} должен {k} - {v}')
                    h=False
                    break

try:
    a = int(input('Введите сумму счета: \n'))
    x.append(a)
    a = int(input('Введите количество участников: \n'))
    x.append(a)
    s_m =  x[0] / x[1]
    x.append(s_m)
    s = 0
    for i in range(0,a):
        k = 1 + i
        v=int(input(f"сумму закинул в банк {k} человек:"))
        p[k]=v
        s += v
    if s != x[0]:
        raise RuntimeError("сумма чека не совпадает с суммами персон")
except RuntimeError as error:
    print(error)
    
greedy()
print(res)