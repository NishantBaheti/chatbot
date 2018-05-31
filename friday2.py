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
import pafy
import vlc
r=sr.Recognizer()

directions=''' quick guide
1.to greet with bot say hello or hey
2.to run any linux command(try simple ones like-date)
3.to search anything on google keyword search and value,default browser firefox
4.to create directories try a sentence specifically containing keyword="directory"
5.to play any song on youtube use any sentence specifically containing keywords='music' or 'song', default browser firefox
6.to make a note simpy ask her to make a note 
7.to end the session say a line containing specifically the keywords=bye,tata,sayonara'''

#primary message by bot
reply="hello. The name is Friday. how can i help you"
tts=gTTS(text=reply,lang="en")
tts.save("breply.mp3")
os.system("mpg321 breply.mp3")



while True:
	os.system("clear")
	print(directions)	
	with sr.Microphone() as source:   #using microphone 
		print("listening")
		audio=r.listen(source)   #listening and getting value into a variable
		print("...")


	try:
		text=r.recognize_google(audio).lower() #recognizing the text from the variable
		stext=text.split()   #splitting 
		length=len(stext)			
		#print(text)
		#to greet with bot say hello or hey
		for i in range(0,length):
			if(stext[i]=="hello" or stext[i]=="hey"):
				reply="hello sir"
				tts=gTTS(text=reply,lang="en")
				tts.save("sreply.mp3")
				os.system("mpg321 sreply.mp3") 
		#to exit the python interpreter or exit the chatbot
			else:
				for i in range(0,length):

					if(stext[i]=="tata" or stext[i]=="sayonara" or stext[i]=="bye" or (stext[i]=="by" and stext[i]=="friday")):
						print("bye")
						bye="bye sir. happy to help you"
						tts=gTTS(text=bye,lang="en")
						tts.save("bye.mp3")
						os.system("mpg321 bye.mp3")
						os._exit(0)
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
							print("...")
							v=requests.get("https://www.youtube.com/results?search_query="+str(song))
							soup=BeautifulSoup(v.text,"html.parser")
							s=soup.findAll("a")
							for i in s:
								if i.get('href').count('/watch')>0:
									ss="https://www.youtube.com"+str(i.get('href'))
									video=pafy.new(ss)
									best=video.getbest()
									playurl=best.url
									Instance = vlc.Instance()
									player = Instance.media_player_new()
									Media = Instance.media_new(playurl)
									Media.get_mrl()
									player.set_media(Media)
									player.play()									

									#wb.get('firefox').open_new_tab(ss)
									#os.system("cvlc "+ss)
									break
						except Exception as e:
							pass
			
			for i in range(0,length):
				if(stext[i]=="note"):
					note="1 do you want to make a new note or 2 do you want to hear the last note?"
					print(note)					
					tts=gTTS(text=note,lang='en')
					tts.save("note.mp3")
					os.system("mpg321 note.mp3")

					with sr.Microphone() as source:
						audionote=r.listen(source)
						try:
							note=r.recognize_google(audionote).lower()
							print("...")
							snote=note.split()
							l=len(snote)
							for i in range(0,l):
								if(snote[i]=="new"):
									newnote="start"
									tts=gTTS(text=newnote,lang='en')
									tts.save("newnote.mp3")
									os.system("mpg321 newnote.mp3")
								 	
									with sr.Microphone() as source:
										newnote=r.listen(source)
										try:
											new_note=r.recognize_google(newnote)
											note_file=open("note.txt",'w+')
											note_file.write(new_note)
											note_file.seek(0)
											note_file.read()
											print("...")
											print("done")
										except Exception as e:
											pass
								if(snote[i]=="last"):
										lastnote="playing the last note you saved"
										tts=gTTS(text=lastnote,lang='en')
										tts.save("lastnotenotice.mp3")
										os.system("mpg321 lastnotenotice.mp3")
										last_note=os.popen("cat note.txt").read()										
										#last_note=open("note.txt",'r')
										#last_note.seek(0)
										#lnote=last_note.read()
										tts=gTTS(text=last_note,lang='en')
										tts.save("lastnote.mp3")
										os.system("mpg321 lastnote.mp3")
						except Exception as e:
											pass
					
								#'''try: 
									#	song=r.recognize_google(audio1)	
										#l=glob.glob('*.mp3')
								#		os.system("mpg321 "+song+".mp3")				
								#	except Exception as e:
								#		pass'''	
	
	except Exception as e:
		pass

						
