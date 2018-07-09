# without enumerate
example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

# same with enumerate
for i, j in enumerate(example):
    print(i, j)

# creating a dictionary with enumerate
new_dict = dict(enumerate(example))
print(new_dict)
# enumerate with dict and list comprehension
[print(i, j) for i, j in enumerate(new_dict.values())]
