
# Game board
board = ["-" for x in range(9)]

# if game is still going
gameStillGoing = True

# Who won ? or tie ?

winner = None

# Whos turn is it

currentPlayer = "X"
# display game 
def display_board():
    count = 0
    for i in range(len(board)):
        count += 1
        if count == 3:
            print(board[i])
            count = 0
            continue
        print(board[i] + " | ", end="")

def play_game():
    display_board()
    global gameStillGoing
    # while the game is still going
    while gameStillGoing:

        handle_turn(currentPlayer)

        # Flip to the other player
        flip_player()

        # The game has ended
        
        check_if_gameOver()

# handle a single turn of an arbitrary player
def handle_turn(currentPlayer):
    print(currentPlayer + " turn")
    position = input("Choose a position from 1-9 ")

    while position not in [str(x) for x in range(1, 10)]:
        position = input("Choose a position from 1-9 ")

    while board[int(position) - 1] != "-":
        print("Wrong position, Go again!")
        position = input("Choose a position from 1-9 ")
    
    board[int(position) - 1] = currentPlayer
    display_board()


def check_if_gameOver():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    global gameStillGoing
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    if winner == "X" or winner == "O":
            print(winner + " won. ")
            gameStillGoing = False
def check_rows():
    global gameStillGoing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        gameStillGoing = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global gameStillGoing
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        gameStillGoing = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():

    global gameStillGoing
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
   

    if diagonal_1 or diagonal_2 :
        gameStillGoing = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[1]

    return

def check_if_tie():
    global gameStillGoing
    if "-" not in board:
        gameStillGoing = False
        print("Tie.")
        return

def flip_player():

    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

play_game()


#board
#display board
#play game
# handle turn
#check win
    # check rows, columns, diagonals
# check tie
# flip player