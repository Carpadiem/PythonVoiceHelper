import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import libcommands as libcmd
import pyautogui as pag


def talk(words):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(words)
    engine.runAndWait()


def listener():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk("Говорите")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()

    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = listener()

    return task


def command(task):

    # open-system
    if 'сайт' in task:
        for key, value in libcmd.websites.items():
            if task == key:
                talk('выполнено')
                webbrowser.open(value)

    elif 'файл' in task:
        for key, value, in libcmd.programs.items():
            if task == key:
                talk('выполнено')
                os.startfile(value)

    # focus imitation
    for key, value in libcmd.buttons.items():
        if task == key:
            pag.press(value)


while True:
    command(listener())
