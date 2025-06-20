# AUDIO ==>  TEXT
# install 2 package (pyaudio,SpeechRecognition)

import speech_recognition as sr
def speech_txt():
    r=sr.Recognizer()  #used to recognize

    while True:
        with sr.Microphone() as source:     # or source=sr.Microphone() ,source is the object of Microphone
            print('speak')
            audio=r.listen(source) #now our voice is inside audio
            
            try:
                text=r.recognize_google(audio) # we use google api to convert back to text
                print(text)
            except:
                print('did not here anything')

speech_txt()