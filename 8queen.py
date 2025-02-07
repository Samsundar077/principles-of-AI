def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row):
    if row >= len(board):
        print_board(board)
        return True

    res = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            res = solve_n_queens_util(board, row + 1) or res
            board[row][col] = '.'
    return res

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
    return

n = 8
solve_n_queens(n)
