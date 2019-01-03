def create_table():
    '''
    Docstring explaines function
    DOCSTRING: information about the function
    INPUT: no input
    OUTPUT: returns list of lists to set 6x6 table to play tic tac toe
    '''
    tab = [] 
    for i in range(3):
        tab.append (list(('_', '_', '_')))
    return tab

def print_table(tab):
    for i in range(3):
        print(tab[i])
        
def turns (tab, player, row, col):
    tab[row-1][col-1] = player
    return tab

def check_turn (tab, player, flag):
    for i in range(3):
        if tab[i][0] == tab [i][1] == tab [i][2] == player:
            flag = True
        elif tab[0][i] == tab [1][i] == tab [2][i] == player:
            flag = True
    if tab[0][0] == tab[1][1] == tab[2][2] == player or tab[0][2] == tab[1][1] == tab[2][0] == player:
        flag = True
        
    if flag:
        print_table(tab)
        if player == 'X':
            print ('Player #1 is the winner!')
        else:
            print ('Player #2 is the winner!')
    return flag
    
def players_turns (tab, player):
    flag = False
    while flag == False:
        row = input ('Player #{}, your turn! Choose row (from 1 to 3): '.format(player))
        col = input ('Choose column (from 1 to 3): ')
        if is_number(row) and is_number(col):
            flag = correct_turn(tab, int(row), int(col))
        else:
            print ('One of the parameters is not integer number! Try again!')
    return int(row), int(col)

def correct_turn(tab, row, col):
    flag = True
    if row < 1 or row > 3 or col < 1 or col > 3:
        print ('Out of range! Try again!')
        flag = False
    elif tab[row-1][col-1] != '_':
        print ('This cell is occupied! Try again!')
        flag = False
    
    return flag

def is_number (s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def the_end (tab, flag):
    flag = True
    for i in range (3):
        for j in range (3):
            if tab[i][j] == '_':
                flag = False
    if flag:
        print ('The end!')
    return flag

def end_of_the_game(tab):
    for i in range(3):
        for j in range (3):
            if tab[i][j] == '_':
                return False
    
    
    
turns_flag = False       
table = create_table()
player1 = 'X'
player2 = 'O'
player = ''
end_flag = False
count_turns = 0


while turns_flag == False:
    
    for i in range(1,3):
        if i == 1:
            player = player1
        else:
            player = player2
            
        print_table(table)
        turn_row, turn_col = players_turns(table, i)
        count_turns += 1
        print(count_turns)
        turns(table, player, turn_row, turn_col)
        turns_flag = check_turn (table, player, turns_flag)
        if turns_flag or count_turns == 9:
            turns_flag = True
            break
