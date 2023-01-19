import os


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


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def _startup_message(self):
        print(STARTUP_MESSAGE)

    def _can_convert(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def _right_coordinate(self, coordinate):
        coordinate = coordinate.strip().split(' ')

        if len(coordinate) != 2:
            print('Invalid coordinate.')
            return False

        if not all([self._can_convert(i) for i in coordinate]):
            print('Invalid coordinate.')
            return False

        check_range = True
        for i in coordinate:
            i = int(i)
            if not (i >= 1 and i <= 3):
                check_range = False

        if not check_range:
            print('Invalid coordinate.')
            return False

        return True

    def _enter_coordinate(self):
        while True:
            coordinate = input('Enter coordinate: ')
            if self._right_coordinate(coordinate):
                coordinate = coordinate.strip().split(' ')
                col, row = [int(i) for i in coordinate]
                return col, row

    def play(self):
        self._startup_message()

        while True:

            while True:
                col, row = self._enter_coordinate()
                marked = self.player1.mark(col, row)
                if marked:
                    break
                else:
                    print("Dude it's already played, try another one.")

            if self.board.winner('X'):
                print('Hello God of tic tac toe')
                break

            # before computer move, because the 9th move made by player1
            if self.board.tie():
                print('Tie')
                break

            self.player2.mark()
            os.system('clear')
            print(self.board.board)

            if self.board.winner('O'):
                print("What's up looser?!")
                break
