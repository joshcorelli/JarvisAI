from numpy import append

def read_file(str):
    read_file = open('knudsee/recent_commands.txt', 'r+') #Read and write in the file.
    file_lines = read_file.readlines()
    file_length = len(file_lines)

    if file_length < 3: #If the file is empty
        file_lines.append(str) #String list gets the argument.
    else:
        num = file_length - 3 #Ensures that there is less than 4 r_commands
        file_lines.pop(num)
        file_lines.append(str)
    
    print(file_lines)
    read_file.seek(0)
    read_file.truncate(0)
    read_file.writelines(file_lines) #Writes contents of list in txt file.
    
    read_file.close()