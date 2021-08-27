#!/usr/bin/python3

import hashlib
import pyfiglet
from termcolor import colored
hash = hashlib.md5()
hash1 = hashlib.sha256()
hash2 = hashlib.sha512()
hash3 = hashlib.sha224()
hash4 = hashlib.sha384()
hash5 = hashlib.sha1()

ascii_banner = pyfiglet.figlet_format("HASH GENERATOR", font = "slant")
print(colored(ascii_banner,"red"))
while True:
	name = input(f"please type password for encrypt into  hash algorithm : ")
	banner = """      0: MD5
         1: SHA256
         2: SHA512
	 3: SHA224
	 4: SHA384
	 5: SHA1    """
	print(banner)
	number = input("choose a number : ")
	hash.update(name.encode())
	hash1.update(name.encode())
	hash2.update(name.encode())
	hash3.update(name.encode())
	hash4.update(name.encode())
	hash5.update(name.encode())

	if number == "0":
		print("MD5 HASH : ",colored( hash.hexdigest(),"red"))
	elif number == "1":
		print("SHA256 HASH : ", colored(hash1.hexdigest(),"red"))
	elif number == "2":
		print("SHA512 HASH : ", colored(hash2.hexdigest(),"red"))
	elif number == "3":
		print("SHA224 HASH : ", colored(hash3.hexdigest(),"red"))
	elif number == "4":
		print("SHA384 HASH : ", colored(hash4.hexdigest(),"red"))
	elif number == "5":
		print("SHA1 HASH : ", colored(hash5.hexdigest(),"red"))
		exit(0)
	elif number == "q":
		print("THANKS FOR USING :")
		exit(0)
	else:
		print("CHOOSE A CORRECT number ")

