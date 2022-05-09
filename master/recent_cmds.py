from asyncio.windows_events import NULL
from matplotlib.pyplot import title
from numpy import append
from tkinter import *
import jarvisFunctions

cmd_cnvs = None
r_cmd = None

def run_ai_cmd(str):
    for i in cmd_cnvs.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    
    entry_lbl = Label(cmd_cnvs, bg="#caf0f8", wraplength=250)

    if str.split(' ')[0] == "Weather":
        s = str.index('|')
        e = str.index('|', s+1)
        entry_lbl.config(text=jarvisFunctions.tell_weather(str[s+1:e])) #Grabs the 3rd string before the line feed
        entry_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    elif str == "News\n":
        news_str = jarvisFunctions.get_news()
        entry_lbl.config(text=f"Top Storys: \n{news_str[0]}\n\n{news_str[1]}\n\n{news_str[2]}")
        entry_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    elif str.split(' ')[0] == "Topic":
        s = str.index('|')
        e = str.index('|', s+1)
        entry_lbl.config(text=jarvisFunctions.get_topic(str[s+1:e]))
        entry_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    elif str.split(' ')[0] == "Website":
        s = str.index('|')
        e = str.index('|', s+1)
        entry_lbl.config(text=jarvisFunctions.open_website(str[s+1:e]))
        entry_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    elif str == "Date and Time\n":
        entry_lbl.config(text=jarvisFunctions.get_dt())
        entry_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    elif str.split(' ')[0] == "Application":
        s = str.index('|')
        e = str.index('|', s+1)
        entry_lbl.config(text=jarvisFunctions.get_application(str[s+1:e]))
        entry_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)


def read_file(str):
    rd_file = open('master/recent_commands.txt', 'r+') #Read and write in the file.
    file_lines = rd_file.readlines()
    file_length = len(file_lines)

    if file_length < 3: #If the file is empty
        file_lines.append(str) #String list gets the argument.
    else:
        num = file_length - 3 #Ensures that there is less than 4 r_commands
        file_lines.pop(num)
        file_lines.append(str)
    
    rd_file.seek(0)
    rd_file.truncate(0)
    rd_file.writelines(file_lines) #Writes contents of list in txt file.
    
    rd_file.close()

    add_cascade(r_cmd)

def add_cascade(cscd): #cscd meaning cascade.
    txt_file = open('master/recent_commands.txt', 'r')
    file_lines = txt_file.readlines()

    try:
        if cscd.index("end") != None:
            for i in range(0,cscd.index("end") + 1):
                cscd.delete("end")
    except:
        None

    if len(file_lines) == 3: #Only allows for 3 reent commands
        cscd.add_command(label=file_lines[0], command=lambda: run_ai_cmd(file_lines[0]))
        cscd.add_command(label=file_lines[1], command=lambda: run_ai_cmd(file_lines[1]))
        cscd.add_command(label=file_lines[2], command=lambda: run_ai_cmd(file_lines[2]))
    elif len(file_lines) == 2:
        cscd.add_command(label=file_lines[0], command=lambda: run_ai_cmd(file_lines[0]))
        cscd.add_command(label=file_lines[1], command=lambda: run_ai_cmd(file_lines[1]))
    elif len(file_lines) == 1:
        cscd.add_command(label=file_lines[0], command=lambda: run_ai_cmd(file_lines[0]))
