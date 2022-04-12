from unicodedata import name
import JarvisAI
import re
import pprint
import random
from struct import pack_into
from tkinter import *
import recent_cmds

# Main
window = Tk()

m_bar = Menu(window) #Add menu ontop of the window
window.config(menu=m_bar) #Includes the menu bar

cmd_canvas = Canvas(window, bg="#caf0f8", width=300, height=400)
cmd_canvas.grid(sticky=W)

# Function Declarations
def weather_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    text_inp = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 30, window=text_inp)

    def get_city(str):
        if len(cmd_canvas.winfo_children()) == 3:
            cmd_canvas.winfo_children()[2].destroy()
        entry_lbl = Label(cmd_canvas, text="City: "+str, bg="#caf0f8")
        cmd_canvas.create_window(150, 90, window=entry_lbl)

    get_wthr = Button(cmd_canvas, text="Get Weather", command=lambda: get_city(text_inp.get()))
    cmd_canvas.create_window(150, 60, window=get_wthr)
    recent_cmds.read_file("Weather\n")

def web_input():
    print(cmd_canvas.winfo_children())
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    recent_cmds.read_file("Website\n")

def topic_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    recent_cmds.read_file("Topic\n")

def mic_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    recent_cmds.read_file("Microphone\n")

cmds = Menu(m_bar, tearoff=0)
m_bar.add_cascade(label="Menu", menu=cmds) #Adds list of commands, name Menu
cmds.add_command(label="Weather", command=weather_input)
cmds.add_command(label="Open Website", command=web_input)
cmds.add_command(label="Topic", command=topic_input)
cmds.add_command(label="Microphone", command=mic_input)
cmds.add_separator()
cmds.add_command(label="Exit", command=quit)

r_cmds = Menu(m_bar, tearoff=0)
m_bar.add_cascade(label="Recent Commands",menu=r_cmds) #Adds list of commands, name Recent Commands
recent_cmds.add_cascade(r_cmds)

window.title('Jarvis AI Capstone')
window.geometry("600x400")
window.state('zoomed')

window.mainloop()