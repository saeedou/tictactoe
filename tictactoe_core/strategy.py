class Strategy:
    def __init__(self, board):
        self.board = board

    def block_or_win(self):
        board_segment = []
        win_index_patterns = ['012', '345', '678', '036', '147', '258', '048',
                              '246']

        def segment_block_or_win(array):
            space_number = array.count(' ')
            x_number = array.count('X')
            o_number = array.count('O')
            if (o_number == 2 or x_number == 2) and space_number == 1:
                # TODO: returns bull shit
                return array.index(' ')

            return None

        for row in win_index_patterns:
            for i in row:
                board_segment.append(self.board[int(i)])

            index = segment_block_or_win(board_segment)
            if index is not None:
                return int(row[index])
            else:
                board_segment = []

        return None

    def two_way_play(self):
        counter = 0

        def compare_to_row(row, board):
            wing1 = {board[int(i)] for i in row[0]}
            wing2 = {board[int(i)] for i in row[1]}
            if len(wing1) == 2:
                return wing1 == wing2
            return False

        corner_wings_indexs = {
            '0': ['12', '36'],
            '2': ['01', '58'],
            '6': ['03', '78'],
            '8': ['67', '25']
        }

        corner_key = None
        for k, v in corner_wings_indexs.items():
            if self.board[int(k)] == ' ' and compare_to_row(v, self.board):
                counter += 1
                corner_key = int(k)

        if counter == 1:
            return corner_key

        return None

    def play_any(self):
        for i in range(9):
            if self.board[i] == ' ':
                return i

        return None

    def first_move(self):
        if self.board.count(' ') == 9 or self.board[4] == ' ':
            return 4
        elif self.board.count(' ') == 8:
            return 0
        else:
            return None

    def play_side(self):
        side_indexes = '1357'
        for i in side_indexes:
            if self.board[int(i)] == ' ':
                return int(i)

        return None
