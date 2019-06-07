import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id )

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<18: 
        speak("Good Afternoon!")
    else:
        speak("Good Morning!")
    speak("Hello Master Pritivash!! I am Maverick. How can I help you? ")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    #Take microphone input from the user and returs string
    r = sr.Recognizer()
    with sr.Microphone() as source:     
        print ("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print( "Master said : ",(query),"\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "none"
    return query
 

if __name__ == "__main__":
    wishMe()
    if 1:
    #while True:
        query = takeCommand().lower() #logic for exe task by query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Master, the time is{strTime}")

        elif ' open code' in query:
            codePath = 'C:\\Users\\QWERTYvash\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code' 
            os.startfile(codePath)
            
    speak("Bye. Shutting down!! ")