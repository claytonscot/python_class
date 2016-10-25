__author__ = 'Home'
#Object Oriented GUI programming
#use a class with Tkinter

from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons"""

    def __init__(self, master):
        #initialize the frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.button_clicks = 0 #counts number of button clicks

    def create_widgets(self):
        """Create button displaying nUmber of clicks"""

        #create first button
        self.button1 = Button(self)
        self.button1["text"] = "Total Clicks: 0"
        self.button1["command"] = self.update_count
        self.button1.grid()

        self.button2 = Button(self)
        self.button2
        self.button2["text"] = "Double Clicks: 0"
        self.button2["command"] = self.update_count
        self.button2.grid()

    def update_count(self):
        """Increase click-count and display total"""
        self.button_clicks += 1
        self.button1["text"] = "Total Clicks: " + str(self.button_clicks)
        self.button2["text"] = "Double Clicks: " + (str(self.button_clicks * 2))

root = Tk()
root.title("Easy Buttons")
root.geometry("900x600")

app = Application(root)

root.mainloop()