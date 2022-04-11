import JarvisAI
import re
import pprint
import random
from struct import pack_into
from tkinter import *
import recent_cmds

# Function Declarations
def weather_input():
    recent_cmds.read_file("Weather\n")

def web_input():
    recent_cmds.read_file("Website\n")

def topic_input():
    recent_cmds.read_file("Topic\n")

def mic_input():
    recent_cmds.read_file("Microphone\n")

# Main
def main():
    window = Tk()

    m_bar = Menu(window) #Add menu ontop of the window
    window.config(menu=m_bar) #Includes the menu bar

    cmds = Menu(m_bar, tearoff=0)
    m_bar.add_cascade(label="Menu", menu=cmds) #Adds list of commands, name Menu
    cmds.add_command(label="Weather", command=weather_input)
    cmds.add_command(label="Open Website", command=web_input)
    cmds.add_command(label="Topic", command=topic_input)
    cmds.add_command(label="Microphone", command=mic_input)
    cmds.add_separator
    cmds.add_command(label="Exit", command=quit)

    r_cmds = Menu(m_bar, tearoff=0)
    m_bar.add_cascade(label="Recent Commands",menu=r_cmds) #Adds list of commands, name Recent Commands

    window.geometry("700x500")
    window.state('zoomed')

    window.mainloop()

if __name__ == "__main__":
    main()