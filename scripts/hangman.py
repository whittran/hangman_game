import random;
from word import categories


def display_word(word, guessed_letters, incorrect_guesses):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    display += "\n\nGuessed letters: " + ", ".join(guessed_letters)
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
    print("Choose a category:")
    for index, category in enumerate(categories.keys(), start=1):
        print(f"{index}. {category}")
    choice = int(input("Enter the number of your choice: ")) - 1
    category = list(categories.keys())[choice]

    word = random.choice(categories[category])
    guessed_letters = []
    incorrect_guesses = []
    attempts = 6

    while True:
        print("Word:", display_word(word, guessed_letters, incorrect_guesses))
        print(display_hangman(6 - attempts))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a single letter.")
            continue

        if guess in guessed_letters:
            print("\nYou've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("\nCorrect!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("\nIncorrect!")
            attempts -= 1
            if attempts == 0:
                print("Sorry, you're out of attempts. The word was:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes" :
        hangman()
    else:
        print("Thanks for playing!")

hangman()
