#!/usr/bin/python3

import requests
import threading
from bs4 import BeautifulSoup
import pyfiglet
import sys
import time
from termcolor import colored
from datetime import datetime

global ascii_banner
ascii_banner = pyfiglet.figlet_format("LINK##FINDER", font = "slant")
print(colored(ascii_banner,"red"))
date = datetime.now()
time2 = date.strftime("%H:%M:%S")
print(colored(f"========================================={time2}=========================================","blue"))

if len(sys.argv) == 2:
    print(f"GIVEN URL : {sys.argv[1]}")
    print(colored("=======================================================================================","blue"))

class fuzzer:
    def __init__(self):
        if len(sys.argv) == 2:
            self.url = sys.argv[1]

    
    def link_fuzz(self):
        try:
            if len(sys.argv) == 2:
                n = 0
                self.res = requests.get(self.url)
                self.soup = BeautifulSoup(self.res.text,"html.parser")
                self.data = self.soup.findAll("a")
                for url in self.data:
                    n +=1
                    self.main_link = url.get("href")
                    time.sleep(0.1)
                    print(f"link {colored(n,'red')}    :::::     {colored(self.main_link,'yellow')}")
            else:
                self.usage()
        except Exception as e:
            print(colored("URL IS INCORRECT : ",'red'), sys.argv[1])
    def thread(self):
        if len(sys.argv) == 2:
            t1 = threading.Thread(target=self.link_fuzz)
            t1.start()
            t1.join()
        else:
            self.usage()
    def usage(self):
        print(colored("""
                      ___    ___    ___    ___         
                |  | |___   /___\  | __   |___                                 
                |__|  ___|  |   |  |___|  |___         

            ""","red"))
        print(colored("[*] python3 link_brute.py http://url/  [*]","blue"))



obj = fuzzer()
obj.thread()

print(colored("=======================================================================================","blue"))