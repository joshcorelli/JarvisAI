#token = '94bdb0ac9d2f973461c46a3dd2eb0e'

from idlist import myGmail, password
from Emails import emailList
import JarvisAI
import re
import pprint
import random
from regex import D

isSendingEmail = False

# backend_tts_api='pyttsx3' for different voices options
# backend_tts_api='gtts' for female voice by google text to speech library
obj = JarvisAI.JarvisAssistant(sync=True, token='94bdb0ac9d2f973461c46a3dd2eb0e', disable_msg=False, load_chatbot_model=True,
high_accuracy_chatbot_model=False, chatbot_large=True, backend_tts_api='pyttsx3')

def t2s(text):
    obj.text2speech(text)

while True:
    res = obj.mic_input()
    isSendingEmail = False

    if re.search('weather|temperature', res):
        city = res.split('in ')[-1]
        weather_res = obj.weather(city=city)
        print(weather_res)
        t2s(weather_res)

    if re.search('send email', res):
        try:
            isSendingEmail = True
            response = "What should I say?"
            print(response)
            t2s(response)
            res = obj.mic_input()
            content = res

            response = "Subject to your email!"
            print(response)
            t2s(response)
            res = obj.mic_input()
            subject = res

            response = "Who would you like to send this email to. Please provide the number that corresponds to the name:"
            print(response)
            t2s(response)
            i = 1
            for x in emailList:
                print(i, end = ': ')
                print(emailList[x])
                i+=1

            res = obj.mic_input()
            try:
                # if res != int:
                #     pass
                to = emailList[res]
            except Exception as e:
                print(e)
                response = "Invalid number..."
                print(response)
                t2s(response)

            obj.send_mail(to, subject, content, myGmail, password)

            response = "Email has been sent successfully."
            print(response)
            t2s(response)
        except Exception as e:
            print(e)
            response = "Unable to send the email"
            print(response)
            t2s(response)
            
    if re.search('news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        t2s(news_res[0])
        t2s(news_res[1])

    if re.search('tell me about', res):
        topic = res.split(' ')[-1]
        wiki_res = obj.tell_me(topic)
        print(wiki_res)
        t2s(wiki_res)

    if re.search('date', res):
        date = obj.tell_me_date()
        print(date)
        print(t2s(date))

    if re.search('time', res):
        time = obj.tell_me_time()
        print(time)
        t2s(time)

    if re.search('open', res):
        domain = res.split(' ')[-1]
        open_result = obj.website_opener(domain)
        print(open_result)

    if re.search('launch', res):
        dict_app = {
            'chrome': 'C:\Program Files\Google\Chrome\Application\chrome.exe',
            'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe',
            # 'notepad': '%windir%\system32\\notepad.exe',
            # 'snipping tool': '%windir%\system32\SnippingTool.exe'
            # 'discord': 'C:\Users\joshu\AppData\Local\Discord\Update.exe --processStart Discord.exe'
        }
        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            print('Application path not found')
        else:
            t2s('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)

    if re.search('hello|hi|hey', res):
        print('Hi')
        t2s('Hi')

    if re.search('how are you', res):
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print(f"I am {response}")
        t2s(f"I am {response}")

    if re.search('your name|who are you', res):
        print("My name is Jarvis, I am your personal assistant")
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
        pprint.pprint(li_commands)
        t2s(ans)
        
    if re.search('stop|break|exit|kill', res):
        print("I cant believe you've done this...")
        t2s("I cant believe you've done this...")
        break