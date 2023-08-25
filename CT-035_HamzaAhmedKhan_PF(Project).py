###                                   PROJECT  -  J.A.R.V.I.S  (AI- Voice Assistant)                                ###

###                                                       BY                                                        ###

###                           GROUP (  MINAHIL TARIQ  --  SAIM AHMED -- HAMZA AHMED KHAN  )                         ###





import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia                                                   ##  DONT FORGET TO INSTALL THE NECESSARY PIPS TO RUN THIS CODE                                                                
import webbrowser                                                  ##  e.g.   pyttsx3, wikipedia, speech recognition ..  
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("\n\t*** I AM YOUR VOICE ASSISTANT ***")
print("\nPlease Tell Me How May I Assist You Sir!..")
print("I can do multiple tasks and here they are\nnow listen carefully!")
print("\nINSTRUCTIONS:")    
print("\n-Say What time is it")
print("-Say What date is it")
print("-Say open drive")
print("-Say play music")
print("-Say according to wikipedia in the end in your sentence")
print("-Say open youtube")
print("-Say open google chrome")
print("-Say open facebook")
print("-Say open gmail")
print("-Say open vs code")

def wishMe():
    
    hour = int(datetime.datetime.now().hour)    
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")    

    speak("Please Tell Me How May I Assist You Sir!")
    speak("I can do multiple tasks and here they are now listen carefully!")
    speak("If You want to know the Time\n(Say What time is it)")
    speak("If You want to know the Date\n(Say What date is it)")
    speak("If You want to open Drive C\n(Say open drive)")                        
    speak("If You want to listen music\n(Say play music)")                           
    speak ("If You want to know about anything on Wikipedia...\n(Say according to wikipedia in the end in your sentence)")
    speak("If You want to open youtube\n(Say open youtube)")
    speak("If You want to open google\n(Say open google chrome)")
    speak("If You want to open facebook\n(Say open facebook)")
    speak("If You want to open gmail\n(Say open gmail)")
    speak("If You want to open vs code\n(Say open vs code)")                        


def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ="en-in")
        print(f"User Said:  {query}\n")
    
    except Exception as e:    
        print("Say That Again Please!...")
        return "None"
    
    return query    

if __name__ == "__main__":
    speak ('I Am Online Sir!\nMy Name Is Jarvis!\nStand For(Just A Rather Very Intelligent System\n)')
    
    wishMe()
    while True:
    #if 1:    
        query = takeCommand().lower()                                        ##  LOGIC FOR EXECUTING TASK BASED ON QUERY
        
        if "what time is it" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}, Sir!")
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time") 
        
        elif "what date is it" in query:
            strdate = datetime.date.today()
            print(strdate)
            speak(f"The date is {strdate}, Sir!")
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time") 
        

        elif "open drive" in query: 
            speak ("Opening Drive C....")                                    ##  IF YOU WANT TO OPEN OTHER DRIVE YOU HAVE TO CHANGE THE DRIVE FROM HERE
            os.startfile("C:")
                                                           
        elif "play music" in query:
            speak ("Playing Music....")
            music_dir = r"C:\Users\Hamza Ahmed Khan\Downloads\Music"                          ## TO PLAY MUSIC YOU HAVE TO CHANGE THE PATH ADDRESS \\
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))    
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time") 
        
        elif "wikipedia" in query:
            speak ("Searching Wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("According to wikipedia")
            print(results)
            speak(results)
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time")
        
        elif "open youtube" in query:
            speak ("Opening Youtube....")
            webbrowser.open("youtube.com")
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time")

        elif "open google chrome" in query:
            speak ("Opening Google Chrome....")
            webbrowser.open("google.com")
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time")

        elif "open gmail" in query:
            speak ("Opening Gmail....")
            webbrowser.open("gmail.com")
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time")

        elif "open facebook" in query:
            speak ("Opening Facebook....")
            webbrowser.open("facebook.com")
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time")

        elif "open vs code" in query:
            speak ("Opening Visual Studio Code....")
            codepath = "C:\\Users\\HP\\Desktop\\Visual Studio Code"                                   ##  TO OPEN VS-CODE YOU HAVE TO CHANGE THE PATH ADDRESS \\ 
            os.startfile(codepath)
            speak("Thank u Is there any thing for me...so let me Know...Have a Great time")   
               
                        

                  



