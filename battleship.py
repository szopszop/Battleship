

height = 5
width = 5
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
ship_size = 3


def get_difficulty(): # extra
    pass


def create_game_board(width, height) -> list:
    game_board = [[0]* width for i in range(height)]
    return game_board


def get_field_position(height, width):
    position = input('\nPlease select a field: ')
    if len(position) <= 1 or (len(position) > 2 or position[0].upper() not in alphabet or position[1] not in numbers):
        print("Incorrect input! (Must be only a letter and a number)")
        return get_field_position(height, width)
    else:
        row = int(position[1]) - 1
        column = alphabet.find(position[0].upper())
        if row >= height or column + 1 > width:
            print("Incorrect input! (Exceeds number of columns or rows)")
            return get_field_position(height, width)
        return row, column


def print_board():
    pass


def place_ship(game_board): # work in progress ~Sebastian
    size = 0
    
    while size != ship_size:
        row, column = get_field_position(height, width)
        try:
            if game_board[row - 1 : row + 2][column] == 'X' or game_board[row][column -1 : column + 2] == 'X':
                print("Ships cant be touching (except at the corners)")
                continue
        except IndexError:
            pass

        game_board[row][column] = 'X'




def user_move(game_board: list) -> tuple:
    is_empty_flag = False
    is_valid_flag = False

    while not (is_valid_flag and is_empty_flag):
        is_empty_flag = False
        is_valid_flag = False
        user_input = get_field_position(height, width)
        
        column = int(ord(user_input[0])-65)
        row = int(user_input[1:])-1 
        
        if game_board[row][column] == 0:
            is_empty_flag = True
        else:
            print('\nYou already picked this field.')
            continue

        if is_empty_flag and is_valid_flag:
            return row, column

        # add another flag, that checks for ships coliding"


def ask_for_ship_orientation():
    pass
    return None


def game_logic():
    pass


def main():
    pass


if __name__ == "__main__":
    main()