from strategy import Strategy


def test_block_or_win():
    """If you or your opponent can win in one move, return the index to win or
    block him."""

    board = [
        ' ', ' ', ' ',
        ' ', ' ', 'X',
        ' ', 'X', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.block_or_win() is None
    board[3] = 'X'
    assert strategy.block_or_win() == 4
    board = [
        ' ', ' ', ' ',
        ' ', 'O', 'X',
        'O', ' ', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.block_or_win() == 2


def test_two_way_play():
    """If playing corner will make two way to win return its index."""
    board = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.two_way_play() is None
    board[1] = 'X'
    board[3] = 'X'
    assert strategy.two_way_play() == 0
    board[1] = ' '
    board[3] = ' '
    board[2] = 'X'
    board[6] = 'X'
    assert strategy.two_way_play() is None


def test_play_any():
    """Play first square that is empty so the game do not crash."""

    board = [
        'X', 'X', 'X',
        ' ', 'X', ' ',
        ' ', ' ', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.play_any() == 3
    board = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    strategy = Strategy(board)
    assert strategy.play_any() is None


def test_first_move():
    """Where to play the first move."""

    board = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.first_move() == 4
    board[3] = 'X'
    assert strategy.first_move() == 4
    board[3] = ' '
    board[4] = 'X'
    assert strategy.first_move() == 0
    board[2] = 'X'
    assert strategy.first_move() is None


def test_play_side():
    """Play side with lowest index."""

    board = [
        ' ', ' ', 'X',
        ' ', 'O', ' ',
        'X', ' ', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.play_side() == 1
    board = [
        ' ', 'X', ' ',
        'X', ' ', 'X',
        ' ', 'X', ' ',
    ]
    strategy = Strategy(board)
    assert strategy.play_side() is None
