#!/usr/bin/python3

import nmap
import socket
import requests
from bs4 import BeautifulSoup
import lxml
import time
import json
import threading
import pyfiglet
from termcolor import colored

global url
ascii_banner = pyfiglet.figlet_format("WEB_SCANNER", font="slant")
print(colored(ascii_banner, "red"))


def usage():
    print("""
    
    ENTER THE URL LIKE : http://something.com/

    """)


usage()
try:
    url = input(f"[*] {colored('ENTER THE URL','blue')} [*] : ")
except:
    print("ENVALID URL :")
    exit()


def web_scrapper():
    try:
        url0 = url.split("//")
        url1 = url0[1].split("/")
        url2 = url0[0] + "//" + url1[0]

        responce = requests.get(url)
        responce0 = requests.get(url+"/aaaaa")

        bs4 = BeautifulSoup(responce.text, 'lxml')
        bs0 = BeautifulSoup(responce0.text, 'lxml')

        found = bs4.findAll('a')
        found0 = bs4.findAll('link')
        found1 = bs0.findAll('address')

        len1 = len(found) + len(found0)
        for link in found:
            time.sleep(0.5)
            main_link = link.get("href")
            print(colored(url2 + main_link, "yellow"))

        for link0 in found0:
            time.sleep(0.5)
            main_link0 = link0.get("href")
            print(colored(main_link0, "yellow"))

        for link1 in found1:
            version = link1.text[0:14]
            print(version)

        if len1 == 0:
            print("NO LINKS ARE FOUND ")
        else:
            pass

    except Exception as e:
        print("THE URL IS NOT VALID")
        exit(0)


def web_header():
    try:
        responce = requests.get(url)
        hed = responce.headers
        hed = dict(hed)
        headers = json.dumps(hed, indent=7)
        print(colored(headers, "yellow"))
    except Exception as e:
        print(f"ENVALID REQUEST :   \n {e}")
    except IndexError as e:
        print("no")


def web_scanner():
    if "http" in url:

        try:
            main_url = url.split("//")
            main_url0 = main_url[1].split("/")
            host = socket.gethostbyname(main_url0[0])
        except:
            host = url

        try:
            count = -1
            scan = nmap.PortScanner()
            ports = [21, 22, 23, 24, 25, 80, 8080, 8000,3036, 69, 111, 161, 139, 145, 135, 6001]
            for port in ports:
                count += 1
                load = scan.scan(host, str(port))
                status = load['scan'][host]['tcp'][port]['state']
                if status == "open":
                    port_num = ports[count]
                    try:
                        name = ""
                        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        sock.connect((host,int(port_num)))
                        sock.settimeout(0.1)
                        banner = sock.recv(1024).decode().split("\r\n")
                        if not banner:
                            banner = name
                        
                    except Exception as e:
                        print(e)
                    print(f"{colored('OPEN PORT','blue')} : {colored(port,'red')}")
                else:
                    pass

        except Exception as e:
            print(e)
        except IndexError as e:
            print(e)
    else:
        usage()


    

def web_brute():
    if "http" in url:
        url0 = url.split("//")
        url1 = url0[1].split("/")
        url3 = url0[0] + "//"+url1[0]
        responce = requests.get(url3+"/robots.txt")
        responce0 = requests.get(url3+"/sitemap.xml")
        try:
            if responce.status_code == 200:
                print(
                    f"{colored('ROBOTS.TXT','blue')} ::::: {colored('FILE FOUND','red')}")
                print("\n")
                print(colored(responce.text, "blue"))
                print("\n")
            if responce0.status_code == 200:
                print(
                    f"{colored('SITEMAP.XML','blue')} ::::: {colored('FILE FOUND','red')}")
                print("\n")
                print(colored(responce0.text, "blue"))
            elif responce.status_code == 404 & responce.status_code == 404:
                print(
                    f"{colored('ROBOTS.TXT','blue')} ::::: {colored('FILE NOT FOUND','red')}")
                print(
                    f"{colored('SITEMAP.XML','blue')} ::::: {colored('FILE NOT FOUND','red')}")
        except Exception as e:
            print(e)
        except IndexError as e:
            print("no")
    else:
        usage()


# def main_web_scanner():
#     if "http" in url:
#         ports = [21, 22, 23, 24, 25, 80, 8080, 8000,3036, 69, 111, 161, 139, 145, 135, 6001]
#         for port in ports:
#             t1 = threading.Thread(target=web_scanner, args=(port,))
#             t1.start()
#         t1.join()
#     else:
#         usage()


print("\n")
print(
    f"#####################################{colored('web_scrapper','red')}####################################")
web_scrapper()

print('\n')

print(
    f"#####################################{colored('web_brute','red')}####################################")
web_brute()

print("\n")


print(
    f"#####################################{colored('web_headers','red')}####################################")
web_header()

print('\n')

print(
    f"#####################################{colored('web_scanner','red')}####################################")
web_scanner()
