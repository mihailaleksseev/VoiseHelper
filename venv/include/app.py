import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print (words)
    os.system("say " + words)


talk("Ask me")


def command():
    r = sr.Recognizer()

    with sr.Microphone as source:
        print ("I need command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            task = r.recognize_google(audio).lower()
            print ("You say " + command)
        except sr.UnknownValueError:
            talk("I cant understand you")
            task = command()

        return task


def make_task(task):
    if 'oen website' in task:
        talk("already opening")
        url = 'https://pypi.org/project/gTTS/'
        webbrowser.open(url)
    elif 'stop' in task:
        talk("already stopping")
        sys.exit()


while True:
    make_task(command())
