#!/usr/bin/python3

import requests
import threading
import sys
import time
from datetime import datetime
import pyfiglet
from termcolor import colored
import random
import socket


import validate

def host_confirm():
           try:
               res = requests.get(sys.argv[1])
               if res.status_code == 200:
                return "URL IS VALID"
               
           except Exception:
                print("URL IS INVALID : ")
                sys.exit(0)
            
                    
global ascii_banner 
ascii_banner = pyfiglet.figlet_format("url_FUZZER", font = "slant")
colour = ["red","blue","green","white","yellow"]
print(colored(ascii_banner,random.choice(colour)))
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


if len(sys.argv) == 3:
   
    print(colored("[*] GIVEN URL [*]:        ","yellow"),sys.argv[1])
    print(colored("[*] DIRECTORY_FILE [*]:   ","yellow"),sys.argv[2])
    print(colored("[*] START-TIME [*]:       ","yellow"),current_time)
    print(colored("[*] HOST CONFIGURATION [*] :","yellow")   ,  host_confirm())
else :
    print("[*] PLEASE GIVE ARGUMENTS [*]")

print(colored("===============================================================================================",random.choice(colour)))
print("\n")

print("DIRECTORIES                                                         status_code")

if len(sys.argv) == 3:
    class fuzz():
        def __init__(self):
            
            self.url = sys.argv[1]
            self.file = sys.argv[2]
        
        def requester(self,fuzz_word):
           
            self_requsts_url = self.url+ "/" + fuzz_word        


            try:
                responce = requests.get(self_requsts_url)
                time.sleep(1)
                self.status_code = responce.status_code
                if self.status_code == 200:
                    print(colored(f"{self_requsts_url}                                               {self.status_code}","red"))
                elif self.status_code == 301:
                    print(colored(f"{self_requsts_url}                                               {self.status_code}","yellow"))
                elif self.status_code == 403:
                    print(colored(f"{self_requsts_url}                                               {self.status_code}","blue"))

                else:
                    pass
            except Exception as e:
                print(e)
            except  requests.exceptions.ConnectionError:
                pass
            except requests.ConnectTimeout:
                pass
                

            
        def threading_url(self):
            
            try:
                with open(self.file,"r",encoding="latin-1") as self.words:
                    self.passwords = self.words.read()
                    for self.password in self.passwords.split("\n"):
                        t1 = threading.Thread(target=self.requester,args=(self.password,))
                        t1.start()
                        time.sleep(0.1)
                    t1.join()
            except threading.ThreadError as e:
                print(e)
            except Exception as e:
                pass
        
    fuzz_obj = fuzz()
    fuzz_obj.threading_url()
    print("\n")
    local = datetime.now()
    end_time = local.strftime("%H:%M:%S")
    print(colored("END-TIME :","yellow"),end_time)

else:
    print("""[+] FIRST ARGUMENT : url  [+]
                    [+] SECOND URL : path of fuzzer list [+]

                    EX: python3 FUZZER.py http://0.0.0.0 local.txt

            
            """)
    



