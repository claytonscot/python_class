__author__ = 'Home'
#Intro to Tkinter and GUI programming
#understanding pieces of the window

from tkinter import *

#create the windown

root = Tk()

#modify root window
root.title("root title")
#sets window dimensions
root.geometry("200x300")

#creates a frame to hold other widgets (a label)
app = Frame(root)
#place app in the grid
app.grid()
#creates the label
label = Label(app, text = "This is a label!")

#creates a button
button1 = Button(app, text = "Click Here")
button1.grid()

#another button. No text
button2 = Button(app)
button2.grid()
button2.configure(text = "This will show text")

#another button.
button3 = Button(app)
button3.grid()

button3["text"] = "This will show as well."

#puts label onto the grid
label.grid()

#kick off the event loop
root.mainloop()

