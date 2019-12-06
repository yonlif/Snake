from utils import Point


class Snake:
    def __init__(self, init_point: Point):
        self.head = init_point
        body_part = self.head.__copy__()
        body_part.x += 1
        self.body = [self.head, body_part]
        for _ in range(2):
            self.add_part()
        self.direction = 'w'

    def __len__(self):
        return len(self.body)

    def add_part(self):
        self.body.append(self.body[-1].__copy__())

    def snake_step(self):
        new_head = self.head.__copy__()
        if self.direction == 'd':
            new_head.x += 1
        if self.direction == 'w':
            new_head.y -= 1
        if self.direction == 'a':
            new_head.x -= 1
        if self.direction == 's':
            new_head.y += 1
        self.body.insert(0, new_head)
        self.body.pop()
        self.head = new_head

    def set_direction(self, direction):
        dir_dict = {'w': 's', 'a': 'd', 'd': 'a', 's': 'w'}
        if not dir_dict[self.direction] == direction:
            self.direction = direction
