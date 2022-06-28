import random
from words import word_list


def choose_answer():
    '''this function picks a answer from word_list and returns it to the caller in uppercase, for example, it picks "stable" and gives the system "STABLE"'''
    correct_answer = random.choice(word_list)
    return correct_answer.upper()

def play_a_game_of_hangman():
    '''this function handles the basic rules of hangman, like how many tries you have'''
    correct_answer = choose_answer()
    revealed_letters = "_" * len(correct_answer)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries= 6
    print("Let's play Hangman!")
    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(revealed_letters)
        print("\n")
        guessed, tries, revealed_letters = play_a_round_of_a_game_of_hangman(correct_answer, guessed_letters, guessed_words, tries, revealed_letters)
    if guessed:
        print("Congrats you guessed the word! You win!")
    else:
        assert tries == 0
        print("Sorry, you ran out of tries. The word was " + correct_answer + ". Maybe next time")

def play_a_round_of_a_game_of_hangman(correct_answer, guessed_letters, guessed_words, tries, revealed_letters):
    '''this function handles the primaries of guessing and winning and most of the messages displayed in the game'''
    guessed = False
    guess = input("Please guess a letter or word: ").upper()
    guessed_a_letter = len(guess) == 1 and guess.isalpha()
    guessed_a_valid_word = len(guess) == len(correct_answer) and guess.isalpha()
    if guessed_a_letter:
    
        
        if guess in guessed_letters:
            print("You already guessed the letter", guess)
        
        elif guess not in correct_answer:
            print(guess, "is not in the word.")
            tries -=1
            guessed_letters.append(guess)
        
        else:
            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(revealed_letters)
            indices = [i for i, letter in enumerate(correct_answer) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            revealed_letters = "".join(word_as_list)
            if "_" not in revealed_letters:
                guessed = True
    
    elif guessed_a_valid_word:
    
        if guess in guessed_words:
            print("You already guessed the word", guess)
    
        elif guess != correct_answer:
            print(guess, "is not the word.")
            tries -= 1
            guessed_words.append(guess)
    
        else:
            guessed = True
            revealed_letters = correct_answer
    
    else:
        print("Not a valid guess.")
        print(display_hangman(tries))
        print(revealed_letters)
        print("\n")
    
    return guessed, tries, revealed_letters
        
def display_hangman(tries):
    '''this is Kevin, he's about to get hanged and you need to save him.
    This function has the figure that will be displayed to indicate how many tries you have remaining'''
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

def main():
    '''this function handles replaying the game'''
    play_a_game_of_hangman()
    while input("Play again? (Y/N) ").upper() == "Y":
        play_a_game_of_hangman()

if __name__ == "__main__":
    main()
