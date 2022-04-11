def read_file(str):
    cmd_queue = []
    read_file = open('recent_commands.txt', 'r')
    x = len(read_file.readlines())
    print(str)
    print(x)