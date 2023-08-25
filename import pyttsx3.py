import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    
    hour = int(datetime.datetime.now().hour)    
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")    

    speak("Please Tell Me How May I Assist You Sir!..")       


def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ="en-in")
        print(f"User Said: , {query}\n")
    
    except Exception as e:    
        print("Say That Again Please!...")
        return "None"
    
    return query    

if __name__ == "__main__":
    speak ('I Am Jarvis (Just A Rather Very Intelligent System..)')
    
    wishMe()
    
    if 1:    
        query = takeCommand().lower()             #Logic for executing task based on query
        
        if "what time is it" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}, Sir!")

        elif "play music" in query:
            music_dir = "C:\\Users\\HP\\Downloads\\Musical"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))     
        
        elif "wikipedia" in query:
            speak ("Searching Wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google chrome" in query:
            webbrowser.open("google.com")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open vs code" in query:
            codepath = "C:\\Users\\HP\\Desktop\\Visual Studio Code"
            os.startfile(codepath)   


def Goodbye():   
    
    speak("It's Good Talking with You Sir!..Enjoy")       
        
Goodbye()       
        

        
      

        

        
    

    



            
        






 


