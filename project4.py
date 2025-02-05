def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "

        print(row_str)
        if i != len(board) - 1:
            print("-----------")


def get_move(turn, board):
    while True:
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))

        if row < 1 or row > len(board):
            print("Invalid row , try again!")
        elif col < 1 or col > len(board):
            print("Invalid col , try again")
        elif board[row - 1][col - 1] != " ":
            print("Already taken , try again!")
        else:
            break
    board[row - 1][col - 1] = turn
    
# TODO: Add AI


def check_win(board, turn):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
    ]
    
    for line in lines:
        win = True
        for pos in line:
            row,col = pos
            if board[row][col] != turn:
                win = False
                break
        if win:
            return True
    return False


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = "X"
turn_count = 0
print_board(board)

while turn_count < 9:
    print()
    print("It is " + turn + "'s turn!")
    get_move(turn, board)
    print_board(board)
    winner = check_win(board, turn)
    if winner:
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_count += 1

if turn_count == 9:
    print("It is a Tie!")
else:
    print("The winner is " + turn + "!")
