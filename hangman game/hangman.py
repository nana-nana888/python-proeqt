import random
from words import word_list  # სიტყვის სიის იმპორტი ცალკე ფაილიდან

# Hangman-ის სურათების ჩვენება
def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
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
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

# შემთხვევითი სიტყვის არჩევა
def get_word():
    return random.choice(word_list).upper()

# თამაშის ლოგიკა
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        # ასოს ან სიტყვის შემოწმება
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters or guess in guessed_words:
                print(f"You already guessed '{guess}'. Try again.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.add(guess)
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.add(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the correct word.")
                tries -= 1
                guessed_words.add(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    # შედეგი
    if guessed:
        print(f"Congrats! You guessed the word '{word}'! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'. Better luck next time!")

# ძირითადი ფუნქცია
def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
