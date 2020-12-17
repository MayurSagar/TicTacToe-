# ____Global_Variables____

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
# if Game is still going on
game_still_going = True

# Who won? Or Tie?
winner = None

# Who's turn is it
current_player = "X"


# display_board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # Display intial boaard
    display_board()

    # while the game still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        # current_player refers to the player whom turn it is right now and so, on the basis of this we will change the
        # turn of player with the help of flip_player.
        # current_player is a argument.
        handle_turn(current_player)

        # check if game is over
        # we have put the check_if_gaem_over() for reason and the reason is after evry move we want see if anybody win
        # and if not then flip the player.
        check_if_game_over()

        # if it's tie than flip to the other player
        flip_player()

    # The game ended ( here i take care of the indentation otherwise you'll gonna print Tie every time you type
    # a for position. so take care.
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


# Testing the handle_turn() with an example for now.
# Handle a single turn of an arbitrary player.
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9 : ")

    # put it in while loop so it ask again and again for valid input and not stop of after 1 or 2 time asking.
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        position = input("Choose a position from 1-9 : ")

    position = int(position) - 1

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # setup global variable
    global winner
    # row_winner, column_winner , diagonal_winner all these are variables and have stored boolean values from
    # check_row() , check_column() , and check_diagonals() all these return boolean values(True,False) and store them
    # in given varibles so, that's why you can put a condition of them like (if,elif)
    # check Rows
    row_winner = check_rows()

    # check Columns
    column_winner = check_column()

    # check Diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # there was no win
        winner = None

    return


def check_rows():
    # set gloabal variables
    global game_still_going

    # Check if rows has all the same values (and is not empty)
    # these are also boolean values so, you can apply condition like (if, elif)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # if any row dose have a match , flag that there is a win
    # whichever is true.
    if row_1 or row_2 or row_3:
        game_still_going = False
        # Return the winner ( X or O ) by checking every row finding which row won.
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    # set gloabal variables
    global game_still_going

    # Check if column has all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # if any column dose have a match , flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
        # Return the winner ( X or O )
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set gloabal variables
    global game_still_going

    # Check if diagonals has all the same values (and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # if any diagonals dose have a match , flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
        # Return the winner ( X or O )
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going

    # if "-" is not in the board then the game_still_going = False (stop)
    # means board is filled by any X or O value but it not filled by "-" so, game stops.and it's a tie.
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global variable we need for use.
    global current_player

    # if current_player was X then change it O
    if current_player == "X":
        current_player = "O"

    # if current_player was O then change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
