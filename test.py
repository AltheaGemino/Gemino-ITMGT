def tic_tac_toe(board):
    rows = len(board)
    cols = len(board[0])

    # Check rows
    for row in board:
        if all(symbol == row[0] for symbol in row) and row[0] != '':
            return row[0]

    # Check columns
    for col in range(cols):
        if all(board[row][col] == board[0][col] for row in range(rows)) and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if all(board[i][i] == board[0][0] for i in range(rows)) and board[0][0] != '':
        return board[0][0]

    if all(board[i][cols - i - 1] == board[0][cols - 1] for i in range(rows)) and board[0][cols - 1] != '':
        return board[0][cols - 1]

    return "NO WINNER"

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

print(tic_tac_toe(board1))
print(tic_tac_toe(board2))
print(tic_tac_toe(board3))
print(tic_tac_toe(board4))
print(tic_tac_toe(board5))
print(tic_tac_toe(board6))
print(tic_tac_toe(board7))