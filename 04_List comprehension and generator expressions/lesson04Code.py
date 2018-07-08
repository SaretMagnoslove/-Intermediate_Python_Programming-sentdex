# basic generator in python 3: range
for i in range(5):
    print(5)
# basic list comprehension
xyz = [i for i in range(5)]
# same result as:
xyz = []
for i in range(5):
    xyz.append(i)
# basic generator
xyz = (i for i in range(5))
# xyz is a generator object so you can't just print instead we use:
for i in xyz:
    print(i)