#!/usr/bin/python3

import os
from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb
import time

r=sr.Recognizer()

reply="hello. I am Friday. Nice to meet you. How may i help you"
tts=gTTS(text=reply,lang="en")
tts.save("sreply.mp3")
os.system("mpg321 sreply.mp3")
while True:	
	with sr.Microphone() as source:
		print("listening")
		audio=r.listen(source)
		print("...")


	try:
		text=r.recognize_google(audio)
		stext=text.split()
		length=len(stext)			

		if(text=="hello" or text=="hey"):
			reply="hello"
			tts=gTTS(text=reply,lang="en")
			tts.save("sreply.mp3")
			os.system("mpg321 sreply.mp3")

		
		else: 
			for i in range(0,length):
				x=os.system(stext[i])
				x1=os.popen(stext[i]).read()
				if(x==0):
					inn1 = gTTS(text =x1,lang='en')
					inn1.save("new.mp3")
					os.system("mpg321 new.mp3")


			for i in range(0,length):
				if(stext[i]=="search"):	
					error= gTTS(text ="Searching on google", lang='en')
					error.save("error.mp3")
					os.system("mpg321 error.mp3")
					print("This is not a linux command")
					wb.get('firefox').open("https://www.google.com/search?q="+stext[1:length])

	except Exception as e:
		pass
