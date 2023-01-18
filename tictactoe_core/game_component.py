from strategy import Strategy


class Board:
    def __init__(self):
        self.maptoboard = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '
        ]

    @property
    def board(self):
        return f'''
    1   2   3
  +---+---+---+
1 | {self.maptoboard[0]} | {self.maptoboard[1]} | {self.maptoboard[2]} |
  +---+---+---+
2 | {self.maptoboard[3]} | {self.maptoboard[4]} | {self.maptoboard[5]} |
  +---+---+---+
3 | {self.maptoboard[6]} | {self.maptoboard[7]} | {self.maptoboard[8]} |
  +---+---+---+
'''

    def mark(self, col, row, sign):
        index = (row - 1) * 3 + col - 1

        if self.maptoboard[index] == ' ':
            self.maptoboard[index] = sign
            return True
        else:
            return False

    def winner(self, sign):
        win_index_patterns = ['012', '345', '678', '036', '147', '258', '048',
                              '246']
        for pattern in win_index_patterns:
                for i in pattern:
                    is_winner = True
                    if self.maptoboard[int(i)] != sign:
                        is_winner = False
                        break
                if is_winner:
                    return is_winner

        return False


    def tie(self):
        if self.maptoboard.count(' ') == 0:
            return True
        return False


class Player:
    def __init__(self, board: Board):
        self.board = board

    def mark(self, col, row):
        return self.board.mark(col, row, 'X')


class Computer:
    def __init__(self, board):
        self.board = board

    def mark(self):
        strategy = Strategy(self.board.maptoboard)
        # The strategy with lower index is has higher priority
        strategies = [
            strategy.first_move(),
            strategy.block_or_win(),
            strategy.two_way_play(),
            strategy.play_side(),
            strategy.play_any()
        ]

        for i in strategies:
            if i is not None:
                index = i
                break

        row = int(index / 3) + 1
        col = (index % 3) + 1
        self.board.mark(col, row, 'O')
        print(self.board.board)
