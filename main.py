"""
File: word_guess.py
-------------------
This program is a game where you have to guess the chosen word by giving the programs
the letter you think might be in the secret word. You are given 8 lives or guesses, which
means that if you were to guess incorrectly, one point of your guess pool would be taken.
If you get to 0 points, the game ends and you lose.
If you guessed correctly, the letter you guessed will be displayed at the place where it is
supposed to be.
If your guess is a letter that you have already guessed before, and doesn't repeat itself in
the word, no lives will be taken and your progress will remain the same.
Changing the Lexicon is easy, you just have to change a variable at the beginning of a program,
allowing the user to choose their own word list to guess from.

Thank you Chris, Mehran and Brahm for teaching me everything I used in this program, thank you
for the amazing classes and pop culture references. I enjoyed Code in Place and decided to start
my journey to learn more about programming. 
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    This function takes in a secret word, makes a version of it in which
    all letters are replaced by dashes and updates the dash version based on
    the letters from the secret word that you have guessed
    """
    dash_word = create_dash_word(secret_word)
    guess_left = INITIAL_GUESSES

    while True:
        if dash_word == secret_word:
            print("Congratulations, the word is: " + secret_word)
            break
        if guess_left == 0:
            print("Sorry, you lost. The secret word was: " + secret_word)
            break
        print("The word now looks like this:", dash_word)
        print("You have", guess_left, "guesses left")
        guess = input("Type a single letter here, then press enter: ")
        if len(guess)>1:
            guess = input("Type a single letter here, then press enter: ")
        if guess.upper() in secret_word:
            print("The guess is correct")
            dash_word = add_letter(guess, dash_word, secret_word)
        else:
            print("There are no", guess + "'s in the word")
            guess_left -= 1

def add_letter(guess, dash_word, secret_word):
    '''
    This function takes in the guessed letter if it was right
    and adds it to the dash version of the word. I used a list in order to keep
    track of the position of each letter and easily replace them since strings are
    immutable, but lists aren't. This function takes in the dash word, turns it into a list
    updates the guessed letter where it is supposed to go and replaces it, then it returns the
    updated dash word.
    '''
    guess = guess.upper()
    dash_word = list(dash_word)
    for i in range(len(secret_word)):
        if dash_word[i] == guess:
            continue
        if secret_word[i] == guess:
            dash_word[i] = guess
            break
    dash_word = "".join(dash_word)
    return dash_word

def create_dash_word(secret_word):
    '''
    Creates a string with as many dashes as letters
    the secret word had and returns it
    '''
    dash_word = ""
    len_sw = len(secret_word)
    for i in range(len_sw):
        dash_word += "-"
    return dash_word


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  It takes words from the file LEXICON_FILE
    defined as a constant at the beginning of the program and turns each
    word into elements of a list. A random word from the list is chosen
    and returned.
    """
    word_dic = []
    with open(LEXICON_FILE) as f:
        for line in f:
            word_dic.append(line.strip())
    word = random.choice(word_dic)
    return word




def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
