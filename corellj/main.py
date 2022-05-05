from unicodedata import name
from struct import pack_into
from tkinter import *
import threading
import recent_cmds
import jarvisFunctions
import obj_reader
from application import openFile, editFile, file_nms
from Emails import file_emails, openEmail

# Main
window = Tk()

m_bar = Menu(window) #Add menu ontop of the window
window.config(menu=m_bar) #Includes the menu bar

cmd_canvas = Canvas(window, bg="#caf0f8", width=300, height=400) #For command inputs
cmd_canvas.grid(sticky=W)
m_canvas = obj_reader.frame(window, width=300, height=400) #For 3D Models
m_canvas.place(x=300, y=0)
m_canvas.animate = 1
m_canvas.after(100, m_canvas.printContext)

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
        jarvisFunctions.open_website(text_inp.get())
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
        topic_str = jarvisFunctions.get_topic(text_inp.get())
        entry_lbl = Label(cmd_canvas, text=topic_str, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 200, window=entry_lbl)
    
    get_top = Button(cmd_canvas, text="Get Topic", command=lambda: get_topic(text_inp.get()))
    cmd_canvas.create_window(150, 60, window=get_top)
    recent_cmds.read_file("Topic\n")

def news_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()

    news_str = jarvisFunctions.get_news()
    entry_lbl = Label(cmd_canvas, text="Top Story: "+news_str, bg="#caf0f8", wraplength=250)
    cmd_canvas.create_window(150, 150, window=entry_lbl)

    recent_cmds.read_file("Topic\n")

def d_and_t():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()

    dt_str = jarvisFunctions.get_dt()
    entry_lbl = Label(cmd_canvas, text=dt_str, bg="#caf0f8", wraplength=250)
    cmd_canvas.create_window(150, 150, window=entry_lbl)

    recent_cmds.read_file("Topic\n")

def application():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()

    text_inp = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 30, window=text_inp) 

    def get_application(str):
        app_status = ""
        app_status = jarvisFunctions.get_application(text_inp.get().lower())
        entry_lbl = Label(cmd_canvas, text=app_status, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 150, window=entry_lbl)
        text_inp.delete(0, END)

    def add_edit_app():
        for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
            i.destroy()

        text_inp1 = Entry(cmd_canvas)
        cmd_canvas.create_window(150, 30, window=text_inp1)

        addApp = Button(cmd_canvas, text="Add application", command=lambda: openFile(text_inp1.get().lower()))
        cmd_canvas.create_window(150, 100, window=addApp)
        add_err = "Please provide an application short cut name that doesn't already exist."
        entry_lbl1 = Label(cmd_canvas, text=add_err, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 60, window=entry_lbl1)
        text_inp1.delete(0, END)

        text_inp2 = Entry(cmd_canvas)
        cmd_canvas.create_window(150, 160, window=text_inp2)

        text_inp3 = Entry(cmd_canvas)
        cmd_canvas.create_window(150, 220, window=text_inp3)

        editApp = Button(cmd_canvas, text="Edit application", command=lambda: editFile(text_inp2.get().lower(), text_inp3.get().lower()))
        cmd_canvas.create_window(150, 290, window=editApp)
        edit_err1 = "Please provide the application short cut name that you want to edit."
        entry_lbl2 = Label(cmd_canvas, text=edit_err1, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 190, window=entry_lbl2)
        text_inp2.delete(0, END)
        text_inp3.delete(0, END)

        edit_err2 = "Please provide the new application short cut name."
        entry_lbl3 = Label(cmd_canvas, text=edit_err2, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 250, window=entry_lbl3)
    
    get_app = Button(cmd_canvas, text="Launch application", command=lambda: get_application(text_inp.get().lower()))
    cmd_canvas.create_window(150, 60, window=get_app)
    addEd = Button(cmd_canvas, text="Add/Edit application", command=lambda: add_edit_app())
    cmd_canvas.create_window(150, 100, window=addEd)
    recent_cmds.read_file("Application\n")

    scrollbar = Scrollbar(cmd_canvas)
    mylist = Listbox(cmd_canvas, yscrollcommand = scrollbar.set)
    cmd_canvas.create_window(150, 250, window=mylist)
    with open(file_nms, 'r') as file:
        lines = file.readlines()
        for line in lines: 
            mylist.insert(END, line)
    
    scrollbar.config( command = mylist.yview )

def email():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()

    text_inp1 = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 30, window=text_inp1)
    edit_err1 = "Please provide the content of the email."
    entry_lbl1 = Label(cmd_canvas, text=edit_err1, bg="#caf0f8", wraplength=250)
    cmd_canvas.create_window(150, 50, window=entry_lbl1)

    text_inp2 = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 70, window=text_inp2)
    edit_err2 = "Please provide the subject of the email."
    entry_lbl2 = Label(cmd_canvas, text=edit_err2, bg="#caf0f8", wraplength=250)
    cmd_canvas.create_window(150, 90, window=entry_lbl2)

    text_inp3 = Entry(cmd_canvas)
    cmd_canvas.create_window(150, 110, window=text_inp3)
    edit_err3 = "Please provide the number associated with the email below to who the email will be sent to."
    entry_lbl3 = Label(cmd_canvas, text=edit_err3, bg="#caf0f8", wraplength=250)
    cmd_canvas.create_window(150, 140, window=entry_lbl3)

    def get_email(content, subject, to):
        app_status = ""
        app_status = jarvisFunctions.send_email(text_inp1.get(), text_inp2.get(), text_inp3.get().lower())
        entry_lbl = Label(cmd_canvas, text=app_status, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 240, window=entry_lbl)
        text_inp1.delete(0, END)
        text_inp2.delete(0, END)
        text_inp3.delete(0, END)

    def add_edit_email():
        for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
            i.destroy()

        text_inp1 = Entry(cmd_canvas)
        cmd_canvas.create_window(150, 30, window=text_inp1)

        addApp = Button(cmd_canvas, text="Add email", command=lambda: openEmail(text_inp1.get().lower()))
        cmd_canvas.create_window(150, 100, window=addApp)
        add_err = "Please provide a valid email name that doesn't already exist."
        entry_lbl1 = Label(cmd_canvas, text=add_err, bg="#caf0f8", wraplength=250)
        cmd_canvas.create_window(150, 60, window=entry_lbl1)
        text_inp1.delete(0, END)

        # text_inp2 = Entry(cmd_canvas)
        # cmd_canvas.create_window(150, 160, window=text_inp2)

        # text_inp3 = Entry(cmd_canvas)
        # cmd_canvas.create_window(150, 220, window=text_inp3)

        # editApp = Button(cmd_canvas, text="Edit email", command=lambda: editFile(text_inp2.get().lower(), text_inp3.get().lower()))
        # cmd_canvas.create_window(150, 290, window=editApp)
        # edit_err1 = "Please provide the application short cut name that you want to edit."
        # entry_lbl2 = Label(cmd_canvas, text=edit_err1, bg="#caf0f8", wraplength=250)
        # cmd_canvas.create_window(150, 190, window=entry_lbl2)
        # text_inp2.delete(0, END)
        # text_inp3.delete(0, END)

        # edit_err2 = "Please provide the new application short cut name."
        # entry_lbl3 = Label(cmd_canvas, text=edit_err2, bg="#caf0f8", wraplength=250)
        # cmd_canvas.create_window(150, 280, window=entry_lbl3)

    send_eml = Button(cmd_canvas, text="Send email", command=lambda: get_email(text_inp1.get(), text_inp2.get(), text_inp3.get().lower()))
    cmd_canvas.create_window(150, 170, window=send_eml)
    add_email = Button(cmd_canvas, text="Add/Edit email", command=lambda: add_edit_email())
    cmd_canvas.create_window(150, 200, window=add_email)
    recent_cmds.read_file("Email\n")

    scrollbar = Scrollbar(cmd_canvas)
    mylist = Listbox(cmd_canvas, yscrollcommand = scrollbar.set)
    cmd_canvas.create_window(150, 350, window=mylist)
    # file_nums, file_emails
    i = 1
    with open(file_emails, 'r') as fe:
        email_lines = fe.readlines()
        for line in email_lines: 
            mylist.insert(END, str(i) + ": " + line)
            i += 1
    
    scrollbar.config( command = mylist.yview )

def mic_input():
    for i in cmd_canvas.winfo_children(): #Destroy widgets in current frame to be replaced
        i.destroy()
    
    mic_lbl = Label(cmd_canvas, text="Microphone On", bg="#caf0f8")
    cmd_canvas.create_window(150, 90, window=mic_lbl)

    mic_process_var = threading.Thread(target=jarvisFunctions.run_ai())
    mic_process_var.start()
    #mic_process_var.join()

    recent_cmds.read_file("Microphone\n")

prog_start_lbl = Label(cmd_canvas, text="Microphone On", bg="#caf0f8")
cmd_canvas.create_window(150, 90, window=prog_start_lbl)

cmds = Menu(m_bar, tearoff=0)
m_bar.add_cascade(label="Menu", menu=cmds) #Adds list of commands, name Menu
cmds.add_command(label="Weather", command=weather_input)
cmds.add_command(label="Open Website", command=web_input)
cmds.add_command(label="Topic", command=topic_input)
cmds.add_command(label="Application", command=application)
cmds.add_command(label="Email", command=email)
cmds.add_command(label="News", command=news_input)
cmds.add_command(label="Date/Time", command=d_and_t)
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
m_canvas.mainloop()
