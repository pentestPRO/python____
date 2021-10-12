#!/usr/bin/python3

from typing import Protocol
import pandas
from termcolor import colored
fevicon_hash = input(colored("ENTER THE FEVICON HASH : ","red")) 

def fevicon(user):
    p = pandas.read_csv("fevicon.txt")

    d = pandas.DataFrame(p)
    for i in range(0,363):
        md5 = d['md5hash'][i]
        if user == md5:
            version = d['version'][i]
            comment = colored(" SERVICE or CMS  is : ","blue")
            print(f" {comment} {colored(version,'yellow')}")
        else:
            print("NOT FOUND ANY CMS NAME OR SERVICE NAME ")
            exit(0)

fevicon(fevicon_hash)



