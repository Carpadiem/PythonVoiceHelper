import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import libcommands as libcmd
import pyautogui as pag
import lang_translator as translator
import weather
import mathfuncs as mf


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
    print("u say: " + task)

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

    elif 'добавь команду' in task:
        print('cmd:cancel - отмена операции')
        cmdtype = input("Тип команды: ")  # f-open, b-open
        cmdname = input("Команда: ")
        cmdvalue = input("Значение команды: ")

        if cmdtype == "f-open":
            libcmd.programs.update({cmdname: cmdvalue})

        elif cmdtype == "b-open":
            libcmd.websites.update({cmdname: cmdvalue})

    elif 'удали команду' in task:
        print('cmd:cancel - отмена операции')
        cmdtype = input("Тип команды: ")
        cmdname = input("Команда: ")

        if cmdtype == "f-open":
            libcmd.programs.pop(cmdname)

        elif cmdtype == "b-open":
            libcmd.websites.pop(cmdname)

    elif 'погода' in task:
        cityname = str(task).replace('погода ', '')
        cityname_translated = translator.translate(cityname, 'en')

        print(cityname_translated)

        weather.city = str("https://yandex.ru/pogoda/" + cityname_translated)
        weather.temp_online()
        weather.weather_online()

    elif 'посчитай' in task:
        formattask = str(task).replace('посчитай ', '')

        if 'плюс' in formattask:
            first = formattask[formattask.find('плюс') + 5:]
            second = formattask[0:formattask.find('плюс') - 1]

            format_first = mf.translate(first)
            format_second = mf.translate(second)

            talk("ответ " + str(mf.plus(format_first, format_second)))

    # focus imitation
    for key, value in libcmd.buttons.items():
        if task == key:
            pag.press(value)


while True:
    command(listener())
