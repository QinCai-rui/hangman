# version 0.0.1

import random

words = ["python", "hangman", "challenge", "programming"]

def get_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_guess():
    guess = input("Guess a letter: ").lower()
    while not guess.isalpha() or len(guess) != 1:
        guess = input("Invalid input. Guess a single letter: ").lower()
    return guess

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    print(stages[tries])

def play_hangman():
    word_to_guess = get_word()
    guessed_letters = set()
    tries = 0
    max_tries = 6

    while tries < max_tries:
        print(display_word(word_to_guess, guessed_letters))
        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            if set(word_to_guess) <= guessed_letters:
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            tries += 1
            display_hangman(tries)

        if tries == max_tries:
            print(f"Game over! The word was: {word_to_guess}")

play_hangman()

