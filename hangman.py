import random

def select_random_word():
    words = ['python', 'programming', 'hangman', 'challenge', 'openai', 'developer', 'algorithm']
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
        ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
        ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
        ---
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |      
        ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
        ---
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        ---
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        ---
        """
    ]
    return stages[tries]

def hangman_game():
    print("Welcome to Hangman!")
    word = select_random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print("Word: ", word_completion)
        print(f"Tries left: {tries}")
        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Invalid input. Please enter a single letter.")

    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you lost. The word was: {word}")

if __name__ == "__main__":
    hangman_game()