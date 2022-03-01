

height = 5
width = 5
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'


def get_difficulty(): # extra
    pass


def create_game_board() -> list:
    game_board = [[0]* width for i in range(height)]
    return game_board


def get_field_position(height, width):
    position = input('\nPlease select a field: ')
    if len(position) <= 1 or (len(position) > 2 or position[0].upper() not in alphabet or position[1] not in numbers):
        print("Incorrect input! (Must be only a letter and a number)")
        return get_field_position(height, width)
    else:
        position_x = int(position[1]) - 1
        position_y = alphabet.find(position[0].upper())
        if position_x >= height or position_y + 1 > width:
            print("Incorrect input! (Exceeds number of columns or rows)")
            return get_field_position(height, width)
        return position_x, position_y


def print_board():
    pass


def user_move(game_board_1: list, game_board_2: list) -> tuple:
    is_empty_flag = False
    no_collision_flag = False

    while not (is_empty_flag and no_collision_flag):
        is_empty_flag = False
        no_collision_flag = False

        position_x, position_y = get_field_position(height, width)
        
        
        if game_board_1[position_x][position_y] == 0:
            is_empty_flag = True
        if game_board_2[position_x][position_y] == 0:
            is_empty_flag = True  
        else:
            print('\nField already taken.')
            continue

        


        if is_empty_flag and no_collision_flag:
            return position_x, position_y



def ask_for_ship_orientation():
    direction = input("Horizontal or Vertical? [H/W]").upper()
    while not (direction == 'H' or direction == 'W'):
        direction = input("Horizontal or Vertical? [H/W]").upper()
    if direction == 'H': return True
    else: return False


def game_logic():
    game_board_1 = create_game_board()
    game_board_2 = create_game_board()



def main():
    game_logic()


if __name__ == "__main__":
    main()