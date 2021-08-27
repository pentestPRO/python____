#!/usr/bin/python3

from termcolor import colored
class ciphyre:

	def __init__(self,data):
		self.alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		self.data = data
		print(colored("[*]PLEASE ENTER SHIFT NUMBER BETWEEN 0 TO 25 [*]","red"))
		self.n = input("ENTER THE SHIFT NO : ")
		print("\n")
		
	def ceaser_encode(self):
		self.add = []
		self.password = ""
		for self.letter in self.data:
			self.add.append(self.letter.upper())

		for self.let in self.add:
			self.hash = self.alphabets.index(self.let)
			self.hash = self.hash + int(self.n)
			if self.hash >= 26:
				self.hash = int(self.hash) - 26
			self.hash_alpha = self.alphabets[self.hash]
			self.password += self.hash_alpha
			
		print("THE ENCRYPTED PASSWORD : ",colored(self.password,"blue"))

	def decode(self):
		self.decoder = []
		self.decode_password = ""
		for self.word in self.data:
			self.decoder.append(self.word.upper())
		
		for self.char in self.decoder:
			self.hash = self.alphabets.index(self.char)
			self.hash = self.hash - int(self.n)
			self.hash_alpha = self.alphabets[self.hash]
			self.decode_password += self.hash_alpha
		print("THE DECRYPTED PASSSWORD : ",colored(self.decode_password,"blue"))

		
		
print(colored("[*] DO NOT ENTER NUMBERS [*]","red"))
data = input("ENTER THE PASSWORD FOR ENCODE OR DECODE  : ")
obj = ciphyre(data)

user_input = input("""YOU HAVE TO ENCODE OR DECODE : 
	1] ENCODE
	2] DECODE
""")
if user_input == "1":
	obj.ceaser_encode()
elif user_input == "2":
	obj.decode()

else:
	print(colored("ENTER A VALID OPTION","red"))