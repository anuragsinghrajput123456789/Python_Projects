Spell Checker App

A small Python project that fixes spelling errors in user input.
It uses the pyspellchecker library to detect wrong words and replace them with the most probable correction.

Features

Corrects spelling in a full sentence

Shows each correction in the terminal

Handles missing suggestions safely

Loops until you type exit

Fast and easy to use

Requirements

Install the pyspellchecker library:

pip install pyspellchecker

How to Run

Save the script as spellCheck.py

Open a terminal in the project folder

Run:

python spellCheck.py

Type any sentence

Type exit to close the program

Code Overview

correct_text() splits input into words and corrects them

Handles cases where no suggestion exists

Prints corrections in real time

Returns the corrected sentence

Example

Input:

I hav a spel cheker progrm

Output:

Correcting hav to have
Correcting spel to spell
Correcting cheker to checker
Correcting progrm to program

Corrected Text: I have spell checker program

Project Structure
SpellChecker/
│── spellCheck.py
│── README.md

Notes

Works offline

Good for practice projects

Easy to extend with GUI or file support
