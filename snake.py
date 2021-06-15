# Reto Damavis
# Fernando Torrado Navarro
import copy


# Class board
class Board:
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.board = [[0 for row in range(self.rows)] for col in range(self.cols)]

    # Get board
    def board_grid(self):
        return self.board

    def __sizeof__(self):
        return self.cols * self.rows

    # Restart board
    def empty_board(self):
        self.board = [[0 for row in range(self.rows)] for col in range(self.cols)]

    def fill_board(self, snake):
        x = 0
        for idx, elem in enumerate(snake):
            try:
                self.board[elem[1]][elem[0]] = idx + 1
            except:
                # if error return true
                return True

    def count_elements_non_zero(self):
        count = 0
        for row in self.board:
            for col in row:
                if col > 0:
                    count += 1
        return count


def constrain_board(board):
    valid = False
    # board.length = 2, 1 ≤ board[i] ≤ 10
    if len(board) != 2 or board[0] < 1 or board[0] > 10 or board[1] < 1 or board[1] > 10:
        valid = True
    return valid


def is_adjacent(snake, board):
    valid = True
    for idx, elem in enumerate(snake):
        if snake[idx][0] >= 0 and snake[idx][1] >= 0 and snake[idx][0] < board.rows and snake[idx][1] < board.cols:
            if idx < len(snake) - 1:
                row = snake[idx][0] - snake[idx + 1][0]
                col = snake[idx][1] - snake[idx + 1][1]
                if abs(row) + abs(col) != 1:
                    valid = False
        else:
            valid = False
    return valid


def constrain_snake(snake, board):
    valid = False
    # 3 ≤ snake.length ≤ 7
    if len(snake) < 3 or len(snake) > 7:
        valid = True
    # snake[i].length = 2
    for idx, elem in enumerate(snake):
        if len(elem) != 2:
            valid = True
    # 0 ≤ snake[i][j] < board[j]
    if board.fill_board(snake):
        valid = True
    if board.count_elements_non_zero() != len(snake):
        valid = True
    if not (is_adjacent(snake, board)):
        valid = True
    return valid


def constrain_depth(depth):
    valid = False
    # 1 ≤ n ≤ 20
    if depth < 1 or depth > 20:
        valid = True
    return valid


def update(snake, board, mv):
    value = copy.copy(snake[0])
    if mv == 'L':
        value[0] -= 1
    if mv == 'R':
        value[0] += 1
    if mv == 'D':
        value[1] += 1
    if mv == 'U':
        value[1] -= 1
    snake.pop()
    snake.insert(0, value)
    board.empty_board()
    board.fill_board(snake)


# Backtracking
def snake_move(result_path, elem_path, snake, board, path_move, n, depth):
    if n == depth:
        if len(elem_path) == depth:
            result_path.append(copy.copy(elem_path))
    else:
        for mv in path_move:
            elem_path.append(mv)
            snake_cp = copy.copy(snake)
            board_cp = copy.copy(board)
            update(snake_cp, board_cp, mv)
            if not (constrain_snake(snake_cp, board_cp)):
                snake_move(result_path, elem_path, snake_cp, board_cp, path_move, n + 1, depth)
            elem_path.pop()


def numberOfAvailableDifferentPaths(board, snake, depth):
    # Counter to available paths
    output = 0
    n = 0
    path_move = ['L', 'R', 'D', 'U']
    result_path = []
    elem_path = []
    # Constrain board
    if constrain_board(board):
        return 'constrain board'

    rows = board[0]
    cols = board[1]
    size_board = board.__sizeof__()
    # Initialize board class
    board = Board(rows, cols)

    # Constrain snake
    if constrain_snake(snake, board):
        return 'constrain snake'

    # Constrain depth
    if constrain_depth(depth):
        return 'constrain'

    snake_move(result_path, elem_path, snake, board, path_move, n, depth)
    output = len(result_path)
    return output % (10 ** 9 + 7)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Declare variables
    board = [4, 3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3

    board = [10, 10]
    snake = [[5, 5], [5, 4], [4, 4], [4, 5]]
    depth = 4

    board = [2, 3]
    snake = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
    depth = 10

    output = numberOfAvailableDifferentPaths(board, snake, depth)

    print(output)
