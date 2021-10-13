l = [1,2,3,4,5,6,7,8,9,10]

# m = []
# for x in l:
#     m.append(x+1)
m = [x+1 for x in l]
print(m)

m = [str(x) for x in l]
print(m)

l = [x for x in range(1, 11)]
print(l)

l = [x for x in range(1, 11) if x<6 if x>3]
print(l)

l = [[1,2,3], [4,5,6], [7,8,9]]
l = [x for y in l for x in y]
print(l)

print([x + y for x in range(10) for y in range(15)])

# for x in range(10):
#     for y in range(15):
#         print(x+y)

d = {"one": 1, "two": 2}
l = [x for x in d.values()]
print(type(l), l)

d = {x:str(x) for x in range(10)}
print(d)

l = [x for x in set("tessdfxjkliwersdfcgjhui78965e4wrasdfghui876dtrcfgvt")]
print(l)