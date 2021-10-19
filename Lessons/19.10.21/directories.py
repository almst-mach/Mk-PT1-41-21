import os

print(os.name)

print(os.sep)

print(f"test{os.sep}test")

x = os.path.join("test", "tst", "test")

print(os.getcwd())

os.makedirs(x)

# os.chdir(x)

# print(os.getcwd())

# print(os.listdir())

print(list(os.walk(os.getcwd())))

# os.remove()

os.removedirs(x)
# os.rmdir(x)