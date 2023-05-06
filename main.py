# importing required modules
import os
import subprocess
import time
import tkinter as Tk
import webbrowser

import customtkinter as CTk
from win10toast import ToastNotifier

from screenSize import ScreenSize

# creating a base window
root = CTk.CTk()
root.title("Inkwell")

# Calculate the size of the screen
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Apply screensize calulations to the GUI
appGeometry = ScreenSize(screenWidth, screenHeight)
root.geometry(appGeometry)

root.configure(bg="Black")

# Create left frame
left_frame = CTk.CTkFrame(root, width=200, fg_color="red")
left_frame.pack(side="left", fill="y")

# Create middle frame
middle_frame = CTk.CTkFrame(root, width=100, fg_color="green")
middle_frame.pack(side="left", expand=True, fill="both")

# Create right frame
right_frame = CTk.CTkFrame(root, width=200, fg_color="blue")
right_frame.pack(side="right", fill="y")


root.mainloop()
