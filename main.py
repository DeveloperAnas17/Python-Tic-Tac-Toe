# ---------GLOBAL VARIABLES -------------

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# If game is still going
game_still_going = True

# Who won? Or tie?

winner = None

# Whose turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[4] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display initial board
    display_board()

    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won. 🎉")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    position = input("Choose a postion from 1-9: ")
    position = int(position) - 1

    board[position] = "X"
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # Get the winner
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

    # set up global variable
    global game_still_going

    # check if the rows have all the same value but not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that ther is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set up global variable
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

 # If any column does have a match, flag that ther is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

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

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

 # If any column does have a match, flag that ther is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_if_tie():
    # set up global variable
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

 # If any diagonal does have a match, flag that ther is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

    return


def flip_player():
    return


play_game()
