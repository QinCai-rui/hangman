# version 0.2.0

import random
from time import sleep

def get_word():
    words = ['apple', 'bread', 'chair', 'dance', 'eagle', 'fruit', 'grape', 'house', 'ivory', 'jelly', 
             'knife', 'lemon', 'mango', 'night', 'ocean', 'peach', 'queen', 'river', 'stone', 'tiger', 
             'union', 'vivid', 'whale', 'xenon', 'yield', 'zebra', 'blaze', 'crane', 'dream', 'flame', 
             'globe', 'haven', 'jolly', 'kneel', 'lunar', 'mirth', 'noble', 'orbit', 'piano', 'quilt', 
             'raven', 'shine', 'thorn', 'unity', 'valor', 'waltz', 'xylog', 'yacht', 'zealot', 'animal',
             'banana', 'castle', 'dragon', 'energy', 'flower', 'garden', 'heaven', 'island', 'jungle',
             'kitten', 'laptop', 'monkey', 'nature', 'orange', 'planet', 'quiver', 'rocket', 
             'sunset', 'tunnel', 'umbrella', 'victory', 'whisper', 'xylophone', 'yellow', 'zephyr', 
             'beacon', 'canyon', 'desert', 'empire', 'forest', 'galaxy', 'harbor', 'insect', 'jigsaw', 
             'knight', 'lantern', 'mystic', 'nectar', 'oracle', 'pirate', 'quasar', 'rescue', 'savage', 
             'trophy', 'utopia', 'voyage', 'wander', 'xenial', 'yonder', 'zephyr', 'adventure', 'butterfly',
             'chocolate', 'dinosaur', 'elephant', 'fireworks', 'grapefruit', 'happiness', 'important', 'jasmine',
             'kangaroo', 'lighthouse', 'mountain', 'notebook', 'orchestra', 'pineapple', 'question', 'rainbow',
             'sunshine', 'universe', 'vacation', 'wonderful', 'xenophobia', 'youthful', 'zoologist', 'beautiful',
             'champion', 'delicious', 'enchanted', 'fantastic', 'glamorous', 'harmonize', 'incredible', 'joyfulness',
             'knowledge', 'legendary', 'magnificent', 'nostalgia', 'optimistic', 'phenomenal', 'quintuple', 'radiation', 
             'spectacle', 'triumphant', 'unstoppable', 'vibrantly', 'whimsical', 'xenophile', 'yearning', 
             'zealously'
            ]

    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_guess(guessed_letters):
    guess = input("Guess a letter: ").lower()
    while not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
        else:
            print("Invalid input. Guess a single letter.")
        guess = input("Guess a letter: ").lower()
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
        print(f"You have {max_tries - tries} attempts remaining.")
        guess = get_guess(guessed_letters)

        if guess in word_to_guess:
            guessed_letters.add(guess)
            if set(word_to_guess) <= guessed_letters:
                sleep(0.5)
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            guessed_letters.add(guess)
            tries += 1
            display_hangman(tries)

        if tries == max_tries:
            sleep(0.5)
            print(f"Game over! The word was: {word_to_guess}")
    sleep(1)
    if input("Do you want to play again? (y/n): ").lower() != "n":
        play_hangman()

play_hangman()
