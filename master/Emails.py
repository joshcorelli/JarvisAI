from tkinter import *
import re

emailList = {"1": "joshuacorelli@gmail.com"}

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

file_nums = "master/email_numbers.txt"
file_emails = "master/email_names.txt"

def read_file():
    file_numbers = open(file_nums, 'r')
    file_emails_list = open(file_emails, 'r')
    try:
        num = file_numbers.readline()
        email = file_emails_list.readline()
        stripped_num = num.strip()
        stripped_email = email.strip()

        while email:	
            temp_dict = {stripped_num: stripped_email}
            emailList.update(temp_dict)
            num = file_numbers.readline()
            email = file_emails_list.readline()
            stripped_num = num.strip()
            stripped_email = email.strip()
    finally:
        file_emails_list.close()
        file_numbers.close()

def add_file(email_name):
    filen = open(file_nums, 'a+')
    filee = open(file_emails, 'a+')
    with filen as file_numbers:
        read_file()
        last_line = list(emailList.keys())[-1]
        last_line_int = int(last_line)
        last_line_int = last_line_int + 1
        last_line_string = str(last_line_int)
        if filen.readline() != "\n":
            file_numbers.write("\n")
            file_numbers.write(last_line_string)
        else:
            file_numbers.write(last_line_string)
    with filee as file_emails_list:
        if filee.readline() != "\n":
            file_emails_list.write("\n")
            file_emails_list.write(email_name)
        else:
            file_emails_list.write(email_name)
    filen.close()
    filee.close()

def openEmail(email_name):
    status = check_if_shotcut_name_exists(email_name)
    if email_name == "":
        print("Please provide an email name.")
    elif status == True:
        print("Please provide an email that doesn't already exist.")
    else:
        if(re.fullmatch(regex, email_name)):
            add_file(email_name)
        else:
            print("Invalid email.")

def check_if_shotcut_name_exists(email_name):
    already_exists = False
    with open(file_emails, 'r') as file:
        for line in file:
            stripped_num = line.strip()
            if stripped_num == email_name:
                already_exists = True
    return already_exists

def editEmail(email_number, new_email_name):
    read_file()
    if email_number == "" or new_email_name == "":
            print("Please provide a valid number and a new email name.")
            return
    elif emailList.get(email_number, -1) != -1:
        status2 = check_if_shotcut_name_exists(new_email_name)
        if status2 == True:
            print("Please provide an email name that doesn't already exist.")
        else:
            if(re.fullmatch(regex, new_email_name)):
                remove_file(email_number, new_email_name)
            else:
                print("Invalid new email.")
    else:
        print(emailList.get(email_number, -1))
        print("Please provide a valid number associated with the email you want to edit.")

def remove_file(email_number, new_email_name):
    read_file()
    del emailList[email_number]

    file_numbers = open(file_nums, 'w')
    file_emails_list = open(file_emails, 'w')

    i = 1
    for key, value in emailList.items():
        i_str = str(i)
        file_numbers.write(i_str + "\n")
        file_emails_list.write(value + "\n")
        i_int = int(i_str)
        i = i_int + 1
    i_str = str(i)
    file_numbers.write(i_str)
    file_emails_list.write(new_email_name)
    file_numbers.close()
    file_emails_list.close()