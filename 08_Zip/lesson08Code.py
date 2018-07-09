# creatinng the input
x = [1, 2, 3, 4]
y = [6, 5, 4, 3]
z = ['x', 'y', 'z', 'w']
# combining and iterating over 3 lists
for a, b, c in zip(x, y, z):
    print(a, b, c)
# or with tuples
for i in zip(x, y, z):
    print(i)
# converting into a list of tuples
print(list(zip(x, y, z)))
# converting into a dictionary
print(dict(zip(x, y)))
# combining with list comprehension
[print(a, b, c) for a, b, c in zip(x, y, z)]
# Remember!!! in list comprehension the values are temp so you can do
[print(x, y) for x, y in zip(x, y)]
print(x)
# but the same with loop is going to change the value of x!
for x, y in zip(x, y):
    print(x, y)
print(x)
