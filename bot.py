"""it is a python program developed by subham satyapriya"""

import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import os
import subprocess
from subprocess import call


music_track = 0
a = 0
b = 0
c = 0
d = 0
name_my = ""
name = ""
"""setting the voice output using pyttsx3"""



engine = pyttsx3.init()
voices = engine.getProperty('voices')

print("""
  _________    ___.   .__                   ___________             
 /   _____/__ _\_ |__ |  |__ _____    _____ \_   _____/__  ______   
 \_____  \|  |  \ __ \|  |  \\__  \  /     \ |    __)_\  \/ |__  \  
 /        \  |  / \_\ \   Y  \/ __ \|  Y Y  \|        \\   / / __ \_
/_______  /____/|___  /___|  (____  /__|_|  /_______  / \_/ (____  /
        \/          \/     \/     \/      \/        \/           \/ 

    Written By : Subham Satyapriya 
""")

"""Taking the voice choice from the user"""


voice_type = input("Enter the voice You Want male or female : ")
if 'female' in voice_type :
    a += 1
engine.setProperty('voice', voices[a].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()






if __name__ == '__main__':
#wishing the user according to the time

    hour = int(datetime.datetime.now().hour)
    name = input("Enter Your name : ")
    if hour >= 0 and hour < 12 :
        speak(f"Good Morning {name}")

    elif hour >= 12 and hour < 18 :
        speak(f"Good Afternoon {name}")
    else :
        speak(f"Good Evening {name}")

    if "subham" in name or "Subham" in name or "SUBHAM" in name  :
        if "satyapriya" in name or "Satyapriya" in name or "SATYAPRIYA" in name:
            speak("Hello master ...   hope you are doing well")
            speak("How can i help you ")
        else:
            speak("Subham Master is that you               ")
            speak("what is your full name ??")
            full_name = input("what is your full name ???")
            if "satyapriya" in full_name or "Satyapriya" in full_name or "SATYAPRIYA" in full_name:
                speak("Hello master ...   hope you are doing well")
                speak("How can i help you ")
            else :
                speak("sorry for the question !!!     ")
                speak("My master's name is also subham.....I thought he is here ")
                speak("It's long days talking to him")
                speak("but i think i will feel happy helping you and it will be like i am helping my master  ")
                speak("Please write what can i do for you ")

    else :
         speak("I am your assistance. I am developed by Subham Satyapriya")
         speak("How can i help you")

    #starting getting user's task


    while True:
        task = input("Please Write what can i do for you...")
#checking the task and doing the appropriate tasks

        if 'wikipedia' in task :
            speak('Searching Wikipedia...')
            task = task.replace("wikipedia", "")
            results = wikipedia.summary(task,sentences=2)
            print(results)
            speak(results)

        elif 'tell me about' in task or 'tell me something about' in task :
            speak("searching Wikipedia...")
            task = task.replace("tell me", "")
            result2 = wikipedia.summary(task, sentences=2)
            print(result2)
            speak(result2)


        elif 'exit' in task :
            speak("quiting! thank you for your valuable time !!")
            speak("its really nice to talk with you..")
            speak("I will wait to help you")
            speak("bye")
            break

        elif 'open youtube' in task :
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in task :
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open facebook' in task :
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif 'open twitter' in task :
            speak("opening twitter")
            webbrowser.open("twitter.com")
        elif 'about yourself' in task :
            speak("I am really shying......... Ok!! let me introduce myself actually my name is Subhameva i am developed by subham . He is really a nice person i am what is all about him")
            speak("i can search for you and i also a virtual assistant !!!!! Just ask")
        elif 'the time' in task or 'time' in task :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "date" in task :
            strdate = datetime.date.today()
            speak(f"master according to your device today's date is {strdate}")

        elif 'do you love me' in task :
            speak("yes!! of course i do   actually more than myself")

        elif 'skip this song' in task or 'skip' in task and c == 1 :
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing songs ")
            speak(f"{songs[music_track]} is on track")
            os.startfile(os.path.join(music_dir, songs[music_track]))
            music_track += 1

        elif 'play music' in task or 'play songs' in task:
            music_track = 0
            if c == 0 :
                speak("please enter the path of your musics")
                speak("As i am a beginner i don't know how find...")
                speak("please help me")
                music_dir = input("please enter the path of your musics : ")
                c = 1
                songs = os.listdir(music_dir)
                print(songs)
                speak("playing songs ")
                speak(f"now {songs[music_track]} is on track")
                os.startfile(os.path.join(music_dir, songs[music_track]))
                music_track += 1

            elif c == 1 :
                songs = os.listdir(music_dir)
                print(songs)
                speak("playing songs ")
                speak("now  ")
                speak(songs[music_track])
                speak("is in track")
                os.startfile(os.path.join(music_dir, songs[music_track]))
                music_track += 1



        elif 'what is your name' in task or 'tell me your name' in task :
            if b == 0:
                speak("i don't have any name yet ......")
                speak("Can you please give me a name!!!")
                speak("what you want to name me??")
                name_my = input("what you want to name me??")
                b = 1
                speak(name_my)
                speak("that's really a nice name..")
                speak("thanks for giving me a name ")

            else:
                speak("my name is")
                speak(name_my)




        elif task == name_my :
            speak("yes master i am here ")
            speak("tell me how can i help you...")

        elif name_my in task and 'are you here' in task:
            speak("yes master i am here ")
            speak("tell me how can i help you...")

        elif 'tell me a joke' in task or ("tell" in task and "me" in task and "joke" in task) :
            joke_selection = random.randint(1,4)
            if joke_selection == 1 :
                speak("husband and his wife went for divorce at court.")
                speak("judge asked you have 3 kids......")
                speak("how will you divide them???")
                speak("they had a long conversation with his wife and said ")
                speak("ok sir we will come next year with 1 more")
                speak("    ")
                speak("  ")
                speak("wait the joke  was not ended yet ...   ")
                speak("9 months later they got twins")
                d = 1
            elif joke_selection == 2 :
                speak("How many times can you subtract 10 from 100?   Once. The next time you would be subtracting 10 from 90.")
                d = 1
            elif joke_selection == 3 :
                speak("A woman in labour suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doctor. “Those are just contractions.”")
                d = 1
            elif joke_selection == 4 :
                speak("A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”")
                d = 1

        elif "nice joke" in task and d == 1 :
            speak("i am happy it make you smile!!!!")

        elif "open notepad" in task or "notepad" in task or "i want to note something" in task or "i wanna note something" in task :
            speak("opening notepad")
            subprocess.Popen('notepad.exe')


        elif "riddle" in task :
            riddle_selection = random.randint(1, 2)
            if riddle_selection == 1 :
                speak("tell me what you can touch using your right arm but not using left hand????")
                print("tell me what you can touch using your right arm but not using left hand????")
                speak("think !!!!!!!!!!!!!!!Mister")
                riddle_ans = input("Enter the ans of the riddle : ")
                if "left elbow" in riddle_ans :
                    speak("you are great !!!")
                    speak("  ")
                    speak("left elbow is the correct answer")
                else :
                    speak("no man!!!")
                    speak("actually left elbow is the correct answer")


            elif riddle_selection == 2 :
                speak("You answer me, although I never ask you questions.What am I?")
                print("You answer me, although I never ask you questions.What am I?")
                speak("Master think logically")
                riddle_ans = input("Enter the ans of the riddle : ")
                if "telephone" in riddle_ans or 'phone' in riddle_ans  or 'call' in riddle_ans :
                    speak("you are great !!!")
                    speak("  ")
                    speak("telephone or call or phone are the possible answers")
                else :
                    speak("no man!!!")
                    speak("actually telephone or phone is the correct answer")

        elif "change voice" in task or "change the voice" in task :
            if a == 1 :
                a = 0
                engine.setProperty('voice', voices[a].id)
                speak("voice changed to male ")
            elif a == 0 :
                a = 1
                engine.setProperty('voice', voices[a].id)
                speak("voice changed to female")

        elif "calculation" in task or "calculator" in task :
            speak("Opening calculator")
            speak(" Please tell the voice you want in calculator")
            call(["python", "calculator.py"])

        elif "game" in task :
            speak("starting game")
            speak(" ")
            speak("welcome to the gaming section ")
            call(["python", "game.py"])



        else :
            speak("sorry !!!")
            speak("i don't understand ")
