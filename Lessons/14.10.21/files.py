
# x = open("test.txt", "w")
# x.write("new content")
# x.close()

# with open("test.txt", "w", newline='\n') as x:
#     x.write("test\n")
#     x.writelines(["line1\n", "line2\n", "line3\n"])

# with open("test.txt", "r") as x:
#     for l in x:
#         print(l)

    # print(x.read())
    # print(x.read(3))

    # while True:
    #     s = x.readline()
    #     print(s)
    #     if s == "":
    #         break

# print(x)
# x.write("test")

# with open("test.txt", "a") as x:
#     x.write("appended content")

with open("test.txt", "w+") as x:
    x.write("test")
    x.seek(0)
    print(x.read())

with open("new", "w") as x:
    x.write("new")