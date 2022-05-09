from tkinter import *
from tkinter import filedialog

dict_app = {'chrome': 'C:\Program Files\Google\Chrome\Application\chrome.exe'}

file_nms = "master/application_names.txt"
file_pths = "master/application_paths.txt"

def read_file():
    file_names = open(file_nms, 'r')
    file_paths = open(file_pths, 'r')
    try:
        name = file_names.readline()
        path = file_paths.readline()
        stripped_name = name.strip()
        stripped_path = path.strip()

        while path:	
            temp_dict = {stripped_name: stripped_path}
            dict_app.update(temp_dict)
            name = file_names.readline()
            path = file_paths.readline()
            stripped_name = name.strip()
            stripped_path = path.strip()
    finally:
        file_paths.close()
        file_names.close()

def add_file(filepath, application_name):
    if filepath != "":
        filen = open(file_nms, 'a+')
        filep = open(file_pths, 'a+')
        with filen as file_names:
            if filen.readline() != "\n":
                file_names.write("\n")
                file_names.write(application_name)
            else:
                file_names.write(application_name)
        with filep as file_paths:
            if filep.readline() != "\n":
                file_paths.write("\n")
                file_paths.write(filepath)
            else:
                file_paths.write(filepath)
        filen.close()
        filep.close()

def openFile(application_name):
    status = check_if_shotcut_name_exists(application_name)
    if application_name == "":
        print("Please provide an application short cut name.")
    elif status == True:
        print("Please provide an application short cut name that doesn't already exist.")
    else:
        filepath = filedialog.askopenfilename(initialdir="C:/", title="Select an executable", filetypes=[("executables", "*.exe")])
        add_file(filepath, application_name)

def check_if_shotcut_name_exists(application_name):
    already_exists = False
    with open(file_nms, 'r') as file:
        for line in file:
            stripped_name = line.strip()
            if stripped_name == application_name:
                already_exists = True
    return already_exists

def editFile(app_name, new_app_name):
    if app_name == "" or new_app_name == "":
        print("Please provide an application short cut name.")
        return
    status1 = check_if_shotcut_name_exists(app_name)
    status2 = check_if_shotcut_name_exists(new_app_name)
    if status1 == False or status2 == True:
        print("Please provide an application short cut name that already exists and one that doesn't exist.")
    else:
        filepath = filedialog.askopenfilename(initialdir="C:/", title="Select an executable", filetypes=[("executables", "*.exe")])
        remove_file(filepath, app_name, new_app_name)

def remove_file(filepath, app_name , new_app_name):
    if filepath != "":
        read_file()
        del dict_app[app_name]

        file_names = open(file_nms, 'w')
        file_paths = open(file_pths, 'w')
        for key, value in dict_app.items():
            file_names.write(key + "\n")
            file_paths.write(value + "\n")
        file_names.write(new_app_name)
        file_paths.write(filepath)
        file_names.close()
        file_paths.close()
