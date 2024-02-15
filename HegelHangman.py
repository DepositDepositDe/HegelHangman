import random

def choose_word():
    """
    Function to choose a random word from a predefined list.
    """
    words = ["dialectic", "geist", "absolute", "synthesis", "thesis", "antithesis", "world-spirit", "phenomenology", "sublation", "concrete universal", "master-slave dialectic", "ethical life", "spirit", "reason", "freedom", "alienation", "self-consciousness", "will", "recognition", "ethics", "art", "religion", "history", "logic", "philosophy"]
    return random.choice(words)

def display_hangman(incorrect_guesses):
    """
    Function to display the Hangman drawing based on the number of incorrect guesses.
    """
    stages = [  # Hangman stages
        """
        --------
        |      |
        |      
        |    
        |    
        |    
        -
        """,
        """
        --------
        |      |
        |      O
        |    
        |    
        |    
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |    
        |    
        -
        """,
        """
        --------
        |      |
        |      O
        |     /|
        |    
        |    
        -
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |    
        |    
        -
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     / 
        |    
        -
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     / \\
        |    
        -
        """
    ]
    # Ensure that the incorrect_guesses value does not exceed the length of stages list
    index = min(incorrect_guesses, len(stages) - 1)
    return stages[index]

def display_word(word, guessed_letters):
    """
    Function to display the word with underscores for unguessed letters.
    """
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    """
    Main function to run the Hangman game.
    """
    print("Welcome to Hegel's Hangman!")
    play_again = True
    while play_again:
        word_to_guess = choose_word()
        guessed_letters = []
        incorrect_guesses = 0
        max_attempts = len(display_hangman(0)) - 1
        incorrect_guess_list = []

        while incorrect_guesses < max_attempts:
            print(display_hangman(incorrect_guesses))
            print(display_word(word_to_guess, guessed_letters))
            guess = input("Make a dialectical synthesis by guessing a letter: ").lower()

            if guess in guessed_letters:
                print("The spirit of repetition pervades you! You've already guessed that letter!")
            elif guess in word_to_guess:
                print("The dialectic unfolds! Correct guess!")
                guessed_letters.append(guess)
                if display_word(word_to_guess, guessed_letters) == word_to_guess:
                    print("The Absolute is realized! Congratulations! You've revealed the word:", word_to_guess)
                    break
            else:
                print("The negation persists! Incorrect guess!")
                guessed_letters.append(guess)
                incorrect_guesses += 1
                incorrect_guess_list.append(guess)

            if incorrect_guesses == max_attempts:
                print(display_hangman(incorrect_guesses))
                print("The dialectical process has reached its limit! The word was:", word_to_guess)
                break

        play_again_input = input("Would you like to play again? (yes/no): ").lower()
        if play_again_input != "yes":
            play_again = False

    print("Thank you for playing Hegel's Hangman!")

if __name__ == "__main__":
    hangman()


# fix ending screen