import pyttsx3
engine=pyttsx3.init()
while True:
    engine.say(input("Type For Computer to Read:"))
    engine.runAndWait()