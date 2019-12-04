import tkinter as tk
import easygui
import pandas as pd
from time import strftime
# import tkinter_flight_scraper_bot
# from tkinter_flight_scraper_bot import Flight_Bot
def caps_from(event):
    """ Forces the input FROM to be upper case and less than 4 characters """
    from_city1.set(from_city.get().upper())
    if len(from_city1.get()) >3: from_city1.set(from_city.get()[:3])

def caps_to(event):
    """ Forces the input To to be the upper case and less than 4 characters """
    from_city1.set(from_city1.get().upper())
    if len(from_city1.get())>3: from_city1.set(from_city1.get()[:3])

def close_app():
    window.destroy()

def run_app():
    print('run')



window = tk.Tk()
""" Return a new Toplevel widget on screen SCREENNAME. A new Tcl interpreter will be created. 
BASENAME will be used for the identification of the profile file (see readprofile). It is constructed from sys.argv[0] without extensions if None is given. 
CLASSNAME is the name of the widget class. """

window.title("FLIGHT SCRAPER")
#window.geometry("600x600") # size of the window when it opens
#window.minsize(width=600, height=600) # you can define the minimum size of the window like this

window.resizable(width="false", height="false") # change to false if you want to prevent resizing

""" Every tkinter app needs to be structured this way. We call the tk.Tk() to create the app window,
and we then build our app and place the widgets (frames, buttons, labels etc.) when we want before "compiling" everything with window.mainloop(). """

# three frames on top of each other
frame_header = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)
frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

# label header to be placed in the frame_header
header = tk.Label(frame_header, text = "FLIGHT SCRAPER TOOL", bg='grey', fg='black', height='3', width='50', font=("Helvetica 16 bold"))
# inside the grid of frame_header, place it in the position 0,0
header.grid(row=0, column=0)

""" The above code should always be before mainloop() """

# two additional frames go inside the center_frame
frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief='sunken')

# and populate them with the labels referring to the inputs we want from the user
from_city = tk.Label(frame_main_1, text = "FROM: ")
to_city = tk.Label(frame_main_2, text = "TO:      ")
departure_date = tk.Label(frame_main_1, text = "    DEPARTURE DATE:")
return_date = tk.Label(frame_main_2, text = "     RETURN DATE:")

# Put it simply: StringVar() allows you to easily track tkinter variables and see if they were read, changed, etc
# check resources here for more details: http://effbot.org/tkinterbook/variable.htm
from_city1 = tk.StringVar()
to_city1 = tk.StringVar()
departure_date1 = tk.StringVar()
return_date1 = tk.StringVar()

# this part is just to display the labels inside the center frame
# the order which we pack the items is important
frame_main_1.pack(fill='x', pady=2)
frame_main_2.pack(fill='x',pady=2)
from_city.pack(side='left')
departure_date.pack(side='left', padx=5)
to_city.pack(side='left')
return_date.pack(side='right', padx=5)

# a proper app needs some buttons too!
button_run = tk.Button(bottom_frame, text="Start", command=run_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_run.grid(column=0, row=0, sticky='w', padx=100, pady=2)

button_close = tk.Button(bottom_frame, text="Exit", command=close_app, bg='dark red', fg='white', relief='raised', width=10, font=('Helvetica 9'))
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)

window.mainloop()

""" def run_app():
    print('getting user inputs')
    user_city_from = str(from_city_entry.get())
    user_city_to = str(to_city_entry.get())
    user_date_depart = str(departure_date_entry.get())
    user_date_return = str(return_date_entry.get())
    
    print('starting Chrome')
    bot = Flight_Bot()
    bot.start_kayak(user_city_from, user_city_to, user_date_depart, user_date_return)
 """