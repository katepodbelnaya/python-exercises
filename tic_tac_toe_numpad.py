from IPython.display import clear_output
import random

num_pad = [7,8,9,4,5,6,1,2,3]

def display_board(board):
    clear_output()
    row = 1
    cell = 7
    while row <= 3:
        print (" --- --- --- ")
        print ("| {} | {} | {} | ".format(board[cell],board[cell+1],board[cell+2]))
        row+=1
        cell-=3
    print (" --- --- --- ")
    
def player_input():
    mark = ""
    while mark != "X" and mark != "x" and mark != "O":
        mark = input("Player 1: Do you want to be X or O? ")
    return mark.upper()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    flag = False
    if mark*3 in "".join(board):
        flag = True
    elif board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:
        flag = True
    else:
        for i in range(1,4):
            if board[i]==board[i+3]==board[i+6]==mark:
                flag = True
    return flag

def choose_first():
    return random.randint(1,2)
    
def space_check(board, position):
    return board[position] != "X" and board[position] != "O"

def full_board_check(board):
    flag = True
    for item in board:
        if item != "X" and item != "O" and item != "#":
            flag = False
            break
    return flag

def player_choice(board):
    flag = True
    while flag:
        position = int(input ("Choose your next position: (1-9): "))
        if space_check(board, position) == False:
            print ("This space on the board is not available! Try again!")
        else:
            flag = False
    return position

def replay():
    answer = input("Do you want to play again? Yes or No: ")
    if answer.lower() == "yes":
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')
marks = [1,2]
while True:
    # Set the game up here
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    mark1 = player_input()
    if mark1 == "X":
        marks [0] = "X"
        marks [1] = "O"
    else: 
        marks [1] = "X"
        marks [0] = "O"
    first = choose_first()
    print ("Player {} go first.".format(first))
    if first
    game_on = True
    while game_on:
        #Player 1/2 Turns
        for i in range(2):
            position = int(player_choice(board))
            place_marker(board, marks[i], position)
            display_board(board)
            if win_check(board, marks[i]):
                print("Your won!")
                game_on=False
                break
            elif full_board_check(board):
                game_on=False
                break

    if not replay():
        break
