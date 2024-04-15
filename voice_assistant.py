import pyttsx3
import wikipedia
Geek = pyttsx3.init()
voice = Geek.getProperty('voice')
Geek.setProperty('voice', voice)
In = input(" search for:  ")
result = wikipedia.summary(In, sentences = 10)
print(result)
Geek.say(result)
Geek.runAndWait()