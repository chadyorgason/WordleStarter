# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():


    def enter_action(s):
        
        guess = ""

        for x in range(N_COLS):
            guess += gw.get_square_letter(N_ROWS-6, x)

        if (guess.lower() in FIVE_LETTER_WORDS):
            gw.show_message("It's a real word. You impress me.")
        else:
            gw.show_message("Not in word list.")

    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)

    ########### Testing
    wordOptions = len(FIVE_LETTER_WORDS)
    randomWord = FIVE_LETTER_WORDS[random.randint(0,wordOptions)].upper()
    print([*randomWord])
    wordOfTheDay = [*randomWord]

    for x in range(N_COLS):
        gw.set_square_letter(N_ROWS - 6, x, wordOfTheDay[x])

    ########### End testing

# Startup code

if __name__ == "__main__":
    wordle()
