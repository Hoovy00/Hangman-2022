import random
from words import word_list

class GameOfHangman(object):
    def __init__(self):
        self.guessed = False
        self.correct_answer = GameOfHangman.choose_answer()
        self.revealed_letters = "_" * len(self.correct_answer)
        self.guessed_letters = []
        self.guessed_words = []
        self.tries = 6

    def play(self):
        '''this function handles the basic rules of hangman, like how many tries you have'''
        print("Let's play Hangman!")
        while not self.guessed and self.tries > 0:
            print(self.display_hangman())
            print(self.revealed_letters)
            print("\n")
            self.play_a_round()
        if self.guessed:
            print("Congrats you guessed the word! You win!")
        else:
            assert self.tries == 0
            print("Sorry, you ran out of tries. The word was " + self.correct_answer + ". Maybe next time")

    def play_a_round(self):
        '''this function handles the primaries of guessing and winning and most of the messages displayed in the game'''
        self.guessed = False
        guess = input("Please guess a letter or word: ").upper()
        guessed_a_letter = len(guess) == 1 and guess.isalpha()
        guessed_a_valid_word = len(guess) == len(self.correct_answer) and guess.isalpha()
        if guessed_a_letter:
        
            
            if guess in self.guessed_letters:
                print("You already guessed the letter", guess)
            
            elif guess not in self.correct_answer:
                print(guess, "is not in the word.")
                self.tries -=1
                self.guessed_letters.append(guess)
            
            else:
                print("Good job,", guess, "is in the word!")
                self.guessed_letters.append(guess)
                word_as_list = list(revealed_letters)
                indices = [i for i, letter in enumerate(self.correct_answer) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                revealed_letters = "".join(word_as_list)
                if "_" not in revealed_letters:
                    guessed = True
        
        elif guessed_a_valid_word:
        
            if guess in self.guessed_words:
                print("You already guessed the word", guess)
        
            elif guess != self.correct_answer:
                print(guess, "is not the word.")
                self.tries -= 1
                self.guessed_words.append(guess)
        
            else:
                guessed = True
                revealed_letters = self.correct_answer
        
        else:
            print("Not a valid guess.")
            print(self.display_hangman())
            print(revealed_letters)
            print("\n")

    @staticmethod        
    def choose_answer():
        '''this function picks a answer from word_list and returns it to the caller in uppercase, for example, it picks "stable" and gives the system "STABLE"'''
        correct_answer = random.choice(word_list)
        return correct_answer.upper()    
        
    def display_hangman(self):
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
        return stages[self.tries]

def main():
    '''this function handles replaying the game'''
    game = GameOfHangman()
    game.play()
    while input("Play again? (Y/N) ").upper() == "Y":
        game.play()

if __name__ == "__main__":
    main()
