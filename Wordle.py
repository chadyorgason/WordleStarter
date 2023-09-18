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
        ######### Checks if they still have guesses left
        if gw.get_current_row() <= 5:
            guess = ""
            ######### Check if word is in word list
            for x in range(N_COLS):
                guess += gw.get_square_letter(gw.get_current_row(), x)

            if (guess.lower() in FIVE_LETTER_WORDS):
                gw.show_message("It's a real word. You impress me.")
                print("It's a real word. You impress me.")
            
                ######### Checks for all CORRECT positions and sets them green
                guessArray = [*guess]
                correctBoxes = []

                for x in range(len(guessArray)):
                    if guessArray[x] == wordOfTheDay[x]:
                        correctBoxes.append(x)

                for x in range(len(correctBoxes)):
                    gw.set_square_color(gw.get_current_row(), correctBoxes[x], "#66BB66")

                ######### Checks for all PRESENT positions and sets them yellow
                print(correctBoxes)
                presentBoxes = []
                yellowCheck = []

                for x in range(len(guessArray)):
                    if x in correctBoxes:
                        you = "cool"
                    else:
                        presentBoxes.append(x)

                print(presentBoxes)
                for x in range(len(presentBoxes)):
                    yellowCheck.append(wordOfTheDay[presentBoxes[x]])
                print(yellowCheck)
                print(guessArray)

                for x in range(len(yellowCheck)):
                    if guessArray[presentBoxes[x]] in yellowCheck:
                        gw.set_square_color(gw.get_current_row(), presentBoxes[x], "#CCBB66")
                        yellowCheck.pop(yellowCheck.index(guessArray[presentBoxes[x]]))
                    ####### Checks for all MISSING positions and sets them grey
                    else:
                        gw.set_square_color(gw.get_current_row(), presentBoxes[x], "#999999")
                print(yellowCheck)


                ######### If you win
                if guess == randomWord:
                    gw.show_message("Well done. Treat yourself to some well earned spoils.")

                ######### If you lose or guesses run out
                else:
                    if gw.get_current_row() > 4:
                        gw.show_message("You lose ha.")
                    else:
                        gw.show_message("Try again buffoon.")
                        gw.set_current_row(gw.get_current_row() + 1)
            
            else:
                gw.show_message("Not in word list.")

        else:
            gw.show_message("Out of guesses!!")

            

    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)

    ########### Choosing a random word and showing it on the last line
    wordOptions = len(FIVE_LETTER_WORDS)
    randomWord = FIVE_LETTER_WORDS[random.randint(0,wordOptions)].upper()
    print([*randomWord])
    wordOfTheDay = [*randomWord]

    for x in range(N_COLS):
        gw.set_square_letter(N_ROWS - 1, x, wordOfTheDay[x])

# Startup code

if __name__ == "__main__":
    wordle()
