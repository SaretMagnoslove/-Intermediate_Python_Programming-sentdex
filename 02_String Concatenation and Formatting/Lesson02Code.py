names = ['Londo', 'Sheridan', 'Ivanova', 'Vir']

for name in names:
    # redability
    print('Hello there, ', name)
    # preformance
    print(' '.join(['hello there, ', name]))

print(', '.join(names))

import os
file_location = 'E:\\Courses\\youtube\\-Intermediate_Python_Programming-sentdex'
file_name = 'example.txt'

# # tempting
# print(file_location + '\\' + file_name)
# # right way
# with open(os.path.join(file_location,file_name)) as f:
#     print(f.read())

who = 'Londo'
how_many = 12

# we want Londo bought 12 apples today

# tempting
print(who, 'bought', how_many, 'apples today')
# right way
print('{1} bought {0} apples today!'.format(who, how_many))
