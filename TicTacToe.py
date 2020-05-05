# ______GLOBAL______________
# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",
         ]

# If game is still going
game_is_on = True

# who won or tie?
winner = None

# whos turn
current = 'X'


def display_board():
    print("-------")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-------")


def play_game():
    # display the board
    display_board()

    while game_is_on:
        # handle the game
        handle_turn(current)
        # checking if game done?

        check_if_done()
        # FLip from X and O or vice versa
        flip_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " WON!")
    elif winner == None:
        print("TIE")


# Handle the turns
def handle_turn(player):
    print(player + "'s turn")

    position = input(" Please Enter which position you want to play?(1-9)")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Please Enter again: ")

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("you cant go again")
    board[position] = player

    display_board()


def check_if_done():
    check_if_win()
    check_if_tie()
    return


def check_if_win():
    global winner

    row = rows()
    column = columns()
    diagonals = diagonal()

    if row:
        winner = row
    elif column:
        winner = column
    elif diagonals:
        winner = diagonals
    else:
        winner = None


def rows():
    global game_is_on

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_is_on = False

    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]


def columns():
    global game_is_on
    coloumn1 = board[0] == board[3] == board[6] != '-'
    coloumn2 = board[1] == board[4] == board[7] != '-'
    coloumn3 = board[2] == board[5] == board[8] != '-'

    if coloumn1 or coloumn2 or coloumn3:
        game_is_on = False
    if coloumn1:
        return board[0]
    if coloumn2:
        return board[1]
    if coloumn3:
        return board[2]
    return


def diagonal():
    global game_is_on
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        game_is_on = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return


def check_if_tie():
    global game_is_on

    if "-" not in board:
        game_is_on = False
    return


def flip_player():
    global current

    if current == 'X':
        current = 'O'
    elif current == 'O':
        current = 'X'

    return



play_game()
