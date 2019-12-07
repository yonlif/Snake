import random
from snake import Snake
from utils import Point
from copy import deepcopy


class GameModel:
    def __init__(self, board_size=50, init_position=Point(25, 25)):
        self.board_size = board_size
        self.run = False
        self.score = 0
        self.apple = None

        self._apple_score = 50
        self._snake = Snake(init_position)
        self._replace_apple()
        # self.lastApple = self.apple

    def start(self):
        self.run = True

    def set_direction(self, direction):
        self._snake.set_direction(direction)

    def get_snake_copy(self):
        return deepcopy(self._snake)

    def game_tick(self):
        if self._is_game_over():
            return
        self._apple_logic()
        self._snake.snake_step()

    def _is_game_over(self):
        if len(self._snake) == self.board_size ** 2:
            self.run = False
            return True
        if not 0 <= self._snake.head.x < self.board_size or not 0 <= self._snake.head.y < self.board_size:
            self.run = False
            return True
        for item in self._snake.body:
            if self._snake.head == item and self._snake.head is not item:
                self.run = False
                return True
        return False

    lastApple = None
    def _apple_logic(self):
        if self._snake.head == self.apple:

            self.lastApple = self.apple

            self._replace_apple()
            self._snake.add_part()
            self.score += self._apple_score

    def _replace_apple(self):
        while True:
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            try_point = Point(x, y)
            if try_point not in self._snake.body:
                self.apple = try_point
                break

    def __str__(self):
        ret = ""
        ret += "+" + "-" * self.board_size + "+" + "\n"
        for x in range(self.board_size):
            ret += '|'
            for y in range(self.board_size):
                if Point(x, y) == self._snake.head:
                    ret += 'h'
                elif Point(x, y) in self._snake.body:
                    ret += 's'
                elif Point(x, y) == self.apple:
                    ret += 'a'
                else:
                    ret += ' '
            ret += '|\n'
        ret += "+" + "-" * self.board_size + "+" + "\t"
        ret += f"Score: {self.score}"
        return ret


if __name__ == '__main__':
    g = GameModel()
    print(g)
