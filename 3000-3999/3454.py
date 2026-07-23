board = input()

if board.count('X') != 2 or board.count('O') != 1:
    print('?')
elif board[0] == 'X' and board[1] == 'X' or board[1] == 'X' and board[2] == 'X':
    print('Alice')
else:
    print('*')
