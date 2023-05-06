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

# root.configure(bg="Black")

tabControl = CTk.CTkTabview(root)
tabControl.grid()
tab1 = Tk.Frame(tabControl)
tab1.grid()
tab2 = Tk.Frame(tabControl)


tabControl.add("Home")
tabControl.add("Editor")


frame_top = CTk.CTkFrame(tab1, fg_color="aquamarine", height=100)
frame_top.grid()

frame_left = CTk.CTkFrame(tab1, fg_color="red", width=200)
frame_left.grid()

frame_middle = CTk.CTkFrame(tab1, fg_color="green")

frame_top_inside = CTk.CTkFrame(frame_middle, fg_color="orange", height=50)
frame_top_inside.grid()

frame_middle.grid()

frame_right = CTk.CTkFrame(tab1, fg_color="blue", width=200)
frame_right.grid()


root.mainloop()
