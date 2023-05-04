# importing required modules
from tkinter import *
import customtkinter
from win10toast import ToastNotifier
import subprocess
import webbrowser
import time
import os

from screenSize import ScreenSize

# creating a base window
root = Tk()
root.title("Inkwell")

# Calculate the size of the screen
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Apply screensize calulations to the GUI
appGeometry = ScreenSize(screenWidth, screenHeight)
root.geometry(appGeometry)

root.configure(bg="Black")


root.mainloop()
