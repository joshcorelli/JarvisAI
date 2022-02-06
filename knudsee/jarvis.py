#import jarvis
from struct import pack_into
from tkinter import *

#Window Configurations
window = Tk()
window.title("Jarvis AI Capstone Project")
window.geometry('500x500')
window['background']='#BEE3DB'
#menuPhoto = PhotoImage(file = "put path here");

#Labels
testLabel = Label(window, text="Welcome to Eian Knudsen's and Joshua Corelli's capstone project!\nAsk me anything.", bg='#89B0AE')
testLabel.place(x=300, y=0)
#Menu Button
menuButton = Button(window, text="Menu", borderwidth=0, bg = '#BEE3DB', activebackground='#89B0AE', width=10, height = 5)
menuButton.place(x=0, y=0)

#Panel of button functions
menuCanvas = Canvas(window, borderwidth=0, width=200, height=500)
menuCanvas.place(x=77, y=0)

#Buttons for the menu panel
button1 = Button(menuCanvas, text="See Weather", borderwidth=0,width=20, height = 3)
button1.pack()
button2 = Button(menuCanvas, text="Open Website", borderwidth=0, width=20, height = 3)
button2.pack()
button3 = Button(menuCanvas, text="Open Application", borderwidth=0, width=20, height = 3)
button3.pack()
button4 = Button(menuCanvas, text="Explain Topic", borderwidth=0, width=20, height = 3)
button4.pack()
button5 = Button(menuCanvas, text="Send E-mail", borderwidth=0, width=20, height = 3)
button5.pack()

#Loops through window as program runs
window.mainloop()