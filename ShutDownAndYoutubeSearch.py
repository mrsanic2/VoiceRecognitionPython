import os
import speech_recognition
import pyaudio
import pyttsx3
import webbrowser

r = speech_recognition.Recognizer()


def SpeakText(command):

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-80)
    engine.say(command)
    engine.runAndWait()
command="halo"
SpeakText(command)
def listen():
    with speech_recognition.Microphone() as source2:

        r.adjust_for_ambient_noise(source2, duration=1)
        SpeakText("What do you want me to do")

        audio2 = r.listen(source2)

        try:
            MyText = r.recognize_google(audio2)
        except:
            SpeakText("Didn't recognize voice")
            SpeakText("Try again buddy")
            listen()
            return


    print(MyText)
    MyText = MyText.lower()
    if MyText == "boom":
        SpeakText("aight bet")
        SpeakText("Shutting down computer in 5")
        SpeakText("4")
        SpeakText("3")
        SpeakText("2")
        SpeakText("1")
        SpeakText("Good bye")
        os.system('shutdown -s')
    elif MyText == "youtube":
       with speech_recognition.Microphone() as source2:
            SpeakText("What video do you want to search?")
            r.adjust_for_ambient_noise(source2, duration=1)
            audio2 = r.listen(source2)
            try:
                video = r.recognize_google(audio2)
            except:
                SpeakText("Didn't recognize video")
                SpeakText("Try again buddy")
                listen()
                return

            video = video.lower()

       SpeakText("Searching "+video)
       webbrowser.open('https://www.youtube.com/results?search_query='+video)
listen()