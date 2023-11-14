import random
import os
import sys


"""
The game variables and basic structure of the game
"""
grid_size = 8
grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]

num_of_ships = 5
bullets_left = 50
game_over = False
num_of_ships_sunk = 0
ship_positions = []

def place_ships():
    """
    Place ships randomly on the grid
    """
    global ship_positions
    ship_positions = []

    for _ in range(num_of_ships):
        ship_size = random.randint(3, 5)
        orientation = random.choice(['horizontal', 'vertical'])

        if orientation == 'horizontal':
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - ship_size)
            new_ship = [(row, col + i) for i in range(ship_size)]
        else:
            row = random.randint(0, grid_size - ship_size)
            col = random.randint(0, grid_size - 1)
            new_ship = [(row + i, col) for i in range(ship_size)]

        # Check if the new ship overlaps with existing ships
        while any(any(cell in ship for cell in new_ship) for ship in ship_positions):
            if orientation == 'horizontal':
                row = random.randint(0, grid_size - 1)
                col = random.randint(0, grid_size - ship_size)
                new_ship = [(row, col + i) for i in range(ship_size)]
            else:
                row = random.randint(0, grid_size - ship_size)
                col = random.randint(0, grid_size - 1)
                new_ship = [(row + i, col) for i in range(ship_size)]

        ship_positions.append(new_ship)





def display_ships_remaining():
    """
    Print the remaining ships and their sizes
    """
    print("Remaining Ships:")
    for ship in ship_positions:
        if ship: 
            size = len(ship)
            print(f"{ship[0][0]}-class Ship: Size {size}")



def display_grid():
    """
    Display the current state of the grid.
    """
    print("\n   " + " ".join(str(i) for i in range(grid_size)))
    for i, row in enumerate(grid):
        print(f"{i} | {' '.join(cell for cell in row)}")
    print()
    display_ships_remaining()


def take_shot():
    """
    Take shot from the user.
    """
    try:
        while True:
            
            for i, row in enumerate(grid):
                print(f"{i} | {' '.join(cell for cell in row)}")
            print()

            row = int(input('Enter row (0-7): '))
            col = int(input('Enter column (0-7): '))

            if not (0 <= row < grid_size and 0 <= col < grid_size):
                print('Invalid input. Row and column must be between 0 and 7.')
            elif grid[row][col] == 'X' or grid[row][col] == 'M':
                print('You already shot this cell. Try again.')
            else:
                print('Valid shot!')
                return int(row), int(col)
    except ValueError:
        print('Invalid input. Please enter numbers.')
        return take_shot()



def update_grid(row, col):
    global bullets_left, num_of_ships_sunk

    if grid[row][col] == 'X' or grid[row][col] == 'M':
        print(f'You already shot this cell ({row}, {col}). Try again.')
        return

    bullets_left -= 1 

    hit_ship = None

    for ship in ship_positions:
        for cell in ship:
            if (row, col) == cell:
                hit_ship = ship
                break
        if hit_ship:
            break

    if hit_ship:
        print('Hit!')
        print(f'Before: {hit_ship}')
        hit_ship.remove((row, col))
        grid[row][col] = 'X'
        if not hit_ship:
            print('You sunk a ship!')
            num_of_ships_sunk += 1
            print('After:', ship_positions)
            ship_positions.remove(hit_ship)
    else:
        print('Miss!')
        grid[row][col] = 'M'

    






def check_game_over():
    """
    Checks if the game is over
    """
    global game_over
    print(f"Ships sunk: {num_of_ships_sunk}, Number of ships: {num_of_ships}, Bullets left: {bullets_left}")
    if num_of_ships_sunk == num_of_ships or bullets_left <= 0:
        game_over = True
    
   

        

def reset_game():
    """
    Reset the game for a new game
    """
    global grid, bullets_left, game_over, num_of_ships_sunk, ship_positions
    grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
    bullets_left = 50
    game_over = False
    num_of_ships_sunk = 0
    ship_positions = []

    

def play_battleships():
    """
    Main function to play the game
    """
    place_ships()

    while not game_over:
        row, col = take_shot()
        update_grid(row, col)
        check_game_over()

    if num_of_ships_sunk == num_of_ships:
        print('Congratulations! You sunk all the ships.')
    else:
        print('Game over. Out of bullets.')

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() == 'yes':
        reset_game()
        play_battleships()
    else:
        print('Thank you for playing!')


if __name__ == "__main__":
    play_battleships()
