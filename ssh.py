#!/usr/bin/python3

import pexpect

prompt = ["# ",">>> ","> ","\$ "]

def sendcommand(child,cmd):
	child.sendline(cmd)
	child.expect(prompt)
	print(child.before)

def connect(username,hostname,password):
	ssh_key = "Are you sure you want to continue connecting "
	structure = "ssh"+ " " + username + "@" +  hostname
	child = pexpect.spawn(structure)
	ret = child.expect([pexpect.TIMEOUT,ssh_key,'[P|p]assword: '])
	print(ret)
	if ret == 0:
		print("# error is occured")
		return
	if ret == 1:
		child.sendline("yes")
		ret = child.expect([pexpect.TIMEOUT,'[p|p]assword: '])
		print(ret)
		if ret == 0:
			print("# error is eccured")
			return
	child.sendline(password)
	child.expect(prompt)
	return child
def main():
	username = "msfadmin"
	hostname = "192.168.0.104"
	password = "msfadmin"

	child = connect(username,hostname,password)
	#setdefaulttimeout(5)
	sendcommand(child,"cat /etc/passwd ")
main()
