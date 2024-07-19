# version 0.1.0

import random

def get_word():
    words = ['Apple', 'Bread', 'Chair', 'Dance', 'Eagle', 'Fruit', 'Grape', 'House', 'Ivory', 'Jelly', 
    'Knife', 'Lemon', 'Mango', 'Night', 'Ocean', 'Peach', 'Queen', 'River', 'Stone', 'Tiger', 
    'Union', 'Vivid', 'Whale', 'Xenon', 'Yield', 'Zebra', 'Blaze', 'Crane', 'Dream', 'Flame', 
    'Globe', 'Haven', 'Jolly', 'Kneel', 'Lunar', 'Mirth', 'Noble', 'Orbit', 'Piano', 'Quilt', 
    'Raven', 'Shine', 'Thorn', 'Unity', 'Valor', 'Waltz', 'Xylog', 'Yacht', 'Zealot', 'Animal',
    'Banana', 'Castle', 'Dragon', 'Energy', 'Flower', 'Garden', 'Heaven', 'Island', 'Jungle',
    'Kitten', 'Laptop', 'Monkey', 'Nature', 'Orange', 'Planet', 'Quiver', 'Rocket', 
    'Sunset', 'Tunnel', 'Umbrella', 'Victory', 'Whisper', 'Xylophone', 'Yellow', 'Zephyr', 
    'Beacon', 'Canyon', 'Desert', 'Empire', 'Forest', 'Galaxy', 'Harbor', 'Insect', 'Jigsaw', 
    'Knight', 'Lantern', 'Mystic', 'Nectar', 'Oracle', 'Pirate', 'Quasar', 'Rescue', 'Savage', 
    'Trophy', 'Utopia', 'Voyage', 'Wander', 'Xenial', 'Yonder', 'Zephyr', 'Adventure', 'Butterfly',
    'Chocolate', 'Dinosaur', 'Elephant', 'Fireworks', 'Grapefruit', 'Happiness', 'Important', 'Jasmine',
    'Kangaroo', 'Lighthouse', 'Mountain', 'Notebook', 'Orchestra', 'Pineapple', 'Question', 'Rainbow',
    'Sunshine', 'Universe', 'Vacation', 'Wonderful', 'Xenophobia', 'Youthful', 'Zoologist', 'Beautiful',
    'Champion', 'Delicious', 'Enchanted', 'Fantastic', 'Glamorous', 'Harmonize', 'Incredible', 'Joyfulness',
    'Knowledge', 'Legendary', 'Magnificent', 'Nostalgia', 'Optimistic', 'Phenomenal', 'Quintuple', 'Radiation', 
    'Spectacle', 'Triumphant', 'Unstoppable', 'Vibrantly', 'Whimsical', 'Xenophile', 'Yearning', 
    'Zealously']
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
            print("You already guessed that letter. Try a different one. ")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            if set(word_to_guess) <= guessed_letters:
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            guessed_letters.add(guess)
            tries += 1
            display_hangman(tries)

        if tries == max_tries:
            print(f"Game over! The word was: {word_to_guess}")

play_hangman()

