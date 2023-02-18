import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

audio = sr.Recognizer()
engine = pyttsx3.init()
wikipedia.set_lang('pt')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('Sou sua assistente virtual, como posso lhe ajudar?')

with sr.Microphone() as source:
    voice = audio.listen(source)
    commandFromVoice = audio.recognize_google(voice, language='pt-BR')
    command = commandFromVoice.lower()
    if 'horas' in command:
        speak('São ' + str(datetime.datetime.now().hour) +
              ' horas e ' + str(datetime.datetime.now().minute) + ' minutos.')
    if 'procurar por' in command:
        speak('Pesquisando...')
        command = command.replace('procurar por', '')
        result = wikipedia.summary(command, sentences=2)
        speak(result)
