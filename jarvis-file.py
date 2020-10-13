"""
Author  - Saurabh Pal
Date    - 17 Sept., 2020
Purpose - Python Project for learning

"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser # for opening web browser
import os
import random
import smtplib # To send mail from gmail


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >=12 and hour<16:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("Hi, I am Jarvis Sir. Please tell me how may I help you")
    speak("Hi, I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # It take microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to recognize properly. Say that again!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("your email-id","your password")
    server.sendmail('your email-id',to, content)
    server.close()


if __name__ == '__main__':
    # print("Saurabh is good at python")
    # speak("Saurabh is good at python")
    wishMe()
    # takeCommand()
    # speak(takeCommand())
    while True:
        query = takeCommand().lower()

        #Logic for executing task based on query
        if "wikipedia" in query:
            speak('Spearching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia - ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverlflow' in query:
            webbrowser.open("stackoverlflow .com")

        elif 'play songs' in query:
            music_dir = 'D:\\Soulful Songs'
            songs = os.listdir(music_dir)
            print(songs)
            random_var = random.randint(0,10)
            os.startfile(os.path.join(music_dir, songs[random_var]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'open vscode' in query:
            codePath = "C:\\Users\\ucc14\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to saurabh' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "saurabhpal25081995@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent Successfully!")
            except Exception as e:
                print(e)
                speak("Sorry due to technical issue Jarvis can not sent email at this moment!")
        
        elif 'quit' in query:
            print("Shutting down...")
            exit()

