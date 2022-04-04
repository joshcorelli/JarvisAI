import JarvisAI
import re
import pprint
import random
from struct import pack_into
from tkinter import *

obj = JarvisAI.JarvisAssistant(sync=True, token='94bdb0ac9d2f973461c46a3dd2eb0e', disable_msg=False, load_chatbot_model=True,
high_accuracy_chatbot_model=False, chatbot_large=True, backend_tts_api='pyttsx3')

isMicOn=True
show=True

def t2s(text):
    obj.text2speech(text)

def micOn():
    isMicOn=True

    while isMicOn:
        res = obj.mic_input()

        if re.search('weather|temperature', res):
            city = res.split(' ')[-1]
            weather_res = obj.weather(city=city)
            testLabel.config(text=weather_res)
            print(weather_res)
            t2s(weather_res)

        if re.search('news', res):
            news_res = obj.news()
            pprint.pprint(news_res)
            testLabel.config(text=news_res[0]+"\n"+news_res[1])
            t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
            t2s(news_res[0])
            t2s(news_res[1])

        if re.search('tell me about', res):
            topic = res.split(' ')[-1]
            wiki_res = obj.tell_me(topic)
            print(wiki_res)
            testLabel.config(text=wiki_res)
            t2s(wiki_res)

        if re.search('date', res):
            date = obj.tell_me_date()
            print(date)
            testLabel.config(text=date)
            print(t2s(date))

        if re.search('time', res):
            time = obj.tell_me_time()
            print(time)
            testLabel.config(text=time)
            t2s(time)

        if re.search('open', res):
            domain = res.split(' ')[-1]
            open_result = obj.website_opener(domain)
            print(open_result)

        if re.search('launch', res):
            dict_app = {
                'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
            }

            app = res.split(' ', 1)[1]
            path = dict_app.get(app)
            if path is None:
                t2s('Application path not found')
                print('Application path not found')
            else:
                t2s('Launching: ' + app)
                obj.launch_any_app(path_of_app=path)

        if re.search('hello', res):
            print('Hi')
            t2s('Hi')

        if re.search('how are you', res):
            li = ['good', 'fine', 'great']
            response = random.choice(li)
            print(f"I am {response}")
            t2s(f"I am {response}")

        if re.search('your name|who are you', res):
            print("My name is Jarvis, I am your personal assistant")
            testLabel.config(text="My name is Jarvis, I am your personal assistant")
            t2s("My name is Jarvis, I am your personal assistant")

        if re.search('what can you do', res):
            li_commands = {
                "open websites": "Example: 'open youtube.com",
                "time": "Example: 'what time it is?'",
                "date": "Example: 'what date it is?'",
                "launch applications": "Example: 'launch chrome'",
                "tell me": "Example: 'tell me about India'",
                "weather": "Example: 'what weather/temperature in Mumbai?'",
                "news": "Example: 'news for today' ",
            }
            ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
            I can open websites for you, launch application and more. See the list of commands-"""
            print(ans)
            testLabel.config(text=ans)
            pprint.pprint(li_commands)
            t2s(ans)
            
        if re.search('stop|break|exit|kill', res):
            testLabel.config(text="I can't believe you've done this...")
            print("I cant believe you've done this...")
            t2s("I cant believe you've done this...")
            isMicOn=False
            break
    return

def micOff():
    isMicOn=False
    return

def menu_show():
    global show
    if show:
        menuCanvas.itemconfig(1, state='normal')
        show=False
    else:
        menuCanvas.itemconfig(1, state='disabled')
        show=True

#Window Configurations
window = Tk()
window.title("Jarvis AI Capstone Project")
window.geometry('500x500')
window['background']='#BEE3DB'
#menuPhoto = PhotoImage(file = "put path here");

#Labels
testLabel = Label(window, text="Capstone: Eian Knudsen & Joshua Corelli", bg='#89B0AE')
testLabel.place(x=300, y=0)
#Menu Button
menuButton = Button(window, text="Menu", command=menu_show, borderwidth=0, bg = '#BEE3DB', activebackground='#89B0AE', width=10, height = 5)
menuButton.place(x=0, y=0)

#Panel of button functions
menuCanvas = Canvas(window, borderwidth=0, width=200, height=500, state='disabled')
menuCanvas.place(x=77, y=0)

#Buttons for the menu panel
button1 = Button(menuCanvas, text="See Weather", borderwidth=0,width=20, height = 3)
button1.pack()
text_input = Text(window, height=5, width=20)
text_input.pack()
button2 = Button(menuCanvas, text="Open Website", borderwidth=0, width=20, height = 3)
button2.pack()
button3 = Button(menuCanvas, text="Open Application", borderwidth=0, width=20, height = 3)
button3.pack()
button4 = Button(menuCanvas, text="Explain Topic", borderwidth=0, width=20, height = 3)
button4.pack()
button5 = Button(menuCanvas, text="Send E-mail", borderwidth=0, width=20, height = 3)
button5.pack()
button6 = Button(menuCanvas, text="Microphone Input", command=micOn, borderwidth=0, width=20, height = 3)
button6.pack()
button7 = Button(menuCanvas, text="Button Input", command=micOff, borderwidth=0, width=20, height = 3)
button7.pack()

#Loops through window as program runs
window.mainloop()