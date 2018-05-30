#!/usr/bin/python3

import os
#importing google tts
from gtts import gTTS
#importing speech recognition
import speech_recognition as sr
#importing web browser library
import webbrowser as wb
#import glob
#importing beautifulsoup 
from bs4 import BeautifulSoup
import requests
r=sr.Recognizer()

directions=''' quick guide
1.to greet with bot say hello or hey
2.to run any linux command(try simple ones like-date)
3.to search anything on google keyword search and value,default browser firefox
4.to create directories try a sentence specifically containing keyword="directory"
5.to play any song on youtube use any sentence specifically containing keywords='music' or 'song', default browser firefox
'''

#primary message by bot
reply="hello. The name is Friday. how can i help you"
tts=gTTS(text=reply,lang="en")
tts.save("sreply.mp3")
os.system("mpg321 sreply.mp3")



while True:
	os.system("clear")
	print(directions)	
	with sr.Microphone() as source:   #using microphone 
		print("listening")
		audio=r.listen(source)   #listening and getting value into a variable
		print("...")


	try:
		text=r.recognize_google(audio)  #recognizing the text from the variable
		stext=text.split()   #splitting 
		length=len(stext)			
		
		#to greet with bot say hello or hey
		if(text=="hello" or text=="hey"):
			reply="hello"
			tts=gTTS(text=reply,lang="en")
			tts.save("sreply.mp3")
			os.system("mpg321 sreply.mp3")

		
		else:
			#to run any linux command(try simple ones like-date) 
			for i in range(0,length):
				x=os.system(stext[i])
				x1=os.popen(stext[i]).read()  #opening and reading output of linux command
				if(x==0):
					inn1 = gTTS(text =x1,lang='en')
					inn1.save("new.mp3")
					os.system("mpg321 new.mp3") 

			#to search anything on google keyword search and value default browser firefox
			for i in range(0,length):
				if(stext[i]=="search"):	
					error= gTTS(text ="Searching on google", lang='en')
					error.save("error.mp3")
					os.system("mpg321 error.mp3")
					wb.get('firefox').open_new_tab("https://www.google.com/search?q="+text)

			#to create directories try a sentence specifically containing keyword="directory"			
			for i in range(0,length):
				if(stext[i]=="directory"):
					dir=gTTS(text="how many directories",lang='en')
					dir.save("howmany.mp3")
					os.system("mpg321 howmany.mp3")
					with sr.Microphone() as source:
						print("number of directories")
						audio1=r.listen(source)
						print("...")
						try :
							number=r.recognize_google(audio1)
							num=int(number)						
							for i in range(1,num+1):
								os.system("mkdir dir"+str(i))
							print("done")
						except Exception as e:
							pass 
			
			#to play any song on youtube default browser firefox				
			for i in range(0,length):
				if(stext[i]=="music" or stext[i]=="song"):
					with sr.Microphone() as source:
						tts=gTTS(text="which song ",lang='en')
						tts.save('whichsong.mp3')
						os.system("mpg321 whichsong.mp3")
						audio1=r.listen(source)
						try: 
							song=r.recognize_google(audio1)	
							#l=glob.glob('*.mp3')
							os.system("mpg321 "+song+".mp3")				
						except Exception as e:
							pass	
	except Exception as e:
		pass

'''		try:
							song=r.recognize_google(audio1)	
							print("...")
							v=requests.get("https://www.youtube.com/results?search_query="+str(song))
							soup=BeautifulSoup(v.text,"html.parser")
							s=soup.findAll("a")
							for i in s:
								if i.get('href').count('/watch')>0:
									ss="https://www.youtube.com"+str(i.get('href'))
									wb.get('firefox').open_new_tab(ss)
									break
						except Exception as e:
							pass'''
