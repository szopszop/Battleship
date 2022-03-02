from copy import deepcopy
import os, time

height = 5
width = 5
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_difficulty(): # extra
    pass


def create_game_board(height) -> list:
    board = []
    for i in range(height):
        board.append(['o'] * height)
    return board


def cover_board(board):
    covered_board = []
    for row in board:
        covered_row = []
        for l in row:
            covered_row.append(str(l))
        covered_board.append(covered_row)
    return covered_board


def print_board(board):
    char = 0
    i = 1
    h = []
    while (i <= height):
        h.append(str(i))
        i = i + 1
    x = ' '.join(h)
    # print(h)
    print("")
    print('        ' + x)
    print('        ' + '↓ ' * width)
    print('       ' + '__' * width)
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "→ ", "|", element, "|")
        print("")
    print('       ' + '--' * width)
    return board


def display_boards(display_board_1, display_board_2):
    print('\nPlayer 1       Player 2')
    print('  1 2 3 4 5      1 2 3 4 5')
    for i in range(len(display_board_1)):
        print(chr(65+i)+ ' '+' '. join(display_board_1[i])+'    '+chr(65+i)+ ' '+' '. join(display_board_2[i]))
    print()


def get_field_position(height, width):
    position = input('\nPlease select a field: ')
    if len(position) <= 1 or (len(position) > 2 or position[0].upper() not in alphabet or position[1] not in numbers):
        print("Incorrect input! (Must be only a letter and a number)")
        return get_field_position(height, width)
    else:
        column = int(position[1]) - 1
        row = alphabet.find(position[0].upper())
        if row >= height or column + 1 > width:
            print("Incorrect input! (Exceeds number of columns or rows)")
            return get_field_position(height, width)
        return row, column


def check_valid_position(board, row, column) -> bool:
    if row >= height or row < 0 or column >= width or column < 0:
        return True
    elif board[row][column] == 'X':
        return False
    
    return True


def check_for_neighbours(board, row, column) -> bool:
    try:
        if board[row+1][column] == 'X':
            return False
        elif board[row-1][column] == 'X':
            return False
        elif board[row][column+1] == 'X':
            return False        
        elif board[row][column-1] == 'X':
            return False
        return True
    except IndexError:
        return True
        print('index error')

def disallowed_fields(board, row, column):
    disallowed_fields = []






def ask_for_ship_orientation():
    direction = input("Horizontal or Vertical? [H/W]").upper()
    while not (direction == 'H' or direction == 'V'):
        direction = input("Horizontal or Vertical? [H/V]").upper()
    if direction == 'H': 
        return False
    return True


def validation(game_board) -> tuple:
    valid_flag, neighbours_flag = False, False
    
    while not (valid_flag and neighbours_flag):
        valid_flag, neighbours_flag = False, False

        row, col = get_field_position(height, width)
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
        game_board[row][col] = 'X'

    if ship > 1:
        if ask_for_ship_orientation():          # True = horizontal
            for i in range(ship):
                if row >= width: 
                    return False
                    
                else:
                    game_board[row+i][col] = 'X'
            return True
        else:                                   # False = vertical
            for i in range(ship):
                if row >= height: 
                    return False
                else:
                    game_board[row][col+i] = 'X'
            return True      

                
def game_setup() -> list:
    game_board_1 = create_game_board(height)
    game_board_2 = create_game_board(height)
    display_board_1 = deepcopy(game_board_1)
    display_board_2 = deepcopy(game_board_2)
    return game_board_1, game_board_2, display_board_1, display_board_2


def placement_phase():
    print('\nWelcome to the Battleship game!')
    game_board_1, game_board_2, display_board_1, display_board_2 = game_setup()
    print_board(game_board_1)

    ships = [3, 2, 1]
    # Player_1
    print('Player 1 turn.')
    for ship in ships:
        print(f'Choose place for a ship of size {ship}.')
        row, col = validation(game_board_1)
        while not placing_ships(game_board_1, row, col, ship):
            print("Your ship doesn't fit. Try again.")
            row, col = validation(game_board_1)
        print_board(game_board_1)
    # Player_2
    print('\nPlayer 2 turn.\n')
    for ship in ships:
        print(f'Choose place for a ship of size {ship}.')
        row, col = validation(game_board_2)
        while not placing_ships(game_board_2, row, col, ship):
            print("Your ship doesn't fit. Try again.")
            row, col = validation(game_board_2)
        print_board(game_board_2)

    console_clear()
    display_boards(display_board_1, display_board_2)


def main():
    placement_phase()


if __name__ == "__main__":
     main()