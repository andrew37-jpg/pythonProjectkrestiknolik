class TicTacToeBoard:
    def __init__(self):
        self._field = [[None for _ in range(3)] for _ in range(3)]
        self._current_player = 'X'
        self._winner = None
        self._moves_left = 9

    def new_game(self):
        self._field = [[None for _ in range(3)] for _ in range(3)]
        self._current_player = 'X'
        self._winner = None
        self._moves_left = 9

    def get_field(self):
        return self._field

    def check_field(self):
        # Проверка строк
        for i in range(3):
            if self._field[i][0] == self._field[i][1] == self._field[i][2]:
                if self._field[i][0] is not None:
                    self._winner = self._field[i][0]

        # Проверка столбцов
        for j in range(3):
            if self._field[0][j] == self._field[1][j] == self._field[2][j]:
                if self._field[0][j] is not None:
                    self._winner = self._field[0][j]

        # Проверка диагоналей
        if self._field[0][0] == self._field[1][1] == self._field[2][2]:
            if self._field[0][0] is not None:
                self._winner = self._field[0][0]
        if self._field[0][2] == self._field[1][1] == self._field[2][0]:
            if self._field[0][2] is not None:
                self._winner = self._field[0][2]

        if self._winner is not None:
            return self._winner
        elif self._moves_left == 0:
            return 'D'
        else:
            return None

    def make_move(self, row, col):
        if self._winner is not None:
            return 'Игра уже завершена'
        if self._field[row - 1][col - 1] is not None:
            self._field[row - 1][col - 1] = self._current_player
            self._moves_left -= 1
            winner = self.check_field()
            if winner is not None:
                if winner == 'X':
                    return 'Победил игрок X'
                elif winner == '0':
                    return 'Победил игрок 0'
                else:
                    return 'Ничья'
            else:
                if self._current_player == 'X':
                    self._current_player = '0'
                return 'Продолжаем играть'