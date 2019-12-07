from controller import BaseController


class AIController(BaseController):
    i = 0
    def dumbAsShit(self):
        if self.i == 0:
            if self.game_model.get_snake_copy().head.y == 0:
                self.game_model.set_direction("d")
            if self.game_model.get_snake_copy().direction == "d" and self.game_model.get_snake_copy().head.x == self.game_model.board_size - 1:
                self.game_model.set_direction("s")
            elif self.game_model.get_snake_copy().direction == "s" and self.game_model.get_snake_copy().head.y % 2 == 1:
                self.game_model.set_direction("a")
            elif self.game_model.get_snake_copy().direction == "a" and self.game_model.get_snake_copy().head.x == 1 and self.game_model.get_snake_copy().head.y != self.game_model.board_size - 1:
                self.game_model.set_direction("s")
            elif self.game_model.get_snake_copy().direction == "s" and self.game_model.get_snake_copy().head.y % 2 == 0:
                self.game_model.set_direction("d")
                # print(self.game_model.get_snake_copy().direction)

        if self.game_model.get_snake_copy().head.y == self.game_model.board_size - 1 and self.game_model.get_snake_copy().head.x == 0:
            self.i = 1
            self.game_model.set_direction("w")
        elif self.game_model.get_snake_copy().head.y == 0 and self.i == 1:
            self.game_model.set_direction("d")
            self.i = 0


    gotThere = False
    def leftCorner2Apple(self):
        if self.gotThere == False:
            if self.game_model.get_snake_copy().direction == "w":
                self.game_model.set_direction("a")
            elif self.game_model.get_snake_copy().direction == "s":
                self.game_model.set_direction("a")
        if self.game_model.get_snake_copy().head.x == 0 and self.gotThere == False:
            self.game_model.set_direction("w")

        if self.game_model.get_snake_copy().head.y == 0 and self.game_model.get_snake_copy().head.x == 0:
            self.game_model.set_direction("d")
            self.gotThere = True

        if self.game_model.get_snake_copy().head.x == self.game_model.apple.x and self.gotThere:
            self.game_model.set_direction("s")
            if self.game_model.apple == self.game_model.get_snake_copy().head:
                self.gotThere = False
                self.game_model.set_direction("a")

    def controller_step(self):
        # self.dumbAsShit()
        self.leftCorner2Apple()
        pass




# (0, 0)     (29, 0)
# (0, 29)    (29, 29)
