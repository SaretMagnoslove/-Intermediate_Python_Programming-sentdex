import random


class Blob:
    def __init__(self,
                 color,
                 x_boundry,
                 y_boundry,
                 size_range=(4, 8),
                 movment_range=(-1, 2)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundry = x_boundry
        self.y_boundry = y_boundry
        self.x = random.randrange(0, x_boundry)
        self.y = random.randrange(0, y_boundry)
        self.movment_range = movment_range

    def move(self):
        self.move_x = random.randrange(self.movment_range[0], self.movment_range[1])
        self.move_y = random.randrange(self.movment_range[0], self.movment_range[1])
        self.x += self.move_x
        self.y += self.move_y
