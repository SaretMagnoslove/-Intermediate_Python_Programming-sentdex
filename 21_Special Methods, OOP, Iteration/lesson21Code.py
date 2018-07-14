def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1

# testing
for i in range_gen(5):
    print(i)

x = range_gen(5)
x.__next__()

[print(i) for i in x]