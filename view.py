import pygame, sys
from pygame.locals import *

from game_model import GameModel

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class GameView:
    def __init__(self, board_size, scale=10):
        self.scale = scale
        self.screen = pygame.display.set_mode([board_size * scale, board_size * scale])
        self.screen.fill(WHITE)
        self.board_size = board_size

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def draw_game(self, game: GameModel):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, RED,
                         (game.apple.x * self.scale, game.apple.y * self.scale, self.scale, self.scale))
        for item in game._snake.body:
            pygame.draw.rect(self.screen, BLUE,
                             (item.x * self.scale, item.y * self.scale, self.scale, self.scale))
        pygame.display.set_caption(f'Score: {game.score}')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
