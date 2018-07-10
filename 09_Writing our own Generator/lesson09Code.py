# the lazy way of building a generator
(i for i in range(5))


# simple generator
def simple_gen():
    yield 'oh'
    yield 'hello'
    yield 'there'


[print(i) for i in simple_gen()]
# crack 3 numbers password
CORRECT_PASS = (3, 1, 4)
# using for loop
found_pass = False
for c1 in range(10):
    if found_pass:
        break
    for c2 in range(10):
        if found_pass:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_PASS:
                print('found the pass: {}'.format((c1, c2, c3)))
                found_pass = True
                break
            print(c1,c2,c3)
# same using a generator
def pass_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1,c2,c3)

for i in pass_gen():
    if (c1, c2, c3) == CORRECT_PASS:
        print('found the pass: {}'.format((c1, c2, c3)))
        break

