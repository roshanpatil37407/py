import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take microphone input from the user and return the recognized text
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Network error.")
        return None

# Function to handle commands
def handle_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "play music" in command:
        speak("Playing music")
        music_dir = "C:/Users/Admin/Music"  # Replace with your music directory path
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    
    elif "quit" in command or "exit" in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("I don't understand that command.")

# Main function
def main():
    speak("Hello! i am roshan patil")
    while True:
        command = take_command()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
