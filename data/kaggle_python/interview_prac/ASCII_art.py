# Program to display ASCII text in ASCII art fonts

#pyfiglet package taes ASCII text and displays it in ASCII art fonts
# Many ASCII art fonts are avilable.

import pyfiglet

userText = input("Enter Some text : ")

#figlet_format() convert ASCII text into ASCII fonts

ascii_art  = pyfiglet.figlet_format(text = userText)

print("\n FONT -DEFAULT")

print(ascii_art)

ascii_art = pyfiglet.figlet_format(text=userText, font="slant")

print("\n FONT -- SLANT")

print(ascii_art)

ascii_art = pyfiglet.figlet_format(text=userText, font="digital")

print("\n FONT - DIGITAL")

print(ascii_art)
