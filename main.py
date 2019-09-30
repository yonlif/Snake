from time import sleep


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        return other.x == self.x and other.y == self.y


class Game:
    def __init__(self, board_size=50, init_position=Point(25, 25)):
        self.board_size = board_size
        self.run = False
        self.score = 0
        self.apple_score = 50

        self.snake = [init_position]
        self.snake_direction = 'w'

        self.apples = None

    def start(self):
        self.run = True
        while self.run:
            sleep(0.2)
            self.game_tick()

    def game_tick(self):
        if self.snake[0] == self.apples:
            self.generate_apple()
            self.score += self.apple_score
        if not 0 <= self.snake[0].x < self.board_size or not 0 <= self.snake[0].y < self.board_size:
            self.run = False
            return None
        self.snake_step()

    def snake_step(self):
        if self.snake_direction == 'w':
            self.snake.insert(0, Point(self.snake[0].x, self.snake[0].y + 1))
        if self.snake_direction == 'a':
            self.snake.insert(0, Point(self.snake[0].x - 1, self.snake[0].y))
        if self.snake_direction == 's':
            self.snake.insert(0, Point(self.snake[0].x, self.snake[0].y - 1))
        if self.snake_direction == 'd':
            self.snake.insert(0, Point(self.snake[0].x + 1, self.snake[0].y))
        self.snake.pop()

    def generate_apple(self):
        pass

    def __str__(self):
        ret = ""
        ret += "+" + "-" * self.board_size + "+" + "\n"
        for x in range(self.board_size):
            ret += '|'
            for y in range(self.board_size):
                if Point(x, y) in self.snake:
                    ret += 's'
                elif Point(x, y) == self.apples:
                    ret += 'a'
                else:
                    ret += ' '
            ret += '|\n'
        ret += "+" + "-" * self.board_size + "+" + "\t"
        ret += f"Score: {self.score}"
        return ret


if __name__ == '__main__':
    g = Game()
    print(g)
