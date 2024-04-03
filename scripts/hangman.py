import random;
from word import word_list


def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    
           |    
           |    
           |    
        ------
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
        ------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |    
        ------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        ------
        """
    ]
    return stages[attempts]

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print(display_hangman(6 - attempts))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect!")
            attempts -= 1
            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

hangman()






