

from bs4 import BeautifulSoup
import requests
import threading
import socket

url = input("ENTER THE DOMAIN : ")

class finder:
    def __init__(self,url):
        self.url = url
    def getrequests(self):
        try:
            self.url_name = f"https://{self.url}"
            self.responce = requests.get(self.url_name)
            self.res = self.responce.text
        except Exception as e:
            print("error occur" + e)

    def scraper(self):
        self.data = BeautifulSoup(self.res,"html.parser")
        self.links = self.data.findAll("a")
        self.master = []
        for self.link in self.links:
            self.packet = self.link.get('href')
            self.master.append(self.packet)
        for i in self.master:
            print(f"{i}")

class client:
    def __init__(self,url):
        self.url = url
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def ip(self):
        self.ipaddress = socket.gethostbyaddr(self.url)
        print(f"[*] {self.ipaddress} [*]")

    def file(self):
        try:
            self.code = [200,301]
            url = f"https://{self.url}/robots.txt"
            data = requests.get(url)
            for n in self.code:

                if data.status_code == n:
                    print(data.status_code)
                    print("[*] ROBOT.TXT FILE IS FOUND [*]")
                else:
                    print("[*] ROBOT.TXT FILE IS NOT  FOUND [*] ")

        except Exception as e:
            print(e)


obj1 = client(url)
obj = finder(url)

t1 = threading.Thread(target=obj.getrequests)
t2 = threading.Thread(target=obj.scraper)
t3 = threading.Thread(target=obj1.ip)
t4 = threading.Thread(target=obj1.file)
try:
    t3.start()
    t3.join()

    t4.start()
    t4.join()

    t1.start()
    t1.join()

    t2.start()
    t2.join()
except threading.ThreadError:
    print("THREAD ERROR  IS OCCURED ")