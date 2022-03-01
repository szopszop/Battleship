

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

                    
def is_move_allowed():
    return True


def game_logic():
    game_board_1 = create_game_board()
    game_board_2 = create_game_board()



def main():
    game_logic()


if __name__ == "__main__":
    main()