#  **********Global Variable**************

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_still_going = True

# who won? or tie?
winner = None

# whose turn is it
current_player = "X"


#  Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tac toe
def play_game():

    # display initial board
    display_board()


# while the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

# Check if the game is ended
        check_if_game_over()


#  flip to the other player
        flip_player()

# The game had ended
    if winner == "X" or winner == "O":
        print("Player " + winner + " Won.🎉")
    elif winner == None:
        print("Game is Tie 🏴")


#  Handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn")

    position = input("Choose a postion from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("\n👎Invalid Input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Select another")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    #  Set up global variable
    global winner

    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():

    #  set up global variable
    global game_still_going

#  Check if any o the rows have all the same value not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

# If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    #  Return the winner (X and O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():

    #  set up global variable
    global game_still_going

#  Check if any o the rows have all the same value not empty

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

# If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    #  Return the winner (X and O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():

    # set up global variable
    global game_still_going

#  Check if any o the rows have all the same value not empty

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    #  Return the winner (X and O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return


def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():

    # global variables we need
    global current_player

# if the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
# If the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
