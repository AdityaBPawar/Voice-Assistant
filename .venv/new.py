# importing all the required libraries
import speech_recognition as sr   # for converting speech (voice) to text
import pyttsx3                   # for converting text to speech
import datetime                  # to fetch system time
import wikipedia                 # for fetching summaries from Wikipedia
import webbrowser                # lets me open websites in the default browser
import pyjokes                   # for telling random programming jokes

#function to make the assistant talk
def speak(text):
    print(f'Assistant : {text}')
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported in this environment.")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

def take_command_text():
    return input("You (type your command): ").lower()

def take_command_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        return "none"

    return query.lower()

def run_assistant():
    wishMe()

    while True:

        print ("\n---Input Mode---")
        mode = input("Type 'v' for voice input or 't' for text input: ").lower()

        if mode == "v":
            query = take_command_voice()
        else:
            query = take_command_text()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia: " + result)
            except wikipedia.exceptions.DisambiguationError:
                speak("Sorry, I couldn't understand. Please say that again...")

        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening google...")
            webbrowser.open("https://www.google.com/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("Sorry, I couldn't understand. Please say that again...")

run_assistant()