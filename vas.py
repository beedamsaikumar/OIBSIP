import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to perform actions based on voice commands
def perform_action(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}")
    elif "search" in command:
        speak("What do you want to search for?")
        search_query = recognize_speech()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I didn't catch that command.")

# Function to recognize speech input
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return ""

# Main program loop
if __name__ == "__main__":
    speak("Hello! How can I help you?")
    
    while True:
        voice_command = recognize_speech()
        perform_action(voice_command)
