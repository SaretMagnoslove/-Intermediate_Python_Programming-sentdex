names = ['Londo', 'Sheridan', 'Ivanova', 'Vir']

# for name in names:
#     # redability
#     print('Hello there, ', name)
#     # preformance
#     print(' '.join(['hello there, ', name]))
#
# print(', '.join(names))

import os
file_location = r"E:\Courses\youtube\-Intermediate_Python_Programming-sentdex"
file_name = 'example.txt'

# tempting
test = (file_location + r"\\" + file_name)
# right way
with open(test) as f:
    print(f.read())