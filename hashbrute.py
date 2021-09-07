#!/usr/bin/python3

import sys
import hashlib
import time
import pyfiglet
from termcolor import colored


global ascii_banner
ascii_banner = pyfiglet.figlet_format("pass_brute", font="slant")


class brute:
    def __init__(self):
        time2 = time.strftime("%H:%M:%S")
        print(colored(ascii_banner, "green"))
        print(f"STARTING TIME : {time2}")
        if len(sys.argv) == 4:
            self.user_input = sys.argv[1]
            self.password_file = sys.argv[2]

    def hash_maker(self, password):
        if len(sys.argv) == 4:
            self.password_name = password
            self.hash_type = sys.argv[3]
            self.hash0 = hashlib.md5()
            self.hash1 = hashlib.sha256()
            self.hash2 = hashlib.sha384()
            self.hash3 = hashlib.sha512()
            self.hash4 = hashlib.sha224()
            self.hash5 = hashlib.sha1()
            self.hash6 = hashlib.sha3_512()
            self.hash7 = hashlib.sha3_224()
            self.hash8 = hashlib.sha3_256()
            self.hash9 = hashlib.sha3_384()
            self.hash10 = hashlib.shake_256()
            self.hash11 = hashlib.shake_128()

            if self.hash_type == "md5":
                self.hash_generator(self.hash0)

            elif self.hash_type == "sha256":
                self.hash_generator(self.hash1)

            elif self.hash_type == "sha384":
                self.hash_generator(self.hash2)

            elif self.hash_type == "sha512":
                self.hash_generator(self.hash3)

            elif self.hash_type == "sha224":
                self.hash_generator(self.hash4)

            elif self.hash_type == "sha1":
                self.hash_generator(self.hash5)
            elif self.hash_type == "sha3_224":
                self.hash_generator(self.hash7)
            elif self.hash_type == "sha3_512":
                self.hash_generator(self.hash6)
            elif self.hash_type == "sha3_384":
                self.hash_generator(self.hash9)
            elif self.hash_type == "sha_256":
                self.hash_generator(self.hash8)

            else:
                print("[*] PLEASE GIVE RIGTE HASH TYPE [*]")
                sys.exit(0)

    def hash_generator(self, hash_name):
        time1 = time.strftime("%H:%M:%S")
        self.hash_name = hash_name
        self.hash_name.update(self.password_name.encode())
        self.name = self.hash_name.hexdigest()

        if self.user_input == self.name:
            print(
                f"#########################{time1}##############################")
            print(f"HASH : {colored(self.user_input,'yellow')}")
            print(f"THE CRACKED HASH  : {colored(self.password_name,'red')} ")
            print(f"#######################################################")
            sys.exit(0)
        else:
            pass

    def usage(self):
        print(colored("""
            FIRST ARGV : HASH (for cracking) 
            SECOND ARGV : PASSWORD FILE
            THIRD ARGV : TYPE OF HASH  EX : md5,sha256,sha512,sha384,sha224      
        """, "blue"))
        print(colored(
            "EX : python3 hash_brute.py hash_format password file hash_type", "red"))

    def hash_brute(self):
        if len(sys.argv) == 4:
            with open(self.password_file, 'r', encoding="latin-1") as f:
                self.pass_name = f.read().split("\n")
                for self.password in self.pass_name:
                    self.hash_maker(self.password)
        else:
            self.usage()


obj = brute()
obj.hash_brute()



