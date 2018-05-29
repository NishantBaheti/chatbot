#!/usr/bin/python3

import os
from gtts import gTTS    #for text to speech conversion
import speech_recognition as sr    #for speech recognition
import webbrowser as wb
#import pyglet    #plays audio within the code
import time,os

#recognizing the voice
r = sr.Recognizer()

 #listening through microphone
with sr.Microphone() as source:
	print("Say something!")	
	audio = r.listen(source)
	print("Done!")

 #recognizing voice
try:
	text = r.recognize_google(audio)
	inn = gTTS(text = text,lang = 'en')
	audioo = 'temp.mp3'
	inn.save(audioo)
	'''
	voice = pyglet.media.load(audioo)
	voice.play()
	time.sleep(voice.duration)'''
	os.system('mpg321 temp.mp3')	
	#os.remove(audioo)
	print("You said: "+text)
	#print(type(text))

 #Running the text on system terminal (if found x=0, else 1)
	x=os.system(text)
	#x1 = os.system(text+"|tee file.txt")
	#f = open("file.txt",'r')
	x1=os.popen(text).read()
#if command is found 
	if(x==0):
		inn1 = gTTS(text =x1, lang='en')
		inn1.save("new.mp3")
		os.system("mpg321 new.mp3")

#if not a command
	else:
	#responding error message
		error= gTTS(text ="oyee chutiye!!! command nahi mila, search kar rahi hoon na", lang='en')
		error.save("error.mp3")
		os.system("mpg321 error.mp3")
		print("This is not a linux command")
		wb.get('firefox').open("https://www.google.com/search?q="+text)
	

except Exception as e:
	pass

