# TEXT ==> AUDIO (install pyttsx3)
# import pyttsx3
# txt_sp=pyttsx3.init()
# text=input('enter the text : ')
# txt_sp.say(text)
# txt_sp.runAndWait()

#change to female voice
import pyttsx3
tex_sp=pyttsx3.init() 
text=input("Enter a text:")

voices = tex_sp.getProperty('voices') 
tex_sp.setProperty('voice',voices[1].id) 

# tex_sp.setProperty('volume', 0.1)   # volume control


tex_sp.say(text)   
tex_sp.runAndWait()


