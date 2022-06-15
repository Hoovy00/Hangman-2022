import random
from words import word_list

# this function is responsible for picking a word
def get_word():
    word = random.choice(word_list)
    return word.upper()

# this function handles the basic rules of hangman, like how many tries you have
def play_a_game_of_hangman():
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries= 6
    print("Let's play Hangman!")
    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        guessed, tries, word_completion = play_a_round_of_a_game_of_hangman(word, guessed_letters, guessed_words, tries, word_completion)
        if guessed:
            print("Congrats you guessed the word! You win!")
        elif tries == 0:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time")

# this function handles the primaries of guessing and winning and most of the messages displayed in the game
def play_a_round_of_a_game_of_hangman(word, guessed_letters, guessed_words, tries, word_completion):
    guessed = False
    guess = input("Please guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed the letter", guess)
        elif guess not in word:
            print(guess, "is not in the word.")
            tries -=1
            guessed_letters.append(guess)
        else:
            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
    elif len(guess) == len(word) and guess.isalpha():
        if guess in guessed_words:
            print("You already guessed the word", guess)
        elif guess != word:
            print(guess, "is not the word.")
            tries -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_completion = word
    else:
        print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    return guessed, tries, word_completion
        
# this is Kevin, he's about to get hanged and you need to save him.
# This function has the figure that will be displayed to indicate how many tries you have remaining
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
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

#this function handles replæaying the game
def main():
    play_a_game_of_hangman()
    while input("Play again? (Y/N) ").upper() == "Y":
        play_a_game_of_hangman()

if __name__ == "__main__":
    main()
