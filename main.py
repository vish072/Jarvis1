import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
# newsapi = "cd22e6eb52004887b7d59b4f6f277d1b"

def speak(text):
    engine.say(text)
    engine.runAndWait()



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open spotify" in c.lower():
         webbrowser.open("spotify://")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/vishakha-08855b246/")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        try:
             link = musicLibrary.music[song]
             webbrowser.open(link)
             speak(f"Playing {song}.")
        except KeyError:
             speak(f"Sorry, I couldn't find the song {song}. Please check your library.")recognizer = sr.Recognizer()
 
# newsapi = "cd22e6eb52004887b7d59b4f6f277d1b"




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open spotify" in c.lower():
         webbrowser.open("spotify://")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/vishakha-08855b246/")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
         try:
             link = musicLibrary.music[song]
             webbrowser.open(link)
             speak(f"Playing {song}.")
         except KeyError:
             speak(f"Sorry, I couldn't find the song {song}. Please check your library.")













if __name__== "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
