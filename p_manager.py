#!/usr/bin/python3

import sys,os
import string
from termcolor import colored

digit = string.digits
alpha = string.ascii_letters + "" + digit+"#"+"@"+"$"+"!"+"%"+"&"+"*"+"."+"`"
print(len(alpha))
arry_alpha = []

def crypt(password):
    p_word = ""
    for letter in alpha:
       arry_alpha.append(letter)
    for i in password:
        index = arry_alpha.index(i)
        index += 10
        if index >= 71:
            index = index - 71
        word = arry_alpha[index]
        p_word += word
    return p_word


    
def decrypt(password):
    p_word = ""
    for letter in alpha:
       arry_alpha.append(letter)
    for i in password:
        index = arry_alpha.index(i)
        index -= 10 
        word = arry_alpha[index]
        p_word += word
    return p_word
    

def add():
    subject  = input("SUBJECT FOR PASSWORD : ")
    username = input("ENTER USERNAME : ")
    password = input("ENTER PASSWORD : ")
    password = crypt(password)
    with open("important.txt","a") as f:
        f.write( subject + "::"+  username + "::" + password +"\n")

def view():
    try:
        with open("important.txt","r") as file :
            data = file.readlines()
            for creds in data:
                creds = creds.strip("\n")
                subject,username , password = creds.split("::")
                password = colored(decrypt(password),"red")
                username  = colored(username,"blue")
                print(f"PASSWORD FOR {username} IS : {password} ::::::::: {subject}")
    except:
        print("file is empty ")

def edit():
    os.system("nano important.txt")
    sys.exit()

while True:
    user = input("ADD OR VIEW OR EDIT THE PASSWORD PROTECTED FILE : ")

    if user == "add":
        add()
    elif user == "view":
        view()
    elif user == "edit":
        edit()
    else:
        sys.exit(0)