import speech_recognition as sr
import pyttsx3
import os
import serial
import time
speech= sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested Driver is not found")
except RuntimeError:
    print("Driver fails to initialize")

voices = engine.getProperty("voices")

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)
engine.runAndWait()'''
def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ""
    print("Listening...")
    with sr.Microphone() as source:
        audio= speech.listen(source)
    try:
        voice_text= speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Network Error")
    return voice_text

def temp(t,d):
    if "t" in d:
        n=t[2:6]
        return n
    
        
if __name__=='__main__':
    speak_text_cmd("Hi!! I am your voice assistant. How can i help you?") 
    while True:
        voice_note = read_voice_cmd()
        print('cmd :{}'.format(voice_note))
        if "hello" in voice_note:
            speak_text_cmd("Hello Sankalp...How can i help you?")
            continue
        elif "open" in voice_note:
            os.system("explorerE:\\{}".format(voice_note.replace('Open ','')))
            continue
        elif "temp" in voice_note:
            ArduinoSerial = serial.Serial('com6',9600)
            time.sleep(2)
            t= str (ArduinoSerial.readline())
            ArduinoSerial.close()
            t1=temp(t,"t")
            print (t)
            speak_text_cmd("temperature is "+str(t1)+" degree celcius")
            continue
        elif "name" in voice_note:
            speak_text_cmd("Your Name is Sankalp")
            continue
        elif "humidity" in voice_note:
            ArduinoSerial = serial.Serial('com6',9600)
            time.sleep(2)
            h= str (ArduinoSerial.readline())
            ArduinoSerial.close()
            h1=temp(h,"h")
            print (h)
            speak_text_cmd("Humidity is "+str(h1)+" degree celcius")
            continue
        elif 'bye' in voice_note:
            speak_text_cmd("Bye sir...take care ...Moving Back to stand by mode")
            exit()
