import os, time, random

size = 5
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
ships = [1, 2, 3]

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_difficulty(): #TODO
    pass


def create_board(size) -> list:
    board = []
    for i in range(size):
        board.append(['o'] * size)
    return board
    


def print_board(board):
    char = 0
    i = 1
    h = []
    while (i <= size):
        h.append(str(i))
        i = i + 1
    x = ' '.join(h)
    # print(h)
    print("")
    print('        ' + x)
    print('        ' + '↓ ' * size)
    print('       ' + '--' * size+'-')
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "→ ", "|", element, "|")
    print('       ' + '--' * size+'-')
    return board


def print_both_boards(game_board_1, game_board_2):
    char = 0
    i = 1
    num_arr = []
    while (i <= size):
        num_arr.append(str(i))
        i = i + 1
    numbers_str = ' '.join(num_arr)
    print("\n Player_1             Player_2")
    print('      ' + numbers_str + '           ' + numbers_str)
    print('      ' + '↓ ' * size + '          ' + '↓ ' * size)
    print('     ' + '--' * size+'-'+ '         ' + '--' * size+'-')
    for i in range(len(game_board_1)):
        char += 1
        print(chr(char + 64).rjust(2), "→ "+ "|"+ ' '. join(game_board_1[i])+ "|     "+ chr(char + 64).rjust(2)+ "→ "+ "|"+ ' '. join(game_board_2[i])+ "|")
    print('     ' + '--' * size+'-'+ '         ' + '--' * size+'-')


def get_field_position(row, col):
    position = input('\nPlease select a field: ')
    if len(position) <= 1 or (len(position) > 2 or position[0].upper() not in alphabet or position[1] not in numbers):
        print("Incorrect input! (Must be only a letter and a number)")
        return get_field_position(row, col)
    else:
        column = int(position[1]) - 1
        row = alphabet.find(position[0].upper())
        if row >= size or column + 1 > size:
            print("Incorrect input! (Exceeds number of columns or rows)")
            return get_field_position(row, col)
        return row, column


def check_valid_position(board, row, column) -> bool:
    if row >= size or row < 0 or column >= size or column < 0:
        return True
    elif board[row][column] in [str(ship) for ship in ships]: 
        return False
    return True


def check_for_neighbours(board, row, column) -> bool:
    try:
        if board[row+1][column] in ships:
            return False
        elif board[row-1][column] in ships:
            return False
        elif board[row][column+1] in ships:
            return False        
        elif board[row][column-1] in ships:
            return False
        return True
    except IndexError:
        return True


def ask_for_ship_orientation():
    direction = input("Horizontal or Vertical? [H/V]").upper()
    while not (direction == 'H' or direction == 'V'):
        direction = input("Horizontal or Vertical? [H/V]").upper()
    if direction == 'H': 
        return False
    return True


def validation(game_board) -> tuple:
    valid_flag, neighbours_flag = False, False
    
    while not (valid_flag and neighbours_flag):
        valid_flag, neighbours_flag = False, False

        row, col = get_field_position(size, size)
        if check_valid_position(game_board, row, col):
            valid_flag = True
        else:
            print('Invalid move.')
            continue
        if check_for_neighbours(game_board, row, col):
            neighbours_flag = True
        else:
            print('Invalid move.')
            continue
        
        if valid_flag and neighbours_flag:
            return row, col


def placing_ships(game_board, row, col, ship):
    if ship == 1:
        if check_signle_ship(game_board, row, col):
            game_board[row][col] = '1'
            return True
        else:
            return False
    if ship > 1:
        if ask_for_ship_orientation():          # True = horizontal
            for i in range(ship):
                if row + i >= size: 
                    return False
            if check_valid_position(game_board, row-1, col):
                valid = check_horizontal(game_board, row, col, ship)
                if valid:
                    for i in range(ship):
                        game_board[row+i][col] = str(ship)
                    return True
                return False                    
            return False
        else:                                   # False = vertical
            for i in range(ship):
                if col + i >= size: 
                    return False
            if check_valid_position(game_board, row, col - 1):
                valid = check_vertical(game_board, row, col, ship)
                if valid:
                    for i in range(ship):
                        game_board[row][col+i] = str(ship)
                    return True
                return False 


def check_signle_ship(game_board, row, col):
    return check_valid_position(game_board, row, col) and \
            check_valid_position(game_board, row-1, col) and \
                check_valid_position(game_board, row+1, col) and \
                    check_valid_position(game_board, row, col - 1) and \
                        check_valid_position(game_board, row, col + 1)


def check_horizontal(game_board, row, col, ship):
    valid = True
    for i in range(ship):
        if not (check_valid_position(game_board, row, col) and \
                        check_valid_position(game_board, row+i, col) and \
                            check_valid_position(game_board, row, col - i) and \
                                check_valid_position(game_board, row, col + i)):
                        valid = False
    return valid


def check_vertical(game_board, row, col, ship):
    valid = True
    for i in range(ship):
        if not (check_valid_position(game_board, row, col) and \
                        check_valid_position(game_board, row - i, col) and \
                            check_valid_position(game_board, row + i, col) and \
                                check_valid_position(game_board, row, col + i)):
                        valid = False
    return valid   

                
def game_setup() -> list:
    game_board_1 = create_board(size)
    game_board_2 = create_board(size)
    return game_board_1, game_board_2


def placement_phase():
    game_board_1, game_board_2 = game_setup()
    print_board(game_board_1)
    ships = [3, 2, 1]
    print('Player 1 turn.')
    for ship in ships:
        print(f'Choose place for a ship of size {ship}.')
        row, col = validation(game_board_1)
        while not placing_ships(game_board_1, row, col, ship):
            print_board(game_board_1)
            print("Your ship cannot be placed here. Try again.")
            row, col = validation(game_board_1)
        print_board(game_board_1)  
    input("Press enter to continue...")
    console_clear()
    print_board(game_board_2)
    print('\nPlayer 2 turn.\n')
    for ship in ships:
        print(f'Choose place for a ship of size {ship}.')
        row, col = validation(game_board_2)
        while not placing_ships(game_board_2, row, col, ship):
            print_board(game_board_2)
            print("Your ship cannot be placed here. Try again.")
            row, col = validation(game_board_2)
        print_board(game_board_2)
    console_clear()
    return game_board_1, game_board_2


def get_random_move(board, player):
    random_decisions = []
    for row in board:
        for col in board:
            if board[row][col] == 'o':
                random_decisions.append(tuple(row, col))
    time.sleep(2)
    return random.choice(random_decisions)


def ask_for_turn_limit():
    while True:
        limit = input('Select the turn limit (must be between 5-50): ')
        if limit.isnumeric():
            limit = int(limit)
            if limit >= 5 and limit <= 50:
                return limit
            else:
                print('Invalid input! (must be between 5-50)')
        else:
            print('Invalid input! (must be a number)')


def shooting(game_board_1, game_board_2, limit):
    display_board_1 = create_board(size) 
    display_board_2 = create_board(size)
    sunk_1 = 0
    sunk_2 = 0
    print_both_boards(display_board_1, display_board_2)
    while True:
        while limit > 0:
            print(f'Remaining rounds: {limit}\n')
            limit -= 1
            sunk_2 = player_move(game_board_2, display_board_2, display_board_1, display_board_2, sunk_2, "Player_1")
            if sunk_2 == sum(ships):
                return 'Player 1'
            
            sunk_1 = player_move(game_board_1, display_board_1, display_board_1, display_board_2, sunk_1, "Player_2")
            if sunk_1 == sum(ships):
                return 'Player 2'
        return 'Timeout'


def player_move(game_board, printed_board, display_board_1, display_board_2, sunk, player):
    print(f'{player} move: ')
    row, col = get_field_position(size, size)
    if game_board[row][col] in ['1', '2', '3']:
        sunk = hit_the_ship(game_board, printed_board, sunk, row, col)
    if game_board[row][col] == 'o':
        miss_the_shot(game_board, printed_board, row, col)
    if game_board[row][col] in ['H', 'S']:
        print("\nYou've already shot this field!")
    print_both_boards(display_board_1, display_board_2)
    return sunk


def miss_the_shot(game_board, printed_board, row, col):
    game_board[row][col] = 'M'
    printed_board[row][col] = 'M'
    print('Miss!')


def hit_the_ship(game_board, printed_board, sunk, row, col):
    sunk += 1
    ship = game_board[row][col]
    game_board[row][col] = 'H'
    printed_board[row][col] = 'H'
    if check_if_sunk(game_board, ship):
        sink_ship(printed_board)
    print("You've hit a ship!")
    print(ship)
    return sunk

    
def check_if_sunk(board, ship):
    sunk = True
    for line in board:
        if ship in line:
            sunk = False
    return sunk


def sink_ship(board):
    for row in board:
        for i in range(size):
            if row[i] == 'H':               
                row[i] = 'S'


def choose_level():
    global size
    sizes = [5,6,7,8,9,10]
    user_input = input("Choose the size of the game board you want to play. (5-10)\n: ")
    while int(user_input) not in sizes:
        user_input = input("Choose the size of the game board you want to play. (5-10)\n: ")
    size = int(user_input)


def main():
    print('\nWelcome to the Battleship game! ')
    limit = ask_for_turn_limit()
    choose_level()
    # choose_ships()
    game_board_1, game_board_2 = placement_phase()
    who_won = shooting(game_board_1, game_board_2, limit)
    if who_won == 'Timeout':
        print("\nThe turn limit reached, nobody has won. :(")
        quit()
    print('\nCongratulations!')
    print(f'{who_won} won the game! ( ͡° ͜ʖ ͡°)')


if __name__ == "__main__":
     main()