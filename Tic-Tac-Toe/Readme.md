# README for Tic-Tac-Toe Game

## Introduction

Welcome to the Tic-Tac-Toe game! This Python program allows users to play the classic Tic-Tac-Toe game against another player or against the computer. The game supports two-player mode and single-player mode with two difficulty levels: easy and hard.

## How to Play

1. **Two Players:**
   - Select option 1 in the main menu.
   - Players take turns entering their moves by specifying the position on the board (1 to 9).
   - The game ends when a player wins or the board is full, resulting in a tie.

2. **One Player (Easy):**
   - Select option 2 in the main menu.
   - Enter your preferred symbol (X or O).
   - The game will randomly choose the starting player.
   - Players take turns entering their moves, and the computer (AI) makes random moves.
   - The game ends when a player wins or the board is full, resulting in a tie.

3. **One Player (Hard):**
   - Select option 3 in the main menu.
   - Enter your preferred symbol (X or O).
   - The game will randomly choose the starting player.
   - Players take turns entering their moves, and the computer (AI) employs a minimax algorithm for strategic moves.
   - The game ends when a player wins or the board is full, resulting in a tie.

## Code Structure

The code is organized into several functions to facilitate readability and maintainability:

- `print_board_state`: Displays the current state of the Tic-Tac-Toe board.
- `check_win`: Checks if there is a winner or if the game is a tie.
- `two_players`: Implements the game logic for two human players.
- `one_player_easy`: Implements the game logic for one human player against an easy-level computer AI.
- `one_player_hard`: Implements the game logic for one human player against a hard-level computer AI.
- `empty_space`: Returns a list of empty spaces on the board.
- `minmax_result` and `minmax`: Implement the minimax algorithm for the hard-level computer AI.

## Running the Code

1. Ensure you have Python installed on your system.
2. Copy and paste the provided Python code into a Python file (e.g., `tic_tac_toe.py`).
3. Run the file using a Python interpreter.

## Additional Notes

- The game board is represented as a list of length 9, where each index corresponds to a position on the board.
- The main menu allows the user to choose the game mode: two players, one player easy, or one player hard.
- The program includes error handling for invalid moves and choices.

Feel free to explore and enjoy the Tic-Tac-Toe game! If you encounter any issues or have suggestions for improvement, please let me know.
