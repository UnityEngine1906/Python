import pyttsx3
import speech_recognition as sr
import os
import time
from fuzzywuzzy import fuzz
import datetime

#phrases
opts = {
    'alias': ('Houston',"Houd", 'HoundStone'),
    'tbr': ('Say','Tell','Say me','Tell me','Tell me please','Say me please','Say please','Tell please','What','Whats','How','turn on','',),
    'cmds': {
        'ctime': ("time is it","time it is","time"),
        'radio': ("the radio","the radio please","radio","radio please",),
        'stupid':("The Joke","A Joke","Joke",)
    }
}

#Functions

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "en-EN").lower()
        print('[log] Recognized ' + voice)

        if voice.startswith(opts['alias']):

            #Appeal to Houston
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            #Recognition and execution of commands
            cmd = recognize_cmd(cmd)
            excute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] I don't understand you! Please try again later!")
    except sr.RequestError as e:
        print("[log] Unknown Error! Please try again!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def excute_cmd(cmd):
    if cmd == 'ctime':
        #time
        now = datetime.datetime.now()
        speak("Now is " + str(now.hour) + ':' + str(now.minute))

    elif cmd == "stupid":
        #Joke
        speak("My creater is dont know normal Jokes... Ha-Ha-Ha!")
    elif cmd == "radio":
        #Radio
        speak("My creater is dont like radio...")

    else:
        #Command not recognized
        speak("I only can say you time hehe")


#Start
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')

speak('Hi')
speak('Houston in touch')

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)
