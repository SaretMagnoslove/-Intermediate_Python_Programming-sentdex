import random


class blob:
    def __init__(self, colour):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4, 8)
        self.colour = colour

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_x

        self.x = 0 if self.x < 0 else WIDTH if self.x > WIDTH else self.x
        self.y = 0 if self.y < 0 else HEIGHT if self.y > HEIGHT else self.y
