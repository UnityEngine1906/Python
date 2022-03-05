import random, sys
import pyttsx3

print('STONE, SCISSORS, PAPER')

wins = 0
loses = 0
ties = 0
speak_engine = pyttsx3.init()

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

while True:
    s.system ('cls')
    speak('WINS ' + str(wins) + ' LOSES ' + str(loses) + ' TIES ' +  str(ties))

    while True:
        speak('(ST)STONE, (SC)SCISSORS, (P)PAPER     search one of them or if you want exit print "exit": ')
        PlayerMove = input()

        if PlayerMove == "Exit" or PlayerMove == "exit":
            exec(open("test123.py").read())

        if PlayerMove == 'ST' or PlayerMove == "SC" or PlayerMove == "P":
            break
        print("(ST)STONE, (SC)SCISSORS, (P)PAPER search one of them: ")

    if PlayerMove == "ST" or PlayerMove == 'st':
        speak("Stone and...")
    if PlayerMove == "SC" or PlayerMove == 'sc':
        speak("Scissors and...")
    if PlayerMove == "P" or PlayerMove == 'p':
        speak("Paper and...")

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMode = "ST"
        speak("Stone")
    if randomNumber == 2:
        computerMode = "SC"
        speak("Scissors")
    if randomNumber == 3:
        computerMode = "P"
        speak("Paper")

    if PlayerMove == computerMode:
        speak("Tie")
        ties += 1
    if PlayerMove == "ST" and computerMode == "SC":
        speak("WoW you WIN")
        wins += 1
    if PlayerMove == "SC" and computerMode == "P":
        speak("WoW you WIN")
        wins += 1
    if PlayerMove == "P" and computerMode == "ST":
        speak("WoW you WIN")
        wins += 1
    if PlayerMove == "SC" and computerMode == "ST":
        speak("Ohh no you LOSE")
        loses += 1
    if PlayerMove == "ST" and computerMode == "P":
        speak("Ohh no you LOSE")
        loses += 1
    if PlayerMove == "P" and computerMode == "SC":
        speak("Ohh no you LOSE")
        loses += 1
