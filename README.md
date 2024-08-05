# Hangman Game
## Version 0.2.2
## Description
This is a simple command-line Hangman game coded in Python. The game selects a random word from a (not very long) word list, and the player has to guess the word one letter at a time. The player has a limited number of attempts to guess the word correctly before the game ends.

## How to Play
Run the script. See https://github.com/QinCai-rui/hangman/README.md#usage
The game will display the word with underscores (_) representing each letter.
Guess a letter by typing it and pressing Enter.
If the guessed letter is in the word, it will be revealed in its correct position(s).
If the guessed letter is not in the word, you lose an attempt.
The game continues until you either guess the word correctly or run out of attempts.
## Features
Random word selection from a list of words.
Visual representation of the Hangman stages using ASCII characters. 
Input validation to ensure valid guesses.
Option to play again after the game ends.
## Requirements
1. Python 3.x Installation
2. Clone the repository or download the script.
3. Ensure you have Python 3.x installed on your system.
## Usage
Run the script using the following command:

`python3 hangman.py`

