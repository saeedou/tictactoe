from game_component import Board, Player, Computer

BOARD12X = '''
    1   2   3
  +---+---+---+
1 |   |   |   |
  +---+---+---+
2 | X |   |   |
  +---+---+---+
3 |   |   |   |
  +---+---+---+
'''
computer_move = '''
    1   2   3
  +---+---+---+
1 |   | O | X |
  +---+---+---+
2 |   | O |   |
  +---+---+---+
3 | X |   |   |
  +---+---+---+
'''


def test_board():
    board = Board()
    board.mark(1, 2, 'X')
    assert board.board == BOARD12X
    assert board.mark(1, 2, 'X') == -1
    assert board.winner('X') is False
    board.mark(1, 1, 'X')
    board.mark(1, 3, 'X')
    # return the winner
    assert board.winner('X') is True
    board.mark(3, 1, 'O')
    board.mark(3, 2, 'O')
    assert board.winner('O') is False
    board.mark(3, 3, 'O')
    assert board.winner('O') is True


# doesn't check for winner, if all the board played it means tie
def test_tie():
    board = Board()
    board.tie() is False

    for i in range(1, 4):
        for j in range(1, 4):
            board.mark(i, j, 'X')
    board.tie() is True


def test_player():
    board = Board()
    player = Player(board)
    player.mark(1, 2)
    assert board.board == BOARD12X


def test_computer():
    board = Board()
    computer = Computer(board)
    board.mark(1, 3, 'X')
    board.mark(2, 2, 'O')
    board.mark(3, 1, 'X')
    computer.mark()
    assert board.board == computer_move
