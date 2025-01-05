'''
Programmer : Abdul Basit
'''

import os
import keyboard

MAP_FILE = 'Final_map.txt'
HELP_FILE = 'help.txt'

os.system("")

def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
        
def load_map(map_file):
    """
    Loads a map from a file as a grid (list of lists)
    """
    # TODO: implement this function
    file = open(map_file, 'r')
    grid = file.readlines()
    for Item in range(len(grid)):
        grid[Item] = list(grid[Item].rstrip('\n'))
    return grid

def find_start(grid):
    """
    Finds the starting position of the player on the map.
    """
    # TODO: implement this function
    for I in range(len(grid)):
        for J in range(len(grid[I])):
            if grid[I][J] == 'S':
                Index = [I, J]
                return Index

def get_command():
    """
    Gets a command from the user.
    """
    # TODO: implement this function
    key = keyboard.read_key()
    if keyboard.is_pressed("esc"):
        return "quit"
    if keyboard.is_pressed("h"):
        return "help"
    if keyboard.is_pressed("up")or keyboard.is_pressed("w"):
        return "north"
    if keyboard.is_pressed("down") or keyboard.is_pressed("s"):
        return "south"
    if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
        return "west"
    if keyboard.is_pressed("right") or keyboard.is_pressed("d"):
        return "east"


def display_map(grid, player_position): # player_position  = [1 ,0]
    """
    Displays the map.
    """
    # TODO: implement this function
    for I in range(len(grid)):
        for J in range(len(grid[I])):
            '''
            the position of the index and playpiece is the same and second condition player position is the updated position
            '''
            if grid[I][J] == grid[player_position[0]][player_position[1]] and [I, J] == player_position: 
                print('🧝', end = '')
            else:
                if grid[I][J] == '*':
                    print('🧱', end = '')
                if grid[I][J] == 'S':
                    print('🏠', end = '')
                if grid[I][J] == 'F':
                    print('🏺', end = '')
                if grid[I][J] == '-':
                    print('🟢', end ='')              
        print(end = '\n')

def display_finish_map(grid, player_position): # player_position  = [1 ,0]
    """
    Displays the map.
    """
    # TODO: implement this function
    for I in range(len(grid)):
        for J in range(len(grid[I])):
            '''
            the position of the index and playpiece is the same and second condition player position is the updated position
            '''
            if grid[I][J] == '*':
                print('🧱', end = '')
            if grid[I][J] == 'S':
                print('🏠', end = '')
            if grid[I][J] == 'F':
                print('🧝', end = '')
            if grid[I][J] == '-':
                print('🟢', end ='')              
        print(end = '\n')

def get_grid_size(grid):
    """
    Returns the size of the grid.
    """
    # TODO: implement this function
    size_of_grid = []
    size_of_grid.append(len(grid))
    size_of_grid.append(len(grid[0]))
    return size_of_grid    

def is_inside_grid(grid, position):
    """
    Checks if a given position is valid (inside the grid).
    """
    # TODO: implement the rest of the function
    grid_rows, grid_cols = get_grid_size(grid)
    player_row, player_col = position
    return 0 <= player_row < grid_rows and 0 <= player_col < grid_cols

def look_around(grid, player_position): # Obtaining directions
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '-')
    row, col = player_position[0], player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('east')
    return directions

def move(direction, player_position, grid): # Updating the player index positional values
    """
    Moves the player in the given direction.
    """
    # TODO: implement this function
    directions = look_around(grid, player_position)
    for I in directions:
        if direction == I:
            if direction == 'north':
                player_position[0], player_position[1] = player_position[0] - 1, player_position[1]
                return True
            elif direction == 'south':
                player_position[0], player_position[1] = player_position[0] + 1, player_position[1]
                return True
            elif direction == 'west':
                player_position[0], player_position[1] = player_position[0], player_position[1] - 1
                return True
            elif direction == 'east':
                player_position[0], player_position[1] = player_position[0], player_position[1] + 1
                return True
    if direction not in directions:
        return False

def check_finish(grid, player_position):
    """
    Checks if the player has reached the exit.
    """
    # TODO: implement this function
    Finish_index_list = []
    for I in range(len(grid)):
        for J in range(len(grid[I])):
            if grid[I][J] == 'F':
                Finish_index_list.append(I)
                Finish_index_list.append(J)
    if Finish_index_list == player_position:
        return True
    else:
        return False

def display_help() -> None:
    """
    Displays a list of commands.
    """
    # TODO: implement this function
    help_file = open(HELP_FILE, 'r')
    lines = help_file.readlines()
    for I in lines:
        print(I)
    

def main():
    global player_position
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function
    print("* + x - - - - - PRESS 'H' for GAME INSTRUCTIONS - - - - - x + *\n")
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    display_map(grid, player_position)
    Light = 'Green'
    while Light == 'Green':
        directions = look_around(grid, player_position)
        cmd = get_command()
        if cmd == "quit":
            return
        elif cmd == "help":
            display_help()
        elif cmd == "north":
            result = move("north", player_position, grid)
            if result == True:
                clear_screen()
                display_map(grid, player_position)
            else:
                print("There is no way there.")
            finish = check_finish(grid, player_position)
            if finish == True:
                clear_screen()
                display_finish_map(grid, player_position)
                print()
                print('Congratulations! You have reached the exit!')
                return
            else:
                continue
        elif cmd == "south":
            result = move("south", player_position, grid)
            if result == True:
                clear_screen()
                display_map(grid, player_position)                
            else:
                print("There is no way there.")
            finish = check_finish(grid, player_position)
            if finish == True:
                clear_screen()
                display_finish_map(grid, player_position)
                print()
                print('Congratulations! You have reached the exit!')
                return
            else:
                continue
        elif cmd == "west":
            result = move("west", player_position, grid)
            if result == True:
                clear_screen()
                display_map(grid, player_position)                
            else:
                print("There is no way there.")
            finish = check_finish(grid, player_position)
            if finish == True:
                clear_screen()
                display_finish_map(grid, player_position)
                print()
                print('Congratulations! You have reached the exit!')
                return
            else:
                continue
        elif cmd == "east":
            result = move("east", player_position, grid)
            if result == True:
                clear_screen()
                display_map(grid, player_position)                    
            else:
                print("There is no way there.")
            finish = check_finish(grid, player_position)
            if finish == True:
                clear_screen()
                display_finish_map(grid, player_position)
                print()
                print('Congratulations! You have reached the exit!')
                return
            else:
                continue
        else:
            print()
    
if __name__ == '__main__':
    main()

