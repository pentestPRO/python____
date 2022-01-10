[*] sock0s [*]

# Date : 10/01/2022

# ->Enumeration Phase:

# Nmap 7.91 scan initiated Mon Jan 10 20:55:32 2022 as: nmap -sC -sV -p- -v -oN nmap_all 192.168.0.102
Nmap scan report for 192.168.0.102
Host is up (0.00041s latency).
Not shown: 65532 filtered ports
PORT     STATE  SERVICE    VERSION
22/tcp   open   ssh        OpenSSH 5.9p1 Debian 5ubuntu1.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 09:3d:29:a0:da:48:14:c1:65:14:1e:6a:6c:37:04:09 (DSA)
|   2048 84:63:e9:a8:8e:99:33:48:db:f6:d5:81:ab:f2:08:ec (RSA)
|_  256 51:f6:eb:09:f6:b3:e6:91:ae:36:37:0c:c8:ee:34:27 (ECDSA)
3128/tcp open   http-proxy Squid http proxy 3.1.19
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported: GET HEAD
|_http-server-header: squid/3.1.19
|_http-title: ERROR: The requested URL could not be retrieved
8080/tcp closed http-proxy
MAC Address: 08:00:27:CE:BB:BA (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 10 20:57:30 2022 -- 1 IP address (1 host up) scanned in 117.58 seconds

>> On port 3128 squid http proxy server is running.
>> squid proxy is intermediate system between server and client. it show all the traffic between server and client. the admin
>> user can change the data also in between.
>> then it also hide running application  which are running on localhost behind the proxy.
>> so i use metasploit and use "auxiliary/scanner/http/squid_pivot_scanning" auxiliary.it bypass the proxy and find which port are
>> open behind the porxy.this auxiliary simply make request to this proxy server using ip "proxy ip and port in which it runnig on"
>> at last this script tells port 80 is open.
>> then i set proxy on phoxyproxy extension on firefox.and visite the 127.0.0.1 website.
>> then i check robots.txt file and in which i found one disallow entry "/wolfcms"
>> wolf is a contentmanagement system for file management for admin-manager.

# ->Exploitation Phase:

>> then i login in to the wolfcms by using cridentials : username=admin&password:admin
>> i found a wolfcms version 0.8.2. by searching on searchsploit find the file upload vulnerbility.

# discription of the vulnerbility:

$
# Exploit Title    : Wolf CMS 0.8.2  Arbitrary File Upload To Command
Execution
# Reported Date    : 05-May-2015
# Fixed Date       : 10-August-2015
# Exploit Author   : Narendra Bhati
# CVE ID           : CVE-2015-6567 , CVE-2015-6568
# Contact:
* Facebook         : https://facebook.com/narendradewsoft
*Twitter           : http://twitter.com/NarendraBhatiB
# Website          : http://websecgeeks.com
# Additional Links -
* https://github.com/wolfcms/wolfcms/releases/
* https://www.wolfcms.org/blog/2015/08/10/releasing-wolf-cms-0-8-3-1.html

#For POC -
http://websecgeeks.com/wolf-cms-arbitrary-file-upload-to-command-execution/

1. Description

Every registered users who have access of upload functionality can upload
an Arbitrary File Upload To perform Command Execution

Vulnerable URL

http://targetsite.com/wolfcms/?/admin/plugin/file_manager/browse/

Vulnerable Parameter

"filename"


2. Proof of Concept

A)Login as regular user ( who have access upload functionality )

B)Go to this page  -
http://targetsite.com/wolfcms/?/admin/plugin/file_manager/browse/

C)Select upload an file option to upload Arbitary File ( filename ex:
"hello.php" )

D)Now you can access the file by here -
http://targetsite.com/wolfcms/public/hello.php


3. Solution:

Update to version 0.8.3.1
http://www.wolfcms.org/download.html

=============

-- 
*Narendra Bhati "CEH" **( Facebook
<http://www.facebook.com/narendradewsoft> , Twitter
<http://www.twitter.com/NarendraBhatiB> , LinkedIn
<https://www.linkedin.com/profile/view?id=115146074> , Personal Blog )*
*Security Analyst - IT Risk & Security Management Services*
Suma Soft Pvt. Ltd. | Suma Center | Near Mangeshkar Hospital | Erandawane
Pune: 411004 |

*======================================================================*
$

>> first upload a php file and then execute it.
>> got a reverse shell of www-data .
>> in the /var/www/html/ directory config.php  file is found in which mysql cridentials are present.
$
define('DB_DSN', 'mysql:dbname=wolf;host=localhost;port=3306'); 
define('DB_USER', 'root'); 
define('DB_PASS', 'john@123'); 
define('TABLE_PREFIX', '');   
$
>> after logging in to the mysql in mysql databases user table found a password hash of user
$ 
password hash : *A7A20B93EC076311A63BF86B5C705B25C054DD77:john@123
$
>> so got a shell of main user. 

# ->PostExploitation Phase:

>> run sudo -l command :
$
(all) all : all
$
>> means run "sudo su" command and get a root access.

# root.txt :a0216ea4d51874464078c618298b1367.txt
>> content of root file
$
If you are viewing this!!
ROOT!
You have Succesfully completed SickOS1.1.
Thanks for Trying
$