from numpy import append
from tkinter import *

def read_file(str):
    rd_file = open('knudsee/recent_commands.txt', 'r+') #Read and write in the file.
    file_lines = rd_file.readlines()
    file_length = len(file_lines)

    if file_length < 3: #If the file is empty
        file_lines.append(str) #String list gets the argument.
    else:
        num = file_length - 3 #Ensures that there is less than 4 r_commands
        file_lines.pop(num)
        file_lines.append(str)
    
    print(file_lines)
    rd_file.seek(0)
    rd_file.truncate(0)
    rd_file.writelines(file_lines) #Writes contents of list in txt file.
    
    rd_file.close()

def add_cascade(cscd): #cscd meaning cascade.
    txt_file = open('knudsee/recent_commands.txt', 'r')
    file_lines = txt_file.readlines()

    for i in file_lines:
        cscd.add_command(label=i)