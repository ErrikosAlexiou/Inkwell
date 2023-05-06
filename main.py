# importing required modules
import os
import subprocess
import time
import tkinter as Tk
import webbrowser
from tkinter import ttk

import customtkinter as CTk
from win10toast import ToastNotifier

from screenSize import ScreenSize

# creating a base window
root = Tk.Tk()

root.title("Inkwell")


# Calculate the size of the screen
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Apply screensize calulations to the GUI
appGeometry = ScreenSize(screenWidth, screenHeight, 0.8, 0.8)
root.geometry(appGeometry)

root.configure(bg="Black")

tabControl = CTk.CTkTabview(root)
tabControl.pack(expand=1, fill="both")

tab1 = Tk.Frame(tabControl)
tab2 = Tk.Frame(tabControl)
tabControl.add("Home")
tabControl.add("Editor")

leftFrame = CTk.CTkFrame(
    tabControl.tab("Editor"), fg_color="red", width=100, height=100
)
leftFrame.grid(column=0, row=0)

middleFrame = CTk.CTkFrame(
    tabControl.tab("Editor"), fg_color="green", width=100, height=90
)
middleFrame.grid(column=1, row=0)

middleBottomBar = CTk.CTkFrame(
    tabControl.tab("Editor"), fg_color="white", width=100, height=10
)
middleBottomBar.grid(column=1, row=1)

rightFrame = CTk.CTkFrame(
    tabControl.tab("Editor"), fg_color="blue", width=100, height=100
)
rightFrame.grid(column=2, row=0)


root.mainloop()
