import random
import timeit

# with open("foo.txt", "w") as outFile:
#     outFile.writelines(["{}\n".format(x) for x in random.sample(range(-10000000, 1000001), 5000000)])

s = """
with open("foo.txt", "r") as file:
    x = file.readlines()
    res = 0
    for i in x:
        if i.strip().isdigit():
            res += int(i.strip())
"""
print(timeit.timeit(s, number=10))
s = """
with open("foo.txt", 'r') as file:
    res = 0
    for line in file:
        if line.strip().isdigit():
            res += int(line.strip())
"""
print(timeit.timeit(s, number=10))
s = """
with open("foo.txt",'r') as file:
    x = (int(line.strip()) for line in file if line.strip().isdigit())
    res = sum(x)
"""
print(timeit.timeit(s, number=10))
