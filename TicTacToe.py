
#____Global_Variables____
#Gaem Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
# if Game is still going on
game_still_going = True

# Who won? Or Tie?
winner = None

#Who's turn is it
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # Display intial boaard
    display_board()

    while game_still_going :

        # which player turn is it.
        handle_turn( current_player)

        check_if_game_over()

        # if it's tie than flip the player
        flip_player()

# Testing the handle_turn() with an example for now.
def handle_turn(player):
    postion = input("Choose a position from 1-9 : ")
    postion = int(postion) - 1

    board[postion] = "X"
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #check Rows
    #check Columns
    #check Diagonals
    return

def check_if_tie():
    return

def flip_player():
    return



play_game()
