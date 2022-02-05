#import jarvis
from tkinter import *

window = Tk()

#Creating Label
testLabel = Label(window, text="Hello world! This is a test GUI.")

#Puts label onto the window
testLabel.pack()

#Loops through window realtime
window.mainloop()