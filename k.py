# import the time module
from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
#creating a window
window = Tk()
window.geometry('600x600')#giving size
window.title('PythonGeeks')#giving title
head=Label(window, text="Countdown Clock and Timer", font=('Calibri 15'))# a label
head.pack(pady=20)