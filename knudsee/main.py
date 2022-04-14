from unicodedata import name
from struct import pack_into
from tkinter import *
from multiprocessing import Process
import recent_cmds
import jarvisFunctions

def mic_process():
    jarvisFunctions.run_ai()

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
        weather_str = jarvisFunctions.tell_weather(text_inp.get())
        entry_lbl = Label(cmd_canvas, text=weather_str, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 100, window=entry_lbl)

    get_wthr = Button(cmd_canvas, text="Get Weather", command=lambda: get_city(text_inp.get()))
    cmd_canvas.create_window(150, 60, window=get_wthr)
    recent_cmds.read_file("Weather\n")

def web_input():
    print(cmd_canvas.winfo_children())
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    
    text_inp = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 30, window=text_inp)

    def get_website(str):
        if len(cmd_canvas.winfo_children()) == 3:
            cmd_canvas.winfo_children()[2].destroy()
        entry_lbl = Label(cmd_canvas, text="Website: "+str, bg="#caf0f8")
        cmd_canvas.create_window(150, 90, window=entry_lbl)

    get_web = Button(cmd_canvas, text="Get Website", command=lambda: get_website(text_inp.get()))
    cmd_canvas.create_window(150, 60, window=get_web)
    recent_cmds.read_file("Website\n")

def topic_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    
    text_inp = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 30, window=text_inp)

    def get_topic(str):
        if len(cmd_canvas.winfo_children()) == 3:
            cmd_canvas.winfo_children()[2].destroy()
        entry_lbl = Label(cmd_canvas, text="Topic: "+str, bg="#caf0f8")
        cmd_canvas.create_window(150, 90, window=entry_lbl)
    
    get_top = Button(cmd_canvas, text="Get Topic", command=lambda: get_topic(text_inp.get()))
    cmd_canvas.create_window(150, 60, window=get_top)
    recent_cmds.read_file("Topic\n")

def mic_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    
    mic_lbl = Label(cmd_canvas, text="Microphone On", bg="#caf0f8")
    cmd_canvas.create_window(150, 90, window=mic_lbl)

    mic_process_var = Process(target=mic_process())
    mic_process_var.start()
    mic_process_var.join()

    recent_cmds.read_file("Microphone\n")

prog_start_lbl = Label(cmd_canvas, text="Microphone On", bg="#caf0f8")
cmd_canvas.create_window(150, 90, window=prog_start_lbl)

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
#window.state('zoomed') #Choose whether to maximize window or not.

window.mainloop()
