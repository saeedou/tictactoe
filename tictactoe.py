from easycli import Root

from tictactoe_core.main_game import Game as BaseGame
from tictactoe_core.game_component import Board, Player, Computer


board = Board()
player1 = Player(board)
player2 = Computer(board)
base_game = BaseGame(board, player1, player2)


class Game(Root):
    __help__ = 'tictactoe cli game'
    __command__ = 'tictactoe'

    def __call__(self, args):
        base_game.play()
