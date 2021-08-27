#!/usr/bin/python3


import dns
import dns.resolver
import time
import threading
import sys
from termcolor import colored





def dnsresolver(domain):
    try:
        domain_name = dns.resolver.resolve(domain, "A")
        if domain_name:

            for name in domain_name:
                print(name)
        else:
            print(" ERROR OCCUR")
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    except threading.ThreadError:
        pass
    except dns.exception.Timeout:
        pass
    except Exception as e:
        pass


with open("/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt", "r") as f:
    subdomain_name = f.read().split("\n")
    for domain in subdomain_name:
        dns_name = domain+"."+"google.com"
        t1 = threading.Thread(target=dnsresolver, args=(dns_name, ))
        
        t1.start()
    t1.join()
