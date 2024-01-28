import sys

def game_board(board):
    print('   |   | ')
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print('   |   | ')


test_board = ['#','1','2','3','4','5','6','7','8','9']
counter = 0
symbol_board = ['#','X','O','X','O','X','O','X','O','X']

def select_pos(counter):

    num_check = True
    while num_check is True:
        answer = input("Select the position you would like to play: ")

        if answer.isdigit() and 0<int(answer)<10:
            num_check = False
        else:
            print("Invalid Value")
    counter = place_pos(int(answer), counter)
    return counter

def place_pos(position,counter):
    counter += 1
    print(counter)
    test_board[position] = symbol_board[counter]
    print("\n"*50)
    game_board(test_board)
    if win_check(test_board,symbol_board[counter]) is True:
        print("Congratulations! You have won")
        sys.exit()
    return counter

def welcome():
    print("  ")
    print("  ")
    print("  ")
    print("Welcome to Tic Tac Toe!")
    print(" ")
    print("The symbol for the first player: X")
    print(" ")
    print("The symbol for the second player: Y")
    counter = 0 
    game_on = True
    while game_on is True:

        game_board(test_board)
        counter = select_pos(counter)
        check = input("Would you like to continue (Y/N)?: ")
        
        if check == "N":
            game_on = False


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

welcome()