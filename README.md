# Battleships Game

Battleships is a classic command-line implementation of the Battleship game in Python. The game randomly places ships on an 8x8 grid, and the player takes shots to sink all the ships within a limited number of bullets.

## Features

- Random placement of ships on the grid.
- Interactive gameplay with the user taking shots on the grid.
- Informative display of the grid, remaining ships, and game status.
- End-of-game messages indicating victory or defeat.
- Option to play the game again after completion.


## Gameplay

- The grid is displayed with row and column indices for user input.
- Enter the row and column numbers when prompted to take a shot.
- Valid shots are marked as 'X,' and misses are marked as 'M.'
- Sink all the ships within the specified number of bullets to win.

## Game Structure

The game is structured into modular functions, including:

- `place_ships()`: Randomly places ships on the grid.
- `display_ships_remaining()`: Prints the remaining ships.
- `display_grid()`: Displays the current state of the grid.
- `take_shot()`: Allows the user to take shots on the grid.
- `update_grid(row, col)`: Updates the grid based on the user's shot.
- `check_game_over()`: Checks if the game is over based on the number of sunk ships and remaining bullets.
- `reset_game()`: Resets the game for a new session.
- `play_battleships()`: The main function to execute the game.

## Deployment

*Create a New Heroku App**:

   - Log in to your Heroku account.
   - In the Heroku Dashboard, click the "New" button, then select "Create new app."
   - Choose a unique name for your app and click "Create App."

3. **Connect to GitHub**:

   - In the Heroku Dashboard, navigate to the "Deploy" tab.
   - In the "Deployment method" section, choose "GitHub."
   - Connect your Heroku app to your GitHub repository by searching for the repository name and clicking "Connect."


5. **Deploy Branch (Below automatic deploys)**:


6. **Open the App**:

   - Once the deployment is successful, click the "Open App" button in the top right corner of the Heroku Dashboard.

7. **Play the Game**:

   - Your Battleships game should now be accessible online via the Heroku app URL.


## Acknowledgments

- This project is inspired by the classic Battleship game.


