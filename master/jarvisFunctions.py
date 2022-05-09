#token = '94bdb0ac9d2f973461c46a3dd2eb0e'

from email.mime import application
from idlist import myGmail, password
import JarvisAI
import re
import pprint
import random
from regex import D
import application
import Emails
import smtplib
import wikipedia

# backend_tts_api='pyttsx3' for different voices options
# backend_tts_api='gtts' for female voice by google text to speech library
obj = JarvisAI.JarvisAssistant(sync=True, token='94bdb0ac9d2f973461c46a3dd2eb0e', disable_msg=False, load_chatbot_model=True,
high_accuracy_chatbot_model=False, chatbot_large=True, backend_tts_api='pyttsx3')

mic_on = True #Flags is the mic is on (True) or off (False)

def t2s(text):
    obj.text2speech(text)

def tell_weather(city_name):
    weather_string = obj.weather(city=city_name)
    return weather_string

def open_website(website_name):
    domain = website_name.split(' ')[-1]
    obj.website_opener(domain)

def get_topic(topic_name):
    wiki_res = tell_me_about(topic_name)
    return wiki_res

def tell_me_about(topic):
    try:
        wikipedia.set_lang("en")
        ny = wikipedia.summary(str(topic), chars=500, auto_suggest=True)
        ny = ny + "..."
        return ny
    except Exception as e:
        print("Exception: ", e)
        return "Topic not found."

def get_news():
    news_obj = obj.news()
    return news_obj

def get_dt():
    date_obj = obj.tell_me_date()
    time_obj = obj.tell_me_time()
    dt_str = "Date: " + date_obj + "\nTime: " + time_obj
    return dt_str

def get_application(application_name):
    application.read_file()
    path = application.dict_app.get(application_name)
    if path is None:
        app_err = "Application path not found"
        return app_err
    else:
        obj.launch_any_app(path_of_app=path)
        return "Opening " + application_name

def send_email(content, subject, to):
    Emails.read_file()
    if to == "":
        return "Please provide a number that corresponds with an email."
    elif content == "":
        return "Please provide content to your email."
    elif subject == "":
        return "Please provide a subject to your email."
    elif Emails.emailList.get(to, -1) != -1:
        email_name = Emails.emailList[to]
        send_mail(email_name, subject, content, myGmail, password)
        return "Email has been sent successfully."
    else:
        return "Invalid number..."

def send_mail(to, subject, content, myGmail, password):
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myGmail, password)
        message = f'Subject: {subject}\n\n{content}'
        mail.sendmail(myGmail, to, message)
        mail.close()
    except Exception as e:
        print(e)

def run_ai():
    while mic_on:
        res = obj.mic_input()

        if re.search('weather|temperature', res):
            city = res.split('in ')[-1]
            weather_res = obj.weather(city=city)
            print(weather_res)
            t2s(weather_res)

        if re.search('send email', res):
            try:
                Emails.read_file()
                
                response = "Subject to your email!"
                print(response)
                t2s(response)
                res = obj.mic_input()
                subject = res

                response = "What should I say?"
                print(response)
                t2s(response)
                res = obj.mic_input()
                content = res

                response = "Who would you like to send this email to. Please provide the number that corresponds to the name:"
                print(response)
                t2s(response)
                i = 1
                for x in Emails.emailList:
                    print(i, end = ': ')
                    print(Emails.emailList[x])
                    i+=1

                res = obj.mic_input()
                if Emails.emailList.get(to, -1) != -1:
                    to = Emails.emailList[res]
                    send_mail(to, subject, content, myGmail, password)

                    response = "Email has been sent successfully."
                    print(response)
                    t2s(response)
                else:
                    response = "Invalid number..."
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
            wiki_res = tell_me_about(topic)
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
            app = res.split(' ', 1)[1]
            application.read_file()
            path = application.dict_app.get(app)
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
            I can open websites for you, launch application and more."""
            print(ans)
            pprint.pprint(li_commands)
            t2s(ans)
            
        if re.search('stop|break|exit|kill', res):
            print("I cant believe you've done this...")
            t2s("I cant believe you've done this...")
            break