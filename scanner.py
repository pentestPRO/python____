#!/usr/bin/env-python3

import socket
from socket import *
from threading import *
import optparse
import pyfiglet
from termcolor import colored


screenlock = Semaphore(value=1)
ascii_banner = pyfiglet.figlet_format("PORT SCANNER", font = "slant")

def scann(host, port):

    sock = socket(AF_INET,SOCK_STREAM)
    if sock.connect_ex((host, int(port))):
        screenlock.acquire()
        print(colored(f"The port {port} is close","red"))
        
    else:
        screenlock.release()
        print(colored(f"The port {port} is open","blue"))
        
def portscann(host, ports):
    try:
        ip = gethostbyname(host)
        print(ip)
    except:
        print(f"The host is not resolve {[ip]}")
        return
    try:
        name = gethostbyaddr(ip)
        print("Name is ",name)
        print(f"The scanning result for {[name[0]]}")
    except:
        print(f"The scanning result for {[ip]}")
    setdefaulttimeout(1)

    for port in ports:
        T = Thread(target=scann(host, port), args=(host, int(port)))
        T.start()
        

def main():
    print(colored(ascii_banner,"blue"))
    parse = optparse.OptionParser("usage%prog " + "-H <host name or ip address> -p <port number>")
    parse.add_option('-H', dest='host', type='string',  help='specify a host name')
    parse.add_option('-p', dest='port', type='string',  help='specify a port number')
    (options, args) = parse.parse_args()
    host = options.host
    ports = str(options.port).split(',')

    if (host == None) | (ports[0] == None):
        print(parse.usage)
        exit(0)
    portscann(host,ports)
    

if __name__ == '__main__':
    main()
    
