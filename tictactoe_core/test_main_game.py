from unittest import mock

from main_game import Game
from game_component import Board, Player, Computer


STARTUP_MESSAGE = '''To play enter square coordinates(column, row)
    Example: 1 1
    This will mark the first column on the first row.

    1   2   3
  +---+---+---+
1 |   |   |   |
  +---+---+---+
2 |   |   |   |
  +---+---+---+
3 |   |   |   |
  +---+---+---+
'''

EMPTY_BOARD = '''
    1   2   3
  +---+---+---+
1 |   |   |   |
  +---+---+---+
2 |   |   |   |
  +---+---+---+
3 |   |   |   |
  +---+---+---+
'''

N = '\n'

WINNING_MESSAGE = 'Hello God of tic tac toe'
LOSING_MESSAGE = "What's up looser?!"
TIE_MESSAGE = 'Tie'
PLAY_AGAIN_MESSAGE = "Dude it's already played, try another one."


# Q: how to test 'while True' with condition that doesn't break it?
# Q: is it good practice to test private method to avoid testing 'while True'?
def test__right_coordinate(capsys):
    board = Board()
    player1 = Player(board)
    player2 = Computer(board)
    game = Game(board, player1, player2)
    scenarios = ('1 2 3', 'x y', '1 x', '1', '2 5')
    for i in scenarios:
        assert game._right_coordinate(i) is False
        out, err = capsys.readouterr()
        assert out == 'Invalid coordinate.\n'

    assert game._right_coordinate('1 2') is True


def test_play(capsys):
    board = mock.Mock()
    player1 = mock.Mock()
    player2 = mock.Mock()
    game = Game(board, player1, player2)

    with mock.patch('builtins.input') as m:
        m.return_value = '1 1'
        player1.mark.return_value = True
        board.winner.return_value = True
        game.play()
        out, err = capsys.readouterr()
        assert out == STARTUP_MESSAGE + N + WINNING_MESSAGE + N

    with mock.patch('builtins.input') as m:
        m.return_value = '1 1'
        player1.mark.return_value = True
        board.winner.return_value = False
        board.tie.return_value = True
        game.play()
        out, err = capsys.readouterr()
        assert out == STARTUP_MESSAGE + N + TIE_MESSAGE + N

    with mock.patch('builtins.input') as m:
        m.return_value = '1 1'
        player1.mark.return_value = True
        board.winner.side_effect = [False, True]
        board.tie.return_value = False
        board.board = EMPTY_BOARD
        game.play()
        out, err = capsys.readouterr()
        assert err == ''
        assert out == (
            STARTUP_MESSAGE + N
            + EMPTY_BOARD + N
            + LOSING_MESSAGE + N
        )

    board = mock.Mock()
    game = Game(board, player1, player2)

    with mock.patch('builtins.input') as m:
        m.side_effect = ['1 1', '1 2']
        player1.mark.side_effect = [False, True]
        board.winner.return_value = True
        game.play()
        out, err = capsys.readouterr()
        assert out == (
            STARTUP_MESSAGE + N
            + PLAY_AGAIN_MESSAGE + N
            + WINNING_MESSAGE + N
        )
