# Equation to Image

## Description
Utility for creating Latex-based equations and copying them rapidly to the clipboard. Useful for Evernote.

## Run

1. run sublime text 3; save a file to \tmp\equation.md
2. ctrl + shift + p: opens sublime text 3 command prompt
3. select "Insert Equation as Image"
4. type the equation using latex commands and see a preview
5. when finished, press enter and save the file \temp\equation.md
6. to get the image of the equation, run python equation_to_image.py, which will copy the image to the clipboard.
7. to get the latex, run python get_eqn.py, which will copy the latex code to the clipboard.