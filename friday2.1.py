#!/usr/bin/python3

import os
#importing google tts
from gtts import gTTS
#importing speech recognition
import speech_recognition as sr
#importing web browser library
import webbrowser as wb
#importing beautifulsoup 
from bs4 import BeautifulSoup
import numpy as np
#importing computer vision library 
import cv2
import requests
import pafy
import vlc
from PIL import Image
import time

#importing smtp library for accessing email to send emails
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders

#creating instance for speech recognition 
r=sr.Recognizer()

directions=''' quick guide
1.to greet with bot say hello or hey
2.to run any linux command(try simple ones like-date)
3.to search anything on google keyword search and value,default browser firefox
4.to create directories try a sentence specifically containing keyword="directory"
5.to play any song on youtube use any sentence specifically containing keywords='music' or 'song', default browser firefox
6.to make a note simpy ask her to make a note 
7.start surveillance of camera range use keyword="motion detection","keep an eye" 
8.to end the session say a line containing specifically the keywords=bye,tata,sayonara'''

#primary message by bot
reply="hello everyone. The name is Friday."
tts=gTTS(text=reply,lang="en")
tts.save("breply.mp3")
os.system("mpg321 breply.mp3")

def mail_image(warning_image):
	
	email_user="nb9461416717@gmail.com"
	email_send="nb9461416717@gmail.com"
	subject= "warning!! Motion Detected"
	passwd="nishant@1234"
	#img_data=open(warning_image,'rb').read()
	msg=MIMEMultipart()
	msg['From']=email_user
	msg['To']=email_send
	msg['subject']=subject

	body='Intruder '
	msg.attach(MIMEText(body,'plain'))
	
	text=MIMEText("Warning")
	msg.attach(text)
	with open(warning_image,'rb') as fp:
		image=MIMEImage(fp.read())
		msg.attach(image)

	text=msg.as_string()
	server=smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email_user,passwd)
	server.sendmail(email_user,email_send,text)
	server.quit()


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
				reply="hello nishant"
				tts=gTTS(text=reply,lang="en")
				tts.save("sreply.mp3")
				os.system("mpg321 sreply.mp3") 
		#to exit the python interpreter or exit the chatbot
			else:
				for i in range(0,length):

					if(stext[i]=="tata" or stext[i]=="sayonara" or stext[i]=="bye" or (stext[i]=="by" and stext[i]=="friday")):
						print("bye")
						bye="bye nishant. happy to help you"
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
									if 0xff == ord('q'):
										player.release()						

									#wb.get('firefox').open_new_tab(ss)
									#os.system("cvlc "+str(ss))
									break
						except Exception as e:
							pass
			
			for i in range(0,length):
				if(stext[i]=="note"):
					note="1 do you want to make a new note or do you want to hear the last note?"
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
											note_file.close()
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
			for i in range(0,length):
				if(stext[i]=="keep" or stext[i]=="eye" or stext[i]=="motion"):
					cap=cv2.VideoCapture(0)
					#taking pic 1
					#tts=gTTS(text="warning! Security breach",lang='en')
					#tts1=gTTS(text="I am on it",lang='en')
					#tts.save("on.mp3")
					#os.system("mpg321 on.mp3")
					print("Motion Detection start")
					while cap.isOpened():
						tp1=cap.read()[1]
						tp2=cap.read()[1]
						tp3=cap.read()[1]
						gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)	
						gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
						gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)
						newimage1=cv2.GaussianBlur(gray1, (21, 21), 0)
						newimage2=cv2.GaussianBlur(gray2, (21, 21), 0)
						newimage3=cv2.GaussianBlur(gray3, (21, 21), 0)
						#creating difference between first and second

						#diff1=cv2.subtract(tp1,tp2)	
						#can also be done by numpy array subtraction
						#cv2.imshow('nishant1',tp1)
						#cv2.imshow('nishant2',tp2)
						#cv2.imshow('nishant3',tp3)
						#cv2.imshow('nishant4',tp4)
						#most accurate result by cv2

						f_diff1=cv2.absdiff(newimage1,newimage2)
						f_diff2=cv2.absdiff(newimage2,newimage3)
						f_diff3=cv2.bitwise_and(f_diff1,f_diff2)
						#cv2.imshow('nishant',f_diff3)
						#cv2.imshow('nishant1',tp1)
						#creating a threshold to get clearer image					
						thresh=cv2.threshold(f_diff3, 10, 255, cv2.THRESH_BINARY)[1]
						thresh = cv2.dilate(thresh, None, iterations=2)
						cv2.imshow('MotionDetection',thresh)
						#cv2.imshow('nishant1',f_diff1)
						#cv2.imshow('nishant2',f_diff2)
						#print(thresh)
						if np.array_equal(thresh,np.zeros((480,640))):
							pass
						else:
							#os.system("mpg321 Warning.mp3")
							cv2.imwrite('warning.png',tp3)
							im=Image.open("warning.png")
							im.save("warning.png")
							mail_image("warning.png")						
							
							#can send the image of movement to the mail of concern user 
						if cv2.waitKey(1) & 0xff == ord('q'):
							cv2.destroyWindow('MotionDetection')
							cap.release()
							break
							
	
					#mail_image('warning.png')
					
					
							
	except Exception as e:
		pass

						
