# Jarvis AI Desktop Voice Assistant

Fucntionality of Jarvis Assistant are -
* It can play music for you.
* It can do Wikipedia searches for you.
* It is capable of opening websites like Google, Youtube, etc., in a web browser.
* It is capable of opening your code editor or IDE with a single voice command.

We have used various module in this projects like pyttsx3, sapi5, wikipedia, smtplib, speech_recognition.


**speak()** function will take audio as an argument, and then, it will pronounce it.<br>
**pyttsx3** help us to convert text to speech. In short, it is a text-to-speech library. In case this would not work use **pypiwin32**.<br>
**sapi5 -** Speech API developed by Microsoft and Helps in synthesis and recognition of voice.<br>
**VoiceId** helps us to select different voices.<br>
voice[0].id = Male voice <br>
voice[1].id = Female voice <br>
**smtplib** is Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and to route emails between mail servers.<br>
