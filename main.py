from controller import BasicController, UserController
from ai_controller import AIController
from game_model import GameModel
from view import GameView

if __name__ == '__main__':
    model = GameModel(board_size=30)
    view = GameView(model.board_size)
    controller = UserController(model, view)
    # controller = AIController(model, view)
    controller.play()
