# Define the Sudoku solver
def solve_sudoku(board):
    # Find an empty cell (denoted by 0)
    empty_cell = find_empty(board)
    if not empty_cell:
        # If there's no empty cell, the puzzle is solved
        return True
    else:
        row, col = empty_cell

    # Try numbers 1 through 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            # If the number is valid, place it in the cell
            board[row][col] = num

            # Recursively attempt to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If it leads to an invalid state, reset the cell
            board[row][col] = 0

    return False

# Check if placing num in board[row][col] is valid
def is_valid(board, num, row, col):
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Find an empty cell in the Sudoku grid (denoted by 0)
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

# Print the Sudoku grid
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(f" {board[i][j]} ", end="")
        print()

# Sample Sudoku puzzle (0 denotes empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the puzzle and print the solution
print("Unsolved Sudoku:")
print_board(sudoku_grid)
if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku:")
    print_board(sudoku_grid)
else:
    print("No solution exists.")
