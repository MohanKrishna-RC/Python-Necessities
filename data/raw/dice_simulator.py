"""
What is Tkinter?
Python offers various packages to design the GUI, i.e. the Graphical User Interface. 
Tkinter is the most common, fast, and easy to use Python package used to build Graphical User Interface applications. 
It provides a powerful Object-Oriented Interface and is easy to use. 
Also, you develop an application; you can use it on any platform, 
which reduces the need of amendments required to use an app on Windows, Mac, or Linux.
"""
"""
Tkinter: Imported to use Tkinter and make GUI applications.
Image, Imagetk: Imported from PIL, i.e. Python Imaging Library. We use it to perform operations involving images in our UI.
Random: Imported to generate random numbers.
"""

import tkinter
from PIL import Image, ImageTk
import random

"""
In this step, we will build the main window of our application, where the buttons, labels, and images will reside. 
We also give it a title by title() function.
"""
# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('600x600')
root.title('DataFlair Roll the Dice')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Let's Play!",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
HeadingLabel.pack()

#randomly display the images
# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))


# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget 
ImageLabel.pack( expand=True)

# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()
