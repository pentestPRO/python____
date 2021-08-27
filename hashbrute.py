#!/usr/bin/python3

import hashlib
import time
hasher = input("enter the hash : ")

f = open("local.txt", "r")
for line in f.readlines():
	line = line.strip("\n")
	hash = hashlib.sha384()
	hash.update(line.encode())
	data = hash.hexdigest()
	if data == hasher:
		print("password is : " + line )
		print(time.time())
		exit(0)
	else:
		print("do not match : " + line)


