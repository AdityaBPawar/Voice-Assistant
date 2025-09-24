# importing all the required libraries
import speech_recognition as sr   # for converting speech (voice) to text
import pyttsx3                   # for converting text to speech
import datetime                  # to fetch system time
import wikipedia                 # for fetching summaries from Wikipedia
import webbrowser                # lets me open websites in the default browser
import pyjokes                   # for telling random programming jokes

# function to make the assistant talk
def speak(text):
    print(f"Assistant: {text}")  # print so I can also see the response
    try:
        engine = pyttsx3.init()   # initialize text-to-speech
        engine.say(text)          # put the text in the queue to be spoken
        engine.runAndWait()       # actually say it
    except:
        # if the environment doesn't support speech, just show the text
        print("Speech output not supported in this environment.")

# greeting function based on time of the day
def wish_user():
    hour = int(datetime.datetime.now().hour)  # current hour in 24hr format
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

# function for text-based input (fallback option if voice fails)
def take_command_text():
    return input("You (type your command): ").lower()

# function to take voice input from microphone and convert it to text
def take_command_voice():
    r = sr.Recognizer()  # recognizer object
    with sr.Microphone() as source:  # use the system mic as input
        print("Listening...")
        r.pause_threshold = 1  # wait time before assuming I stopped speaking
        audio = r.listen(source)  # record audio

    try:
        print("Recognizing...")
        # using Google’s speech recognition engine (requires internet)
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Sorry, I couldn't understand. Please say that again...")
        return "none"  # return a dummy string if recognition fails

    return query.lower()

# main loop of the assistant
def run_assistant():
    wish_user()

    while True:
        # choose whether to use voice or text input
        print("\n--- Input Mode ---")
        mode = input("Type 'v' for voice input or 't' for text input: ").lower()

        if mode == 'v':
            query = take_command_voice()
        else:
            query = take_command_text()

        # now process the query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google...")
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
            speak("Sorry, I didn't understand that. Try again.")

# start the assistant
run_assistant()