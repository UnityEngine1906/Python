import webbrowser
import subprocess
import time
import datetime
import speech_recognition as sr
import pyttsx3
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

speak_engine = pyttsx3.init()
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
time = ['time', 'daytime', 'what time is it', 'Time']
chrome = ['home', 'hrome', 'chrome', 'Home', 'Hrome', 'Chrome', 'open home', 'open hrome', 'open chrome']
youtube = ['open YouTube', 'Youtube']
weatherMassiv = ['weather', 'say weather', 'Weather']
OsmanAbi = ['Osman abi ne yapıyor']
game = ['Play with me','Play with me please','Open game','Can we play','game','GameE']

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def Listen():
    with m as source:
        print("say")
        global audio
        audio = r.listen(source)
    global voice
    voice = r.recognize_google(audio, language = "en-EN")

Listen()

for timeAll in time:
    if voice == timeAll:
        now = datetime.datetime.now()
        speak("Now is " + str(now.hour) + ':' + str(now.minute))
        exec(open("test123.py").read())
for cromeAll in chrome:
        if voice == cromeAll:
            subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
            exec(open("test123.py").read())

for youtubeAll in youtube:
        if voice  == youtubeAll:
            webbrowser.open('https://youtube.com/')
            exec(open("test123.py").read())

for wetherAll in weatherMassiv:
        if voice  == wetherAll:
            place = input('City: ')
            country = input('Country: ')
            country_and_place = place + ', ' + country

            owm = OWM('ff7201ac02383373de8de4035fd0f395')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(country_and_place)
            w = observation.weather

            status = w.detailed_status
            w.wind()
            humidity = w.humidity
            temp = w.temperature('celsius')['temp']

            def weather():
                speak('in ' + str(place) + ' now ' + str(status))
                speak('temperature: ' + str(round(temp)) + ' degrees Celsius')


            weather()
            exec(open("test123.py").read())

for OsmanAll in OsmanAbi:
    if voice == OsmanAll:
        speak("ubudiyet-i külliyede ve tefekkür-ü ilahi bahrine müstağrak")

        exec(open("test123.py").read())

for GameAll in game:
    if voice == GameAll:
        exec(open("StoneScissorsPaper.py").read())

#print(voice)
