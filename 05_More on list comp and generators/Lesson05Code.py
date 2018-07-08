# divisible by 5 using generator:
input_list = [i for i in range(30)]


def div_by_five(num):
    return True if num % 5 == 0 else False


xyz = (i for i in input_list if div_by_five(i))

[print(i) for i in xyz]
# same with list comprehension:
xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
[print(i) for i in xyz]

for i in range(5):
    for ii in range(5):
        print(i, ii)

# is identical to:
[[print(i, ii) for ii in range(5)] for i in range(5)]
# or you can do
xyz = [[(i, ii) for ii in range(5)] for i in range(5)]
# or
zxy = [[[i, ii] for ii in range(5)] for i in range(5)]
print(xyz)
print(zxy)
# same with generator
g = (((i, ii) for ii in range(5)) for i in range(5))
for i in g:
    for ii in i:
        print(ii)

# printing in a generator
xyz = (print(i) for i in range(5))
for i in xyz:
    i
