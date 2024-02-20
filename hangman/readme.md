# README for Hangman Game

## Introduction

Welcome to the Hangman game! This Python program allows users to play the classic Hangman game, where the player guesses a word one letter at a time. The game includes different difficulty levels, and players can choose from a variety of words.

## How to Play

1. **Game Levels:**
   - Select the difficulty level from the provided options: Easiest, Easy, Normal, Hard, Very hard.
   - Each level corresponds to a certain number of lives (attempts to guess the word).

2. **Guessing a Word:**
   - Enter a letter to guess the word.
   - The game will display the current state of the word, including correctly guessed letters and placeholders for unrevealed letters.

3. **Winning and Losing:**
   - Win: Guess all the letters correctly within the given number of lives.
   - Lose: Run out of lives without completing the word.

## Code Structure

The code is organized into several functions to facilitate readability and maintainability:

- `valid`: Selects a valid word for the game, excluding words with hyphens or spaces.
- `hangman`: Implements the main game logic, allowing users to input letters and updating the game state accordingly.

The game level is chosen using the `inquirer` library, and the difficulty level mapping is provided in the `GAME_LEVEL_MAPPING` dictionary.

## Running the Code

1. Ensure you have Python installed on your system.
2. Install the required dependencies (`termcolor` and `inquirer`) using:
   ```bash
   pip install termcolor inquirer
   ```
3. Copy and paste the provided Python code into a Python file (e.g., `hangman.py`).
4. Run the file using a Python interpreter.

## Additional Notes

- The game level determines the number of lives available to the player.
- The program uses the `termcolor` library for colored console output.
- Words for the game are stored in an external file (`words.py`), and visuals for hangman stages are stored in `visuals_list.py`.
- Enjoy playing Hangman! If you encounter any issues or have suggestions for improvement, feel free to provide feedback.

Feel free to explore and enjoy the Hangman game! If you encounter any issues or have suggestions for improvement, please let me know.
