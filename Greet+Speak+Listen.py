import imdb
import pyttsx3
import speech_recognition as sr
import datetime
import time

# Function for speak
def speak(text):
    eng = pyttsx3.init()
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[0].id)
    rate = eng.getProperty('rate')
    eng.setProperty('rate', rate-20)
    eng.say(text)
    eng.runAndWait()


# wait i will import one more thing here let's make it more interesting this one...
# I just import listening mode and recognizing mode into it

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold= 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio,language='en-in')
            print(f"You just said: {query}\n")
        except Exception as e:
            speak("sir if you don't mind can you say that again please?....")
            query = "None"
        return query
# Now again i want to make it more interesting.....
# Now i want to make a wish function which helps to greet users.....
# It means morning, afternoon, evening, night sab time pe ye voice assistant greet karega user ko....


def greetMe():
    hour = int(datetime.datetime.now().hour)
    T = time.strftime("%I : %M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning Sir, its {T} sir ...")
    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon Sir, its {T} sir .....")
    else:
        speak(f"Good Evening Sir, its {T} sir ....")
    speak("Sir please tell me what can i do for you?.....")

greetMe()
TakeCommand()