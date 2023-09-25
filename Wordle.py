# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from tkinter import *

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

#guesses = [0,0,0,0,0,0]



class Guesses():
    def __init__(self):
        # Games won with 1 guess, 2 guesses... and the last position is losses
        self.iGuesses = [0,0,0,0,0,0,0]

    def update_guesses(self, results):
        self.iGuesses[results] += 1
        
        return self.iGuesses
    
class Colors():
    def __init__(self):
        # Games won with 1 guess, 2 guesses... and the last position is losses
        self.CORRECT_COLOR = "#66BB66"       # Light green for correct letters
        self.PRESENT_COLOR = "#CCBB66"       # Brownish yellow for misplaced letters
        self.MISSING_COLOR = "#999999"       # Gray for letters that don't appear
        self.UNKNOWN_COLOR = "#FFFFFF"

    def update_colors(self):
        self.CORRECT_COLOR = "#66BB66"       # Light green for correct letters
        self.PRESENT_COLOR = "#89CFF0"       # Brownish yellow for misplaced letters
        self.MISSING_COLOR = "#999999"       # Gray for letters that don't appear
        self.UNKNOWN_COLOR = "#FFFFFF"

    def update_colors2(self):
        self.CORRECT_COLOR = "#B4C540"       # Light green for correct letters
        self.PRESENT_COLOR = "#3686C9"       # Brownish yellow for misplaced letters
        self.MISSING_COLOR = "#E0E2D2"       # Gray for letters that don't appear
        self.UNKNOWN_COLOR = "#FFFFFF"
            
colors = Colors()

class Word():
    def __init__(self):
        # Games won with 1 guess, 2 guesses... and the last position is losses
        ########### Choosing a random word and showing it on the last line
        wordOptions = len(FIVE_LETTER_WORDS)
        randomWord = FIVE_LETTER_WORDS[random.randint(0,wordOptions)].upper()
        print([*randomWord])
        wordOfTheDay = [*randomWord]
        self.currentWord = randomWord
        self.currentLetters = wordOfTheDay

    def update_word(self):
        ########### Choosing a random word and showing it on the last line
        wordOptions = len(FIVE_LETTER_WORDS)
        randomWord = FIVE_LETTER_WORDS[random.randint(0,wordOptions)].upper()
        print([*randomWord])
        wordOfTheDay = [*randomWord]
        self.currentWord = randomWord
        self.currentLetters = wordOfTheDay
        print(self.currentLetters)
        print(self.currentWord)

class ColorWindow(Frame):
    "A GUI application with three button"

    def _init_(self, master):
        self.master = master

    def choose_color(self):
        
        msg1 = Message(self.master, text = "Which color scheme do you want?")  
        msg1.pack()
        print("first print window")
        print(self.master)

        btn1 = Button(self.master, text = "Traditional", command = self.traditional)
        btn1.pack()
        btn2 = Button(self.master, text = "Color Blind Friendly", command = self.color_blind)
        btn2.pack()
        btn3 = Button(self.master, text = "Tropics", command = self.tropics)
        btn3.pack()
    
    def color_blind(self):
        colors.update_colors()
        msg1 = Message(self.master, text = "Close the window and enjoy the colors!")  
        msg1.pack()

    def tropics(self):
        colors.update_colors2()
        msg1 = Message(self.master, text = "Close the window and enjoy the colors!")  
        msg1.pack()

    def traditional(self):
        msg1 = Message(self.master, text = "Close the window and enjoy the colors!")  
        msg1.pack()

root = Tk()
root.title("Color Scheme")
root.geometry("400x250")
app1 = ColorWindow(root)
#call the method
app1.choose_color()
root.mainloop()

def wordle():
    stats = Guesses()
    word = Word()
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
                    if guessArray[x] == word.currentLetters[x]:
                        correctBoxes.append(x)

                for x in range(len(correctBoxes)):
                    gw.set_square_color(gw.get_current_row(), correctBoxes[x], colors.CORRECT_COLOR)

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
                    yellowCheck.append(word.currentLetters[presentBoxes[x]])
                print(yellowCheck)
                print(guessArray)

                for x in range(len(yellowCheck)):
                    if guessArray[presentBoxes[x]] in yellowCheck:
                        gw.set_square_color(gw.get_current_row(), presentBoxes[x], colors.PRESENT_COLOR)
                        yellowCheck.pop(yellowCheck.index(guessArray[presentBoxes[x]]))
                    ####### Checks for all MISSING positions and sets them grey
                    else:
                        gw.set_square_color(gw.get_current_row(), presentBoxes[x], colors.MISSING_COLOR)
                print(yellowCheck)


                ######### If you win
                if guess == word.currentWord:
                    gw.show_message("Well done. Scrumptious.")
                    win = stats.update_guesses(gw.get_current_row())
                    print(win)

                    #stats window
                    root = Tk()
                    root.title("Well Done!")
                    root.geometry("400x500")
                    app = Application(root)
                    #call the method
                    app.create_widgets()
                    root.mainloop()

                ######### If you lose or guesses run out
                else:
                    if gw.get_current_row() > 4:
                        gw.show_message("You lose ha.")
                        stats.update_guesses(6)

                        #stats window
                        root = Tk()
                        root.title("Game Over :(")
                        root.geometry("400x500")
                        app = Application(root)
                        #call the method
                        app.create_widgets()
                        root.mainloop()

                    else:
                        gw.show_message("Try again buffoon.")
                        #gw.show_message(stats)
                        gw.set_current_row(gw.get_current_row() + 1)
                        

            
            else:
                gw.show_message("Not in word list.")

        else:
            gw.show_message("Out of guesses!!")

    

    
    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)

    def playAgain():
        endRow = gw.get_current_row() + 1
        gw.set_current_row(0)
        gw.show_message("")
        for x in range(endRow):
            for y in range(N_COLS):
                gw.set_square_letter(x,y,"")
                gw.set_square_color(x,y,"#FFFFFF")

        word.update_word()
    
    ########### Button test
    class Application(Frame):
        "A GUI application with three button"

        def _init_(self, master):
            self.master = master


        def create_widgets(self):
            #Create first button
            def _sum(arr):
                sum = 0
                for i in arr:
                    sum = sum + i
                return(sum)
            
            guess1 = "\nGames won with 1 Guess: " + str(stats.iGuesses[0])
            guess2 = "\nGames won with 2 Guesses: " + str(stats.iGuesses[1])
            guess3 = "\nGames won with 3 Guesses: " + str(stats.iGuesses[2])
            guess4 = "\nGames won with 4 Guesses: " + str(stats.iGuesses[3])
            guess5 = "\nGames won with 5 Guesses: " + str(stats.iGuesses[4])
            guess6 = "\nGames won with 6 Guesses: " + str(stats.iGuesses[5])
            losses = "\nTotal losses: " + str(stats.iGuesses[6])
            games = [guess1,guess2,guess3,guess4,guess5,guess6,losses]
            inputStats = ""

            for x in range(7):
                if stats.iGuesses[x] > 0 or x == 6:
                    inputStats += (games[x])


            gamesPlayed = _sum(stats.iGuesses)
            msg1 = Message(self.master, text = "Stats:" + "\n\nGames Played: " + str(gamesPlayed) + inputStats + "\n\nPlay Again?")  
            msg1.pack()

            btn1 = Button(self.master, text = "Yes", command = self.prompt)
            btn1.pack()
            btn2 = Button(self.master, text = "No", command = self.master.destroy)
            btn2.pack()

        def prompt(self):
            msg1 = Message(self.master, text = "Close this window and play again!")
            msg1.pack()
            playAgain()

        
            
            # root = Tk()
            # root.title("Play Again")
            # root.geometry("300x200")
            # app = Application(root)
            # #call the method
            # app.prompt()
            # root.mainloop()

        


            #Create second button
            # btn2 = Button(self.master, text = "T do nothing as well")
            # btn2.pack()

            # #Create third button
            # btn3=Button(self.master, text = "I do nothing as well as well")
            # btn3.pack()

    

    ########### Display correct word in last row
    # for x in range(N_COLS):
    #     gw.set_square_letter(N_ROWS - 1, x, wordOfTheDay[x])

# Startup code

if __name__ == "__main__":
    wordle()
