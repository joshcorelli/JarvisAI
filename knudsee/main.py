import JarvisAI
import re
import pprint
import random
from struct import pack_into
from tkinter import *

# Function Declarations
def weather_input():
    print("State weather")

def web_input():
    print("State website")

def topic_input():
    print("State topic")

def mic_input():
    print("Ask me anything!")

# Main
window = Tk()

m_bar = Menu(window)
window.config(menu=m_bar)

cmds = Menu(m_bar,tearoff=0)
m_bar.add_cascade(label="Menu", menu="cmds")
cmds.add_command(label="Weather", command=weather_input)
cmds.add_command(label="Open Website", command=web_input)
cmds.add_command(label="Topic", command=topic_input)
cmds.add_command(label="Microphone", command=mic_input)
cmds.add_separator
cmds.add_command(label="Exit", command=quit)

r_cmds = Menu(m_bar,tearoff=0)
m_bar.add_cascade(label="Recent Commands",menu="r_cmds")

window.geometry("700x500")
window.state('zoomed')

window.mainloop()