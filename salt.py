#!/usr/bin/python3

import crypt

message = input("The password for encrypt : ")
salt = input("Type salt for encryption : ")

data = crypt.crypt(message,salt)
print(data)
