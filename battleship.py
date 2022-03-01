

from copy import deepcopy


height = 5
width = 5
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
ship_size = 3
size = 5


def get_difficulty(): # extra
    pass


def create_game_board(size) -> list:
    board = []
    for i in range(size):
        board.append(['o'] * size)
    return board

def print_board(board, size):
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
    print('       ' + '__' * size)
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "→ ", "|", element, "|")
        print("")
    print('       ' + '--' * size)
    return board


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


def check_valid_position(board, row, column) -> bool:
    if row >= height or row < 0 or column >= width or column < 0:
        return True
    elif board[row][column] == 'X':
        return False
    else:
        return True


def place_ship(board): # work in progress, only places 3 size 1 ships ~Sebastian
    game_board = deepcopy(board)
    size = 0
    while size != ship_size:
        row, column = get_field_position(height, width) 
        if check_valid_position(game_board, row, column) and check_valid_position(game_board, row-1, column) and check_valid_position(game_board, row+1, column) and check_valid_position(game_board, row, column - 1) and check_valid_position(game_board, row, column + 1):
            game_board[row][column] = 'X'
            print_board(game_board)
            size += 1
        else:
            print_board(game_board)
            print("\nInvalid position! Try some place else")
    print("Done")


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



def player_1_start_deployment_procedure():
      print(f'Player 1 deploys ships.')

      print_board()

      # petla rozmieszczania statkow
      ship_sizes = [2,1]
      for current_size in ship_sizes: ## dla kazdego z rozmiarow statkow w tablicy ship_sizes
          move_acceptable=False        ## zaloz ze ruch nie jest dopuszczalny
          while not move_acceptable:
               print(f'Select position for a ship of {current_size} size: ')
               start_position = user_move(current_size)   # pobierz pozycje startowa
               is_horizontal = ask_for_ship_orientation()        # pobierz orientacje statku
               move_acceptable = is_move_allowed(start_position,is_horizontal)  # sprawdz czy ruch jest akceptowalny
               
               if move_acceptable:
                    place_ship(start_position, is_horizontal) # zapisz na tablicy
                    print("Ship placed successfully.")       # wyswietl komunikat
                    print_board()
               else:
                    print("Not possible.")            # poinformuj o bledzie i rozpocznij while od nowa

                    
# def is_move_allowed():
#     return True


# def game_logic():
#     game_board_1 = create_game_board()
#     game_board_2 = create_game_board()



# def main():
#     game_logic()
    


# if __name__ == "__main__":
#     main()
# create_game_board(size)
# print_board([["o","o","o","o","o"],["o","o","o","o","o"],["o","o","o","o","o"],["o","o","o","o","o"], ["o","o","o","o","o"]], size)