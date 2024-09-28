#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
import os

# Constants to store the notes on a guitar neck tuned in EADGBE
NOTES_E_CORD = ["E", "F", "F# / Gb", "G", "G# / Ab", "A", "A# / Bb", "B", "C", "C# / Db", "D", "D#/Eb", "E"]
NOTES_B_CORD = ["B", "C", "C# / Db", "D", "D#/Eb", "E", "F", "F# / Gb", "G", "G# / Ab", "A", "A# / Bb", "B"]
NOTES_G_CORD = ["G", "G# / Ab", "A", "A# / Bb", "B", "C", "C# / Db", "D", "D#/Eb", "E", "F", "F# / Gb", "G"]
NOTES_D_CORD = ["D", "D#/Eb", "E", "F", "F# / Gb", "G", "G# / Ab", "A", "A# / Bb", "B", "C", "C# / Db", "D"]
NOTES_A_CORD = ["A", "A# / Bb", "B", "C", "C# / Db", "D", "D#/Eb", "E", "F", "F# / Gb", "G", "G# / Ab", "A"]

NOTES = [NOTES_E_CORD, NOTES_B_CORD, NOTES_G_CORD, NOTES_D_CORD, NOTES_A_CORD, NOTES_E_CORD]

# Function to print the guitar neck and other informations
def print_guitar_neck():
    # Clean the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the guitar neck
    print("                                GUITAR NECK                               ")
    print("--------------------------------------------------------------------------")
    # Cords
    for i in range (1,7):
        print("0", end = "")
        # Cases/columns
        for j in range(1,13):
            print("|-",i,"{:02d}".format(j),"-", end = "", sep = "")
        print("|")
    print("--------------------------------------------------------------------------")
    # Print case/column number
    for k in range(1,13):
        print("   ",k,"  ", end = "", sep = "")
    print("\nRespond 666 to exit the program.")

# Function to get the corresponding note to the input number
def getNote(noteNumber):
    # First digit related to cord number
    cord = int(str(noteNumber)[0:1])
    # Second and third digits related to column number
    column = int(str(noteNumber)[1:3])
    # Use of try/except because the input number can be out of the guitar neck
    try:
        note = NOTES[cord-1][column]
    except:
        note = "Note not registred (not on the guitar neck)!"
    return note

# Init user response to 0
userResponse = 0

# Loop until the user send 666 (exit)
while (int(userResponse) != 666):
    print_guitar_neck()
    userResponse = input("\nEnter a value (note position) to get the note's name: ")
    # Try/except because try to case string to int
    try:
        userResponse = int(userResponse)
        # Exit asked by the user
        if (userResponse == 666):
            break
        # Three digit required for the getNote function (in this first version of this program)
        if (userResponse >= 100 and userResponse <= 999):
            print("The corresponding note is :", getNote(userResponse))
        else:
            print("Note not registred (not on the guitar neck)!")
    except:
        print("ERROR: number is required.")
        userResponse = 0
    finally:
        if (userResponse == 666):
            print("You choose to exit the program! See you soon!")
            break
        input("(Press ENTER to continue)")
