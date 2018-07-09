# with time module you can just do
import time
start = time.time()
print(time.time() - start)

input_list = range(100)


def div_by_five(num):
    return True if num % 5 == 0 else False


ge = (i for i in input_list if div_by_five(i))

lc = [i for i in input_list if div_by_five(i)]

import timeit
print(timeit.timeit('1+3', number=50000000))

# time for creating a generator
print(
    timeit.timeit(
        """input_list = range(100)


def div_by_five(num):
    return True if num % 5 == 0 else False


ge = (i for i in input_list if div_by_five(i)) """,
        number=5000))

print(
    timeit.timeit(
        """input_list = range(100)


def div_by_five(num):
    return True if num % 5 == 0 else False


ge = [ i for i in input_list if div_by_five(i) ] """,
        number=5000))


print(
    timeit.timeit(
        """input_list = range(100)


def div_by_five(num):
    return True if num % 5 == 0 else False


ge = (i for i in input_list if div_by_five(i))
for i in ge:
    x = i """,
        number=5000))

print(
    timeit.timeit(
        """input_list = range(100)


def div_by_five(num):
    return True if num % 5 == 0 else False


ge = [ i for i in input_list if div_by_five(i) ]
for i in ge:
    x = i """,
        number=5000))