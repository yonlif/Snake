import pygame
from time import sleep

from game_model import GameModel
from view import GameView


class BaseController:
    def __init__(self, game_model: GameModel, view: GameView, delay: float=0.1):
        self.game_model = game_model
        self.view = view
        self.delay = delay

    def play(self):
        self.game_model.start()
        while self.game_model.run:

            self.controller_step()

            self.game_model.game_tick()
            self.view.draw_game(self.game_model)
            sleep(self.delay)

    def controller_step(self):
        raise NotImplementedError


class BasicController(BaseController):
    options = ['s', 'd', 'w', 'a']
    i = 0

    def controller_step(self):
        c = self.options[self.i // 2]
        i = (self.i + 1) % 8
        self.game_model.set_direction(c)


class UserController(BaseController):
    def controller_step(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.game_model.set_direction('a')
                if event.key == pygame.K_s:
                    self.game_model.set_direction('s')
                if event.key == pygame.K_d:
                    self.game_model.set_direction('d')
                if event.key == pygame.K_w:
                    self.game_model.set_direction('w')
            if event.type == pygame.locals.QUIT:
                pygame.quit()
